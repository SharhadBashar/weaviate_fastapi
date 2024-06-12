from typing import Union
from pydantic import BaseModel
from typing import List, Optional, Dict

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

class Dish_Details(BaseModel):
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

class DoorDash_Schedule(BaseModel):
    monday: Optional[str]
    tuesday: Optional[str]
    wednesday: Optional[str]
    thursday: Optional[str]
    friday: Optional[str]
    saturday: Optional[str]
    sunday: Optional[str]