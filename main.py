import time
import random
from typing import Optional
from datetime import datetime
from dotenv import load_dotenv
from urllib.parse import unquote
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, File, UploadFile, Form, HTTPException, Query

from helper import *
from classes import *
from constants import *
from restaurants import *
from open_ai import Open_AI
# from database import Database
from weaviate_db import Weaviate

load_dotenv()

app = FastAPI()
open_ai = Open_AI()
# database = Database()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ['*'], 
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*'],
)

weaviate = Weaviate()

@app.get('/')
async def root():
    return {'message': 'Welcome to the crispy personalized meal plan generator API.'}

@app.get('/distance')
def distance(loc1: dict, loc2: dict):
    return calculate_distance(loc1, loc2)

@app.get('/format_price')
def format_price(price: str):
    return get_format_price(price)

@app.get('/generate_search_link/{search_val}')
async def generate_search_link(search_val: str):
    loc = get_current_location()
    page = search_val
    return f"/{page}?searchval={search_val.strip()}&lat={loc['latitude']}&lon={loc['longitude']}&tmstp={int(time.time())}"

@app.get('/average_price')
def average_price(data: List[Dish_Details]):
    avg_price = round(sum([float(dish.price) for dish in data if dish.price]) / len(data), 2)
    return avg_price or 0

@app.get('/dish_order_links')
def dish_order_links(dish: Dish_Details):
    return get_dish_order_links(dish)

@app.get('/operating_hours')
def operating_hours(client_time_str: str, ubereats_open: str, ubereats_close: str, doordash_schedule: DoorDash_Schedule):
    return get_operating_hours(client_time_str, ubereats_open, ubereats_close, doordash_schedule)

@app.get('/operating_status')
def operating_status(client_time_str: str, opening_time_str: str, closing_time_str: str):
    return get_operating_status(client_time_str, opening_time_str, closing_time_str)

@app.get('/get_operating_hours/{client_time_str}/{restaurant_id}')
def get_operating_hours(client_time_str: str, restaurant_id: str):
    restaurant_hours_data = weaviate.get_restaurant_data_hours(restaurant_id)
    if not restaurant_hours_data:
        raise HTTPException(status_code = 404, detail = f'No restaurant hours data found for the given restaurant ID')
    return get_operating_hours_restaurant(client_time_str, restaurant_hours_data)

@app.get('/get_operating_status/{client_time_str}/{restaurant_id}')
def get_operating_status(client_time_str: str, restaurant_id: str):
    restaurant_hours_data = weaviate.get_restaurant_data_hours(restaurant_id)
    if not restaurant_hours_data:
        raise HTTPException(status_code = 404, detail = f'No restaurant hours data found for the given restaurant ID')
    return get_operating_status_restaurant(client_time_str, restaurant_hours_data)

@app.get('/process_results_data')
def process_results_data(client_time_str: str, dish_data: List[Dish_Details]):
    return get_processed_dish_data(client_time_str, dish_data)

@app.get('/shuffle_array')
def shuffle_array(arr: List):
    random.shuffle(arr)
    return arr

@app.get('/get_master_dish_static')
def get_master_dish_static():
    data = weaviate.get_master_dish_static()
    if not data:
        raise HTTPException(status_code = 404, detail = f'No static master dish data found')
    return data

@app.get('/get_cuisine_static')
def get_cuisine_static():
    data = weaviate.get_cuisine_static()
    if not data:
        raise HTTPException(status_code = 404, detail = f'No static cuisine data found')
    return data

@app.get('/get_diets_static')
def get_diets_static():
    data = weaviate.get_diets_static()
    if not data:
        raise HTTPException(status_code = 404, detail = f'No static diets data found')
    return data

@app.get('/get_popular_dish_static')
def get_popular_dish_static():
    data = weaviate.get_popular_dish_static()
    if not data:
        raise HTTPException(status_code = 404, detail = f'No popular dish data found')
    return data

@app.get('/get_cuisine_data/{cuisine}')
def get_cuisine_data(
    cuisine: str,
    latitude: Optional[float] = Query(DEFAULT_LATITUDE, description = 'Latitude of the location'),
    longitude: Optional[float] = Query(DEFAULT_LONGITUDE, description = 'Longitude of the location'),
    offset: Optional[float] = Query(0, description = 'offset multiplier')
):
    cuisine = unquote(cuisine)
    data = weaviate.get_cuisine_data(cuisine, latitude, longitude, offset = offset)
    if not data:
        raise HTTPException(status_code = 404, detail = f'No data found for the given search term {cuisine} and location')
    return data

@app.get('/get_restaurant_dish_data/{restaurant_id}')
def get_restaurant_dish_data(
    restaurant_id: str,
    offset: Optional[float] = Query(0, description = 'offset multiplier')
):
    data = weaviate.get_restaurant_dish_data(restaurant_id, offset = offset)
    if not data:
        raise HTTPException(status_code = 404, detail = 'No data found for the given restaurant ID')
    return data

@app.get('/get_dish_data/{dish_id}')
def get_dish_data(dish_id: str):
    data = weaviate.get_dish_data(dish_id)
    if not data:
        raise HTTPException(status_code = 404, detail = 'No data found for the given dish ID')
    return data

@app.get('/get_dish_base/{neighborhoods}')
def get_dish_base(neighborhoods: str, offset: Optional[float] = Query(0, description = 'offset multiplier')):
    neighborhoods = unquote(neighborhoods)
    data = weaviate.get_dish_base(neighborhoods, offset = offset)
    if not data:
        raise HTTPException(status_code = 404, detail = 'No data found for the given neighborhoods')
    return data

@app.get('/get_dish_combined/{neighborhoods}')
def get_dish_combined(neighborhoods: str, offset: Optional[float] = Query(0, description = 'offset multiplier')):
    neighborhoods = unquote(neighborhoods)
    data = weaviate.get_dish_combined(neighborhoods, offset = offset)
    if not data:
        raise HTTPException(status_code = 404, detail = 'No data found for the given neighborhoods')
    return data

@app.get('/get_dish_cuisine/{neighborhoods}/{cuisines}')
def get_dish_cuisine(neighborhoods: str, cuisines: str, offset: Optional[float] = Query(0, description = 'offset multiplier')):
    neighborhoods = unquote(neighborhoods)
    cuisines = unquote(cuisines)
    data = weaviate.get_dish_cuisine(neighborhoods, cuisines, offset = offset)
    if not data:
        raise HTTPException(status_code = 404, detail = 'No data found for the given neighborhoods and cuisines')
    return data

@app.get('/get_dish_diets/{neighborhoods}/{diets}')
def get_dish_diets(neighborhoods: str, diets: str, offset: Optional[float] = Query(0, description = 'Offset multiplier')):
    neighborhoods = unquote(neighborhoods)
    diets = unquote(diets)
    data = weaviate.get_dish_diets(neighborhoods, diets, offset = offset)
    if not data:
        raise HTTPException(status_code = 404, detail = 'No data found for the given neighborhoods and diets')
    return data

@app.get('/get_dish_popular/{neighborhoods}/{dishes}')
def get_dish_popular(neighborhoods: str, dishes: str, offset: Optional[float] = Query(0, description = 'offset multiplier')):
    neighborhoods = unquote(neighborhoods)
    dishes = unquote(dishes)
    data = weaviate.get_dish_popular(neighborhoods, dishes, offset = offset)
    if not data:
        raise HTTPException(status_code = 404, detail = 'No data found for the given neighborhoods and dishes')
    return data

@app.get('/get_closest_neighbourhoods')
def closest_neighbourhoods(
    latitude: Optional[float] = Query(DEFAULT_LATITUDE, description = 'Latitude of the location'),
    longitude: Optional[float] = Query(DEFAULT_LONGITUDE, description = 'Longitude of the location'),
    k: Optional[int] = Query(CLOSEST_NEIGHBOURHOOD_K, description = 'Number of closest neighbourhoods to return')
):
    data = get_closest_neighbourhoods(latitude, longitude, k = k)
    if not data:
        raise HTTPException(status_code = 404, detail = 'No closest neighbourhoods found for the given coordinates')
    return data

@app.get('/get_single_dish_search/{dish}')
def get_single_dish_search(
    dish: str,
    weaviate_limit: Optional[int] = Query(10, description = 'Number of dishes to return'),
    latitude: Optional[float] = Query(DEFAULT_LATITUDE, description = 'Latitude of the location'),
    longitude: Optional[float] = Query(DEFAULT_LONGITUDE, description = 'Longitude of the location'),
    offset: Optional[float] = Query(0, description = 'offset multiplier'),
    neighborhoods: Optional[List[str]] = Query(None, description = 'List of neighborhoods to filter dishes by'),
    has_unique_image: Optional[bool] = Query(False, description = 'Whether to filter dishes with unique images')
):
    dish = unquote(dish)
    data = weaviate.get_single_dish_search(
        dish,
        neighborhoods = neighborhoods,
        has_unique_image = has_unique_image,
        weaviate_limit = weaviate_limit, 
        latitude = latitude, 
        longitude = longitude,
        offset = offset
    )
    if not data:
        raise HTTPException(status_code = 404, detail = 'No dishes found for the given search term')
    return data

@app.get('/get_search_dishes_ios/{dish}')
def get_search_dishes_ios(
    dish: str,
    weaviate_limit: Optional[int] = Query(10, description = 'Number of dishes to return'),
    max_alternatives: Optional[int] = Query(3, description = 'Maximum number of alternatives to return'),
    neighborhoods: Optional[List[str]] = Query(None, description = 'List of neighborhoods to filter dishes by'),
    has_unique_image: Optional[bool] = Query(False, description = 'Whether to filter dishes with unique images')
):
    dish = unquote(dish)
    initial_dishes = weaviate.get_dish_data_ios(dish, weaviate_limit, neighborhoods, has_unique_image)
    alternatives = weaviate.combine_alternatives_ios(initial_dishes, max_alternatives)
    alternative_dishes = weaviate.get_alternative_dish_data_ios(alternatives, weaviate_limit, neighborhoods, has_unique_image)
    data = {dish: initial_dishes}
    data.update(alternative_dishes)
    if not data:
        raise HTTPException(status_code = 404, detail = 'No dishes found for the given search term')
    return data

@app.get('/get_search_dishes/{query_type}/{query_value}')
def get_search_dishes(
    query_type: str,
    query_value: str,
    neighborhoods: Optional[List[str]] = Query(None, description = 'List of neighborhoods'),
    has_unique_image: bool = Query(False, description = 'Whether to filter dishes with unique images'),
    weaviate_limit: int = Query(10, description = 'Number of dishes to search for in weaviate'),
    max_alternatives: int = Query(3, description = 'Maximum number of alternatives to return'),
    num_dishes: int = Query(10, description = 'Number of dishes to return'),
    latitude: Optional[float] = Query(DEFAULT_LATITUDE, description = 'Latitude of the location'),
    longitude: Optional[float] = Query(DEFAULT_LONGITUDE, description = 'Longitude of the location'),
    offset: int = Query(0, description = 'Offset multiplier'),
):
    data = weaviate.get_search_dishes(
        query_type, 
        query_value, 
        neighborhoods = neighborhoods, 
        has_unique_image = has_unique_image, 
        weaviate_limit = weaviate_limit, 
        max_alternatives = max_alternatives,
        num_dishes = num_dishes,
        latitude = latitude,
        longitude = longitude,
        offset = offset
    )
    if not data:
        raise HTTPException(status_code = 404, detail = 'No dishes found for the given query type and value')
    return data
    

# @app.post('/generate_menu')
# async def generate_meal_plan(user: User):
#     week_meal_plan = open_ai.generate_menu(user)
#     df = pd.DataFrame(week_meal_plan)
#     database.insert_df(df, 'public.DietPlans')
#     print(df.head())
#     print('data inserted into cockroach')
#     print(f'Raw response content: {week_meal_plan}')
#     return week_meal_plan

@app.post('/nutrition_info/')
async def generate_nutrition_info(dish: Dish, file: UploadFile = File(None)):
    dish_info = {}
    if dish.name: dish_info['name'] = dish.name
    if dish.description: dish_info['description'] = dish.description
    if dish.dish_Id: dish_info['dish_Id'] = dish.dish_Id
    if dish.user_Id: dish_info['userId'] = dish.user_Id
    if dish.user_name: dish_info['userName'] = dish.user_name
    if not dish_info:
        raise HTTPException(status_code = 400, detail = 'No valid input provided. Please provide a name and/or description.')

    nutrition_info = open_ai.generate_nutrition_info(dish_info)

    print(f"Raw response content: {nutrition_info}")
    return nutrition_info
    