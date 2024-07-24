from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Optional, Dict
from geopy.distance import geodesic
import requests

app = FastAPI()

# Define types and constants

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