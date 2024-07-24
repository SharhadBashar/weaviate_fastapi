from datetime import datetime, timedelta

from helper import *
from classes import *

def get_dish_order_links(dish: Dish_Details) -> Dict[str, str]:
    link_door_dash = dish.foodItemLinkDoorDash or dish.linkDoorDash or 'None'
    link_uber_eats = (
        dish.foodItemUberCartLinks if dish.foodItemUberCartLinks not in ['None', 'Invalid store identifier in the URL'] else
        dish.foodItemLinkUber if dish.foodItemLinkUber != 'None' else
        dish.linkUber if dish.linkUber != 'None' else
        'None'
    )
    return {'doordash': link_door_dash, 'ubereats': link_uber_eats}

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

def get_operating_hours(client_timestamp: str, ubereats_open: str = None, ubereats_close: str = None, doordash_schedule: DoorDash_Schedule = None) -> Dict[str, str]:
    if (ubereats_open and ubereats_close):
        return {'open': ubereats_open, 'close': ubereats_close, 'source': 'uber'}
    else:
        open_time, close_time = getattr(doordash_schedule, get_day_of_week(client_timestamp)).split(' - ')
        return {'open': open_time, 'close': close_time, 'source': 'doordash'}
