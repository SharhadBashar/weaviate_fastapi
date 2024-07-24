import os
import json
from openai import OpenAI

from prompt import *
from helper import *
from constants import *

class Open_AI:
    def __init__(self):
        if (os.path.exists(PATH_CONFIG)):
            openai_info = read_json(os.path.join(PATH_CONFIG, PATH_OPEN_AI_CONFIG))
            openai_key = openai_info['key']
        else:
            openai_key = os.getenv('OPENAI_KEY')
        self.client = OpenAI(api_key = openai_key)
        
    def generate_menu(self, user):
        response = self.client.chat.completions.create(
            model = MODEL['gpt_4o']['name'],
            messages=[
                {
                    'role': SYSTEM, 
                    'content': SYSTEM_MESSAGE_GEN_MENU},
                {
                    'role': USER, 
                    'content': prompt_menu(user)
                },
            ],
            max_tokens = MAX_TOKENS,
            temperature = TEMPERATURE,
            response_format = RESPONSE_JSON
        )
        diet_plan = json.loads(response.choices[0].message.content)
        week_meal_plan = []
        for day_plan in diet_plan['meal_plan']:
            day = day_plan['day']
            for meal_type, meals in day_plan['meals'].items():
                for meal in meals:
                    week_meal_plan.append({
                        'meal_Id': diet_plan['meal_Id'],
                        'user_Id': diet_plan['user_Id'],
                        'user_name': diet_plan['user_name'],
                        'date': diet_plan['date'],
                        'day': day,
                        'meal_type': meal_type,
                        'meal': meal
                    })
        
        return week_meal_plan
    
    def generate_nutrition_info(self, dish):
        response = self.client.chat.completions.create(
            model = MODEL['gpt_4o']['name'],
            messages=[
                {
                    'role': SYSTEM, 
                    'content': SYSTEM_MESSAGE_GEN_MENU},
                {
                    'role': USER, 
                    'content': prompt_nutrition_info(dish)
                },
            ],
            max_tokens = MAX_TOKENS,
            temperature = TEMPERATURE,
            response_format = RESPONSE_JSON
        )
        return response.choices[0].message.content
