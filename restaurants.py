from pprint import pprint
from haversine import haversine, Unit
from datetime import datetime, timedelta

from helper import *
from classes import *
from constants import *
from neighbourhoods import NEIGHBOURHOODS

def get_dish_order_links(dish: Dish_Details) -> Dict[str, str]:
    link_door_dash = dish.foodItemLinkDoorDash or dish.linkDoorDash or 'None'
    link_uber_eats = (
        dish.foodItemUberCartLinks if dish.foodItemUberCartLinks not in ['None', 'Invalid store identifier in the URL'] else
        dish.foodItemLinkUber if dish.foodItemLinkUber != 'None' else
        dish.linkUber if dish.linkUber != 'None' else
        'None'
    )
    return {'doordash': link_door_dash, 'ubereats': link_uber_eats}

def get_operating_hours(client_time_str: str, ubereats_open: str = None, ubereats_close: str = None, doordash_schedule: DoorDash_Schedule = None) -> Dict[str, str]:
    if (ubereats_open and ubereats_close):
        return {'open': ubereats_open, 'close': ubereats_close, 'source': 'uber'}
    else:
        open_time, close_time = getattr(doordash_schedule, get_day_of_week(client_time_str)).split(' - ')
        return {'open': open_time, 'close': close_time, 'source': 'doordash'}

def get_operating_status(client_time_str, opening_time_str, closing_time_str):
    client_time = datetime.strptime(client_time_str, '%H:%M')
    opening_time = datetime.strptime(opening_time_str, '%H:%M')
    closing_time = datetime.strptime(closing_time_str, '%H:%M')
    if (closing_time <= opening_time):
        closing_time += timedelta(days = 1)
        if (client_time < opening_time):
            client_time += timedelta(days = 1)
    is_open = opening_time <= client_time < closing_time
    closing_soon = is_open and (closing_time - client_time <= timedelta(hours = 1))
    return {'closed': is_open, 'closing_soon': closing_soon}

def get_operating_hours_restaurant(client_time_str, restaurant_hours_data):
    hours = {'open': 'Closed', 'close': 'Closed', 'source': 'none'}

    uber_open_close = restaurant_hours_data.get('openingHours_UberEats_uber', 'None')
    if uber_open_close != 'None':
        uber_open, uber_close = uber_open_close.split('-')
        hours = {'open': uber_open, 'close': uber_close, 'source': 'uber'}

    day_of_week = get_day_of_week(client_time_str)
    doordash_hours = restaurant_hours_data.get(f'{day_of_week}DoorDash', 'Closed')
    if doordash_hours != 'Closed':
        open_time, close_time = doordash_hours.split(' - ')
        hours = {'open': open_time, 'close': close_time, 'source': 'doordash'}

    return {
        'linkDoorDash': restaurant_hours_data.get('linkDoorDash', 'None'),
        'linkUber': restaurant_hours_data.get('linkUber', 'None'),
        'restaurantAddress': restaurant_hours_data.get('restaurantAddress', 'None'),
        'restaurantName': restaurant_hours_data.get('restaurantName', 'None'),
        'restaurantPhone': restaurant_hours_data.get('restaurantPhone', 'None'),  
        **hours
    }

def get_operating_status_restaurant(client_time_str, restaurant_hours_data):
    operating_hours = get_operating_hours_restaurant(client_time_str, restaurant_hours_data)
    if (operating_hours['open'] == 'Closed'):
        operating_status = {'is_open': False, 'closing_soon': False}

    client_time = datetime.strptime(client_time_str, '%Y-%m-%d %H:%M:%S')
    opening_time = datetime.strptime(operating_hours['open'], '%H:%M').time()
    closing_time = datetime.strptime(operating_hours['close'], '%H:%M').time()
    if (closing_time <= opening_time):
        closing_time = (datetime.combine(datetime.min, closing_time) + timedelta(days=1)).time()
        if (client_time.time() < opening_time):
            client_time += timedelta(days = 1)

    is_open = opening_time <= client_time.time() < closing_time
    closing_soon = is_open and (datetime.combine(datetime.min, closing_time) - datetime.combine(datetime.min, client_time.time()) <= timedelta(hours = 1))
    operating_status = {'is_open': is_open, 'closing_soon': closing_soon}
    return {
        'linkDoorDash': restaurant_hours_data.get('linkDoorDash', 'None'),
        'linkUber': restaurant_hours_data.get('linkUber', 'None'),
        'restaurantAddress': restaurant_hours_data.get('restaurantAddress', 'None'),
        'restaurantName': restaurant_hours_data.get('restaurantName', 'None'),
        'restaurantPhone': restaurant_hours_data.get('restaurantPhone', 'None'),  
        **operating_status
    }

def get_processed_dish_data(client_time_str: str, dish_data: List[Dish_Details]) -> List[Dish_Details]:
    processed_dish_data = []
    for dish in dish_data:
        doordash_schedule = DoorDash_Schedule(
            monday = dish.doordash_monday,
            tuesday = dish.doordash_tuesday,
            wednesday = dish.doordash_wednesday,
            thursday = dish.doordash_thursday,
            friday = dish.doordash_friday,
            saturday = dish.doordash_saturday,
            sunday = dish.doordash_sunday
        )
        operating_hours = get_operating_hours(client_time_str, dish.ubereats_open, dish.ubereats_close, doordash_schedule)
        operating_status = get_operating_status(client_time_str, operating_hours['open'], operating_hours['close'])
        dish.operation = {**operating_hours, **operating_status}
        dish.closed = dish.operations['closed']
        order_links = get_dish_order_links(dish)
        dish.doordash_order_link = order_links['doordash']
        dish.ubereats_order_link = order_links['ubereats']
        dish.restaurant_rating = dish.restaurant_rating or 0
        dish.price = get_format_price(dish.price)
        if (dish.calorie > 0):
            dish.fat = round(float(dish.mass_fat) / float(dish.calorie), 2) or 0
            dish.carbs = round(float(dish.mass_carbs) / float(dish.calorie), 2) or 0
            dish.protein = round(float(dish.mass_protein) / float(dish.calorie), 2) or 0
        else:
            dish.fat = 0
            dish.carbs = 0
            dish.protein = 0
        processed_dish_data.append(dish)
    return processed_dish_data

def get_closest_neighbourhoods(latitude = DEFAULT_LATITUDE, longitude = DEFAULT_LONGITUDE, k = CLOSEST_NEIGHBOURHOOD_K) -> list:
    closest_neighbourhoods = []
    for i in range(k):
        closest_distance = float('inf')
        for neighbourhood in NEIGHBOURHOODS:
            distance = haversine((latitude, longitude), (neighbourhood['latitude'], neighbourhood['longitude']))
            if (distance < closest_distance and neighbourhood not in closest_neighbourhoods):
                closest_distance = distance
                closest_neighbourhood = neighbourhood
        closest_neighbourhoods.append(closest_neighbourhood)
    return closest_neighbourhoods


if __name__ == '__main__':
    # pprint(get_operating_hours_restaurant('2023-10-05 12:00:00', restaurant_hours_data_1))
    # pprint(get_operating_hours_restaurant('2023-10-05 12:00:00', restaurant_hours_data_2))
    # pprint(get_operating_status_restaurant('2023-10-05 12:00:00', restaurant_hours_data_1))
    pprint(get_operating_status_restaurant('2024-06-29 11:00:00', restaurant_hours_data_2))
