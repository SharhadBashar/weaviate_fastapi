from fastapi import FastAPI, File, UploadFile, Form, HTTPException
import openai
from openai import OpenAI
from pydantic import BaseModel
import os
import logging
import json
from datetime import datetime
import uuid
print("running")

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = FastAPI()

@app.get("/")
async def health_check():
    return "welcome to the crispy health api"



# Pydantic model for user profile
class UserProfile(BaseModel):
    userId: int
    userName: str
    Name: str
    Age: int
    Gender: str
    Height_cm: int
    Weight_kg: int
    Primary_Health_Goals: str
    Flavor_Preferences: str
    Cuisine_Preferences: str
    Dietary_Preferences: str
    Meal_Budget: str
    Budget_Per_Meal: str
    Allergies_and_Restrictions: str
    Meal_Frequency: str
    Meal_Types: str
    Preferred_Eating_Times: str
    Activity_Level: str
    Target_Weight_kg: int
    Timeline_for_Goals: str
    Preferred_Workout_Days: str




@app.post("/generate-menu")
async def generate_meal_plan(user_profile: UserProfile):
    # Generate a UUID for the meal plan

    try:
        # ratingCategory = data.get("ratingCategory")
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        prompt = f"""
            Generate a -day meal plan with 3 options per meal for the following user profile: Only generate dishes that are relativley common for restaurants to carry
            
            Name: {user_profile.Name}
            Age: {user_profile.Age}
            Gender: {user_profile.Gender}
            Height: {user_profile.Height_cm} cm
            Weight: {user_profile.Weight_kg} kg
            Primary Health Goals: {user_profile.Primary_Health_Goals}
            Flavor Preferences: {user_profile.Flavor_Preferences}
            Cuisine Preferences: {user_profile.Cuisine_Preferences}
            Dietary Preferences: {user_profile.Dietary_Preferences}
            Meal Budget: {user_profile.Meal_Budget}
            Budget_Per_Meal: {user_profile.Budget_Per_Meal}
            Allergies and Restrictions: {user_profile.Allergies_and_Restrictions}
            Meal Frequency: {user_profile.Meal_Frequency}
            Meal Types: {user_profile.Meal_Types}
            Preferred Eating Times: {user_profile.Preferred_Eating_Times}
            Activity Level: {user_profile.Activity_Level}
            Target Weight: {user_profile.Target_Weight_kg} kg
            Timeline for Goals: {user_profile.Timeline_for_Goals}
            Preferred Workout Days: {user_profile.Preferred_Workout_Days}

        Provide the meal plan in the following JSON format:
        {{"mealUUID": "{str(uuid.uuid4())}",
        "userId": "{user_profile.userId}",
        "userName": "{user_profile.userName}",
        "date": "{datetime.now().strftime('%Y-%m-%d %H:%M')}",
        
      
        {{
        "meal_plan": [
            {{
                "day": 1,
                "meals": {{
                    "breakfast": [
                        "Avocado Toast",
                        "Greek Yogurt with Honey and Berries",
                        "Smoothie Bowl"
                    ],
                    "lunch": [
                        "Quinoa Salad",
                        "Veggie Wrap",
                        "Falafel Salad"
                    ],
                    "dinner": [
                        "Vegetarian Sushi",
                        "Vegetarian Stir-fry",
                        "Vegetarian Pad Thai"
                    ]
                }}
            }},
            {{
                "day": 2,
                "meals": {{
                    "breakfast": [
                        "Chia Seed Pudding",
                        "Overnight Oats",
                        "Smoothie with Spinach, Banana, and Almond Milk"
                    ],
                    "lunch": [
                        "Hummus Plate",
                        "Grilled Vegetable Panini",
                        "Caprese Sandwich"
                    ],
                    "dinner": [
                        "Vegetarian Pizza",
                        "Vegetarian Curry",
                        "Vegetarian Tacos"
                    ]
                }}
            }},
            {{
                "day": 3,
                "meals": {{
                    "breakfast": [
                        "Acai Bowl",
                        "Banana Bread",
                        "Protein Smoothie"
                    ],
                    "lunch": [
                        "Lentil Soup",
                        "Stuffed Peppers",
                        "Chickpea Salad"
                    ],
                    "dinner": [
                        "Vegetarian Samosas",
                        "Vegetarian Burrito",
                        "Vegetarian Pasta"
                    ]
                }}
            }}]
    }} 
    }}
        """

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a harvard educated AI nutritionist that provides single item meals that can be ordered through Uber Eats and Doordash. Respond only with valid JSON."},
                {"role": "user", "content": prompt},

            ],
            max_tokens=4096,
            temperature=0.7,
            response_format={"type": "json_object"}
        )
        
        # Debugging: Print the raw response content
        raw_response_content = response.choices[0].message.content
        

        return raw_response_content


    except openai.OpenAIError as oe:
            logging.error(f"OpenAI error: {oe}")
            raise HTTPException(status_code=500, detail="Error interacting with OpenAI")
        
        
@app.post("/menu-prescription")
async def generate_meal_plan(user_profile: UserProfile):
    try:
        prompt = f"""
        Generate a personalized daily meal plan with macros and calories for the following user profile. Only generate dishes that are relatively common for restaurants to carry.

        Name: {user_profile.Name}
        Age: {user_profile.Age}
        Gender: {user_profile.Gender}
        Height: {user_profile.Height_cm} cm
        Weight: {user_profile.Weight_kg} kg
        Primary Health Goals: {user_profile.Primary_Health_Goals}
        Flavor Preferences: {user_profile.Flavor_Preferences}
        Cuisine Preferences: {user_profile.Cuisine_Preferences}
        Dietary Preferences: {user_profile.Dietary_Preferences}
        Meal Budget: {user_profile.Meal_Budget}
        Budget Per Meal: {user_profile.Budget_Per_Meal}
        Allergies and Restrictions: {user_profile.Allergies_and_Restrictions}
        Meal Frequency: {user_profile.Meal_Frequency}
        Meal Types: {user_profile.Meal_Types}
        Preferred Eating Times: {user_profile.Preferred_Eating_Times}
        Activity Level: {user_profile.Activity_Level}
        Target Weight: {user_profile.Target_Weight_kg} kg
        Timeline for Goals: {user_profile.Timeline_for_Goals}
        Preferred Workout Days: {user_profile.Preferred_Workout_Days}

        Provide the meal plan in the following JSON format:
        {{
            "mealUUID": "{str(uuid.uuid4())}",
            "userId": "{user_profile.userId}",
            "userName": "{user_profile.userName}",
            "date": "{datetime.now().strftime('%Y-%m-%d %H:%M')}",
            "daily_macros_and_calories": {{
                "calories": 2500,
                "justification": "Based on {user_profile.Name}'s active lifestyle, age, gender, height, weight, and goal to maintain weight, a daily intake of 2500 calories is appropriate to sustain his current weight and activity level.",
                "macros": {{
                    "protein": {{
                        "grams": 125,
                        "calories": 500,
                        "justification": "20% of the total caloric intake is allocated to protein to support muscle maintenance and recovery, which is essential given {user_profile.Name}'s active lifestyle and vegetarian diet."
                    }},
                    "carbohydrates": {{
                        "grams": 312.5,
                        "calories": 1250,
                        "justification": "50% of the total caloric intake is allocated to carbohydrates to provide sufficient energy for daily activities and workouts, aligning with {user_profile.Name}'s preference for a balanced and active lifestyle."
                    }},
                    "fats": {{
                        "grams": 83.3,
                        "calories": 750,
                        "justification": "30% of the total caloric intake is allocated to fats to ensure adequate intake of essential fatty acids and to support overall health and hormone regulation, suitable for {user_profile.Name}'s dietary preferences and budget."
                    }}
                }}
            }}
        }}
        """

        response = openai.Completion.create(
            model="gpt-4",
            prompt=prompt,
            max_tokens=4096,
            temperature=0.7
        )
        
        raw_response_content = response['choices'][0]['text'].strip()
        
        # Parse and return the JSON response
        return json.loads(raw_response_content)

    except openai.OpenAIError as oe:
        logging.error(f"OpenAI error: {oe}")
        raise HTTPException(status_code=500, detail="Error interacting with OpenAI")

    except json.JSONDecodeError as je:
        logging.error(f"JSON decode error: {je}")
        raise HTTPException(status_code=500, detail="Error parsing JSON response from OpenAI")
