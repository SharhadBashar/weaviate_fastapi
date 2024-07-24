import logging
import os
from dotenv import load_dotenv
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI, File, UploadFile, Form, HTTPException

import open_ai
import database

from helper import *
from classes import *
from open_ai import Open_AI
from database import Database

load_dotenv()

app = FastAPI()
open_ai = Open_AI()
database = Database()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ['*'], 
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*'],
)

@app.get('/')
async def read_root():
    return {'message': 'Welcome to the crispy personalized meal plan generator API.'}

@app.post('/generate_menu')
async def generate_meal_plan(user: User):
    week_meal_plan = open_ai.generate_menu(user)
    df = pd.DataFrame(week_meal_plan)
    database.insert_df(df, 'public.DietPlans')
    print(df.head())
    print('data inserted into cockroach')
    print(f'Raw response content: {week_meal_plan}')
    return week_meal_plan

@app.post("/nutrition_info/")
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
    