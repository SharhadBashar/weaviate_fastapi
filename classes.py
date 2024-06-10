from typing import Union
from pydantic import BaseModel

class User(BaseModel):
    user_Id: int
    user_name: str
    name: str
    age: int
    gender: str
    height: int
    weight: int
    primary_health_goals: str
    flavor_preferences: str
    cuisine_preferences: str
    dietary_preferences: str
    total_budget: str
    meal_budget: str
    allergies_restrictions: str
    meal_frequency: str
    meal_types: str
    eating_time: str
    activity_level: str
    target_weight: int
    goal_timeline: str
    workout_days: str

class Dish(BaseModel):
    name: Union[str, None] = None
    description: Union[str, None] = None
    dish_Id: Union[str, None] = None
    user_Id: Union[str, None] = None
    user_name: Union[str, None] = None
