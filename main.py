import time
import random
from typing import Optional
from datetime import datetime
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, File, UploadFile, Form, HTTPException, Query

from helper import *
from classes import *
from constants import *
from restaurants import *
from open_ai import Open_AI
from database import Database
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

@app.get('/process_results_data')
def process_results_data(client_time_str: str, dish_data: List[Dish_Details]):
    return get_processed_dish_data(client_time_str, dish_data)

@app.get('/shuffle_array')
def shuffle_array(arr: List):
    random.shuffle(arr)
    return arr

@app.get('/get_cuisine_data/{cusine}')
def get_cuisine_data(
    cusine: str,
    latitude: Optional[float] = Query(DEAFULT_LATITUDE, description = 'Latitude of the location'),
    longitude: Optional[float] = Query(DEFAULT_LONGITUDE, description = 'Longitude of the location')
):
    data = weaviate.get_cuisine_data(cusine, latitude, longitude)
    if not data:
        raise HTTPException(status_code = 404, detail = 'No data found for the given search term and location')
    return data

@app.get('/get_restaurant_dish_data/{restaurant_id}')
def get_restaurant_dish_data(
    restaurant_id: str
):
    data = weaviate.get_restaurant_dish_data(restaurant_id)
    if not data:
        raise HTTPException(status_code = 404, detail = 'No data found for the given search term and location')
    return data




@app.post('/generate_menu')
async def generate_meal_plan(user: User):
    week_meal_plan = open_ai.generate_menu(user)
    df = pd.DataFrame(week_meal_plan)
    database.insert_df(df, 'public.DietPlans')
    print(df.head())
    print('data inserted into cockroach')
    print(f'Raw response content: {week_meal_plan}')
    return week_meal_plan

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
    