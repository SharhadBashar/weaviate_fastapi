from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Optional, Dict
from geopy.distance import geodesic
import requests

app = FastAPI()

# Define types and constants
class TCoordinates(BaseModel):
    Latitude: float
    Longitude: float

class TDistance(BaseModel):
    rawDistance: float
    distanceLabel: str

class DishDetails(BaseModel):
    dishRes_ID: Optional[str]
    dish_ID: Optional[str]
    restaurant_ID: Optional[str]
    _additional: Optional[Dict]
    geoCoordinates: Optional[TCoordinates]
    dishName: Optional[str]
    calorie_Count_Estimate: Optional[str]
    cleanedDishName: Optional[str]
    dietTags: Optional[List[str]]
    foodItemLinkUber: Optional[str]
    foodItemLinkDoorDash: Optional[str]
    foodItemUberCartLinks: Optional[str]
    healthAlternatives: Optional[str]
    mass_Carbs: Optional[str]
    mass_Fat: Optional[str]
    mass_Protein: Optional[str]
    imageDoorDash: Optional[str]
    imageUber: Optional[str]
    linkUber: Optional[str]
    linkDoorDash: Optional[str]
    priceClean: Optional[str]
    closeTime_UberEats_uber: Optional[str]
    daysOpen_UberEats_uber: Optional[str]
    monDoorDash: Optional[str]
    tueDoorDash: Optional[str]
    wedDoorDash: Optional[str]
    thuDoorDash: Optional[str]
    friDoorDash: Optional[str]
    satDoorDash: Optional[str]
    sunDoorDash: Optional[str]
    lat: Optional[float]
    long: Optional[float]
    neighborhood: Optional[str]
    openCloseHours: Optional[str]
    openingHours_UberEats_uber: Optional[str]
    restaurantName: Optional[str]
    restaurantPhone: Optional[str]
    restaurantRating: Optional[str]
    restaurantReviewCount: Optional[int]
    eater_ReviewDictVec: Optional[Dict]
    infatuation_ReviewDictVec: Optional[Dict]

class TDoorDashOperatingTimes(BaseModel):
    monDoorDash: Optional[str]
    tueDoorDash: Optional[str]
    wedDoorDash: Optional[str]
    thuDoorDash: Optional[str]
    friDoorDash: Optional[str]
    satDoorDash: Optional[str]
    sunDoorDash: Optional[str]

class OperatingStatus(BaseModel):
    closed: bool
    closingSoon: bool

defaultClientLatitude = 40.7128
defaultClientLongitude = -74.0060

# Helper functions
def calculate_distance(loc1: TCoordinates, loc2: TCoordinates) -> TDistance:
    loc1_coords = (loc1.Latitude, loc1.Longitude)
    loc2_coords = (loc2.Latitude, loc2.Longitude)
    distance_in_kilometers = geodesic(loc1_coords, loc2_coords).kilometers
    distance_in_miles = distance_in_kilometers * 0.621371
    if distance_in_miles < 0.2:
        distance_label = f"{round(distance_in_miles * 5280)} feet"
    else:
        distance_label = f"{round(distance_in_miles * 100) / 100} miles"
    return TDistance(rawDistance=distance_in_miles, distanceLabel=distance_label)

def format_price(price: str) -> str:
    try:
        formatted_price = f"{float(price):.2f}"
    except ValueError:
        formatted_price = ""
    return formatted_price if formatted_price != "0.00" else ""

def get_current_location():
    # Replace with actual implementation to get the current location
    return {"latitude": defaultClientLatitude, "longitude": defaultClientLongitude}

def get_dish_order_links(dish: DishDetails) -> Dict[str, str]:
    link_door_dash = dish.foodItemLinkDoorDash if dish.foodItemLinkDoorDash != 'None' else (
        dish.linkDoorDash if dish.linkDoorDash != 'None' else 'None')
    link_uber_eats = dish.foodItemUberCartLinks if dish.foodItemUberCartLinks != 'None' and dish.foodItemUberCartLinks != 'Invalid store identifier in the URL' else (
        dish.foodItemLinkUber if dish.foodItemLinkUber != 'None' else (
            dish.linkUber if dish.linkUber != 'None' else 'None'))
    return {"doordash": link_door_dash, "ubereats": link_uber_eats}

def get_operating_hours(client_timestamp: str, uber_eats_opening_time: str, uber_eats_closing_time: str, door_dash_operating_times: TDoorDashOperatingTimes) -> Dict[str, str]:
    client_date = int(client_timestamp)
    if uber_eats_opening_time != 'None' and uber_eats_closing_time != 'None':
        open_time = uber_eats_opening_time
        close_time = uber_eats_closing_time
        source = 'uber'
    else:
        day_of_week = ["sunDoorDash", "monDoorDash", "tueDoorDash", "wedDoorDash", "thuDoorDash", "friDoorDash", "satDoorDash"][client_date % 7]
        open_time, close_time = getattr(door_dash_operating_times, day_of_week).split(' - ')
        source = 'doordash'
    return {"open": open_time, "close": close_time, "source": source}

def get_operating_status(client_timestamp: str, opening_time_str: str, closing_time_str: str) -> OperatingStatus:
    client_time = int(client_timestamp)
    opening_time = int(opening_time_str.split(':')[0])
    closing_time = int(closing_time_str.split(':')[0])
    if closing_time < opening_time:
        closing_time += 24
    closed = client_time < opening_time or client_time >= closing_time
    return OperatingStatus(closed=closed, closingSoon=False)

def process_results_data(client_time: str, results_data: List[DishDetails]) -> List[DishDetails]:
    processed_data = []
    for dish in results_data:
        uber_eats_opening_time = dish.daysOpen_UberEats_uber
        uber_eats_closing_time = dish.closeTime_UberEats_uber
        door_dash_operating_times = TDoorDashOperatingTimes(
            monDoorDash=dish.monDoorDash,
            tueDoorDash=dish.tueDoorDash,
            wedDoorDash=dish.wedDoorDash,
            thuDoorDash=dish.thuDoorDash,
            friDoorDash=dish.friDoorDash,
            satDoorDash=dish.satDoorDash,
            sunDoorDash=dish.sunDoorDash,
        )
        operating_hours = get_operating_hours(client_time, uber_eats_opening_time, uber_eats_closing_time, door_dash_operating_times)
        operating_status = get_operating_status(client_time, operating_hours["open"], operating_hours["close"])

        dish.operations = {**operating_hours, **operating_status.dict()}
        order_links = get_dish_order_links(dish)
        dish.preferredLinkDoorDash = order_links["doordash"]
        dish.preferredLinkUberEats = order_links["ubereats"]
        dish.restaurantRating = '0' if dish.restaurantRating == 'nan' else dish.restaurantRating
        if float(dish.calorie_Count_Estimate) > 0:
            dish.pct_Fat = round(float(dish.mass_Fat) / float(dish.calorie_Count_Estimate), 2) or 0
            dish.pct_Carbs = round(float(dish.mass_Carbs) / float(dish.calorie_Count_Estimate), 2) or 0
            dish.pct_Protein = round(float(dish.mass_Protein) / float(dish.calorie_Count_Estimate), 2) or 0
        else:
            dish.pct_Fat = 0
            dish.pct_Carbs = 0
            dish.pct_Protein = 0
        dish.closed = dish.operations["closed"]
        dish.priceClean = format_price(dish.priceClean)
        processed_data.append(dish)
    return processed_data

def shuffle_array(arr: List):
    import random
    random.shuffle(arr)
    return arr

# API Endpoints
@app.post("/calculate_distance")
def api_calculate_distance(loc1: TCoordinates, loc2: TCoordinates):
    return calculate_distance(loc1, loc2)

@app.post("/format_price")
def api_format_price(price: str):
    return format_price(price)

@app.get("/generate_search_link/{search_val}")
async def api_generate_search_link(search_val: str):
    loc = get_current_location()
    page = search_val  # Dummy implementation, replace with actual page calculation
    return f"/{page}?searchval={search_val.strip()}&lat={loc['latitude']}&lon={loc['longitude']}&tmstp={int(time.time())}"

@app.post("/get_average_price")
def api_get_average_price(data: List[DishDetails]):
    avg_price = round(sum([float(d.priceClean) for d in data if d.priceClean]) / len(data), 2)
    return str(avg_price) if not avg_price == "NaN" else "0"

@app.post("/get_dish_order_links")
def api_get_dish_order_links(dish: DishDetails):
    return get_dish_order_links(dish)

@app.post("/get_operating_hours")
def api_get_operating_hours(client_timestamp: str, uber_eats_opening_time: str, uber_eats_closing_time: str, door_dash_operating_times: TDoorDashOperatingTimes):
    return get_operating_hours(client_timestamp, uber_eats_opening_time, uber_eats_closing_time, door_dash_operating_times)

@app.post("/get_operating_status")
def api_get_operating_status(client_timestamp: str, opening_time_str: str, closing_time_str: str):
    return get_operating_status(client_timestamp, opening_time_str, closing_time_str)

@app.post("/process_results_data")
def api_process_results_data(client_time: str, results_data: List[DishDetails]):
    return process_results_data(client_time, results_data)

@app.post("/shuffle_array")
def api_shuffle_array(arr: List):
    return shuffle_array(arr)