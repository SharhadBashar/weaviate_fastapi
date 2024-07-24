import uuid
from datetime import datetime

def prompt_menu(user):
    return f"""Generate a 7-day meal plan with 3 options per meal for the following user profile: Only generate dishes that are relativley common for restaurants to carry
        Name: {user.name}
        Age: {user.age}
        Gender: {user.gender}
        Height: {user.height} cm
        Weight: {user.weight} kg
        Primary Health Goals: {user.primary_health_goals}
        Flavor Preferences: {user.flavor_preferences}
        Cuisine Preferences: {user.cuisine_preferences}
        Dietary Preferences: {user.dietary_preferences}
        Total Budget: {user.total_budget}
        Budget Per Meal: {user.meal_budget}
        Allergies and Restrictions: {user.allergies_restrictions}
        Meal Frequency: {user.meal_frequency}
        Meal Types: {user.meal_types}
        Preferred Eating Times: {user.eating_time}
        Activity Level: {user.activity_level}
        Target Weight: {user.target_weight} kg
        Timeline for Goals: {user.goal_timeline}
        Preferred Workout Days: {user.workout_days}

        Provide the meal plan in the following JSON format:
        {{
            'meal_Id': '{str(uuid.uuid4())}',
            'user_Id': '{user.user_Id}',
            'user_name': '{user.user_name}',
            'date': '{datetime.now().strftime('%Y-%m-%d %H:%M')}',
      
            {{
                'meal_plan': [
                    {{
                        'day': 1,
                        'meals': {{
                            'breakfast': [
                                'Avocado Toast',
                                'Greek Yogurt with Honey and Berries',
                                'Smoothie Bowl'
                            ],
                            'lunch': [
                                'Quinoa Salad',
                                'Veggie Wrap',
                                'Falafel Salad'
                            ],
                            'dinner': [
                                'Vegetarian Sushi',
                                'Vegetarian Stir-fry',
                                'Vegetarian Pad Thai'
                            ]
                        }}
                    }},
                    {{
                        'day': 2,
                        'meals': {{
                            'breakfast': [
                                'Chia Seed Pudding',
                                'Overnight Oats',
                                'Smoothie with Spinach, Banana, and Almond Milk'
                            ],
                            'lunch': [
                                'Hummus Plate',
                                'Grilled Vegetable Panini',
                                'Caprese Sandwich'
                            ],
                            'dinner': [
                                'Vegetarian Pizza',
                                'Vegetarian Curry',
                                'Vegetarian Tacos'
                            ]
                        }}
                    }},
                    {{
                        'day': 3,
                        'meals': {{
                            'breakfast': [
                                'Acai Bowl',
                                'Banana Bread',
                                'Protein Smoothie'
                            ],
                            'lunch': [
                                'Lentil Soup',
                                'Stuffed Peppers',
                                'Chickpea Salad'
                            ],
                            'dinner': [
                                'Vegetarian Samosas',
                                'Vegetarian Burrito',
                                'Vegetarian Pasta'
                            ]
                        }}
                    }},
                    {{
                        'day': 4,
                        'meals': {{
                            'breakfast': [
                                'Fruit Parfait',
                                'Almond Butter Toast',
                                'Bagel with Cream Cheese'
                            ],
                            'lunch': [
                                'Vegetarian Wrap',
                                'Tomato Basil Soup',
                                'Grilled Cheese Sandwich'
                            ],
                            'dinner': [
                                'Vegetarian Sushi',
                                'Vegetarian Stir-fry',
                                'Vegetarian Tacos'
                            ]
                        }}
                    }},
                    {{
                        'day': 5,
                        'meals': {{
                            'breakfast': [
                                'Smoothie Bowl',
                                'Greek Yogurt with Honey and Berries',
                                'Overnight Oats'
                            ],
                            'lunch': [
                                'Veggie Wrap',
                                'Quinoa Salad',
                                'Falafel Salad'
                            ],
                            'dinner': [
                                'Vegetarian Pad Thai',
                                'Vegetarian Pizza',
                                'Vegetarian Burrito'
                            ]
                        }}
                    }},
                    {{
                        'day': 6,
                        'meals': {{
                            'breakfast': [
                                'Chia Seed Pudding',
                                'Acai Bowl',
                                'Protein Smoothie'
                            ],
                            'lunch': [
                                'Grilled Vegetable Panini',
                                'Hummus Plate',
                                'Caprese Sandwich'
                            ],
                            'dinner': [
                                'Vegetarian Curry',
                                'Vegetarian Tacos',
                                'Vegetarian Pasta'
                            ]
                        }}
                    }},
                    {{
                        'day': 7,
                        'meals': {{
                            'breakfast': [
                                'Avocado Toast',
                                'Greek Yogurt with Honey and Berries',
                                'Smoothie Bowl'
                            ],
                            'lunch': [
                                'Quinoa Salad',
                                'Veggie Wrap',
                                'Falafel Salad'
                            ],
                            'dinner': [
                                'Vegetarian Sushi',
                                'Vegetarian Stir-fry',
                                'Vegetarian Pad Thai'
                            ]
                        }}
                    }}
                ]
            }} 
        }}
    """

def prompt_nutrition_info(dish):
    return f"""You are an expert nutritionist. Analyze the following information to provide a detailed nutritional breakdown for the dish.
        Name: {dish.get('name', '')}
        Description: {dish.get('description', '')}

        Include the calories, macronutrients (protein, fat, carbs including fiber and sugars), and micronutrients (vitamins and minerals).
        Also provide confidence bounds for calories and macronutrients for "Strict Mode" (overestimate) and "Lazy Mode" (underestimate). Return the information in the following JSON format:
        {{
            "dish_info": {{
                "name": "{dish.get('name', '')}",
                "description": "{dish.get('description', '')}",
                "dish_Id": "{dish.get('dish_Id', '')}"
                "Nutrition_Id": "{str(uuid.uuid4())}",
                "user_Id": "{dish['user_Id']}",
                "user_name": "{dish['user_name']}",
                "date": "{datetime.now().strftime('%Y-%m-%d %H:%M')}
            }},
            "serving_size": "grams",
            "nutrition": {{
                "calories": {{
                "amount": [amount],
                "unit": "kcal",
                "strict_mode": [lower_bound],
                "lazy_mode": [upper_bound]
                }},
                "macronutrients": {{
                "protein": {{
                    "amount": [amount],
                    "unit": "grams",
                    "strict_mode": [lower_bound],
                    "lazy_mode": [upper_bound]
                }},
                "fat": {{
                    "amount": [amount],
                    "unit": "grams",
                    "strict_mode": [lower_bound],
                    "lazy_mode": [upper_bound]
                }},
                "carbohydrates": {{
                    "amount": [amount],
                    "unit": "grams",
                    "strict_mode": [lower_bound],
                    "lazy_mode": [upper_bound]
                }},
                "fiber": {{
                    "amount": [amount],
                    "unit": "grams"
                }},
                "sugars": {{
                    "amount": [amount],
                    "unit": "grams"
                }},
                "net_carbs": {{
                    "amount": [amount],
                    "unit": "grams"
                }}
                }},
                "micronutrients": {{
                "vitamins": {{
                    "vitamin_a": {{
                    "amount": [amount],
                    "unit": "IU"
                    }},
                    "vitamin_c": {{
                    "amount": [amount],
                    "unit": "milligrams"
                    }},
                    "vitamin_d": {{
                    "amount": [amount],
                    "unit": "micrograms"
                    }},
                    "vitamin_e": {{
                    "amount": [amount],
                    "unit": "milligrams"
                    }},
                    "vitamin_k": {{
                    "amount": [amount],
                    "unit": "micrograms"
                    }},
                    "thiamin": {{
                    "amount": [amount],
                    "unit": "milligrams"
                    }},
                    "riboflavin": {{
                    "amount": [amount],
                    "unit": "milligrams"
                    }},
                    "niacin": {{
                    "amount": [amount],
                    "unit": "milligrams"
                    }},
                    "vitamin_b6": {{
                    "amount": [amount],
                    "unit": "milligrams"
                    }},
                    "folate": {{
                    "amount": [amount],
                    "unit": "micrograms"
                    }},
                    "vitamin_b12": {{
                    "amount": [amount],
                    "unit": "micrograms"
                    }},
                    "pantothenic_acid": {{
                    "amount": [amount],
                    "unit": "milligrams"
                    }}
                }},
                "minerals": {{
                    "calcium": {{
                    "amount": [amount],
                    "unit": "milligrams"
                    }},
                    "iron": {{
                    "amount": [amount],
                    "unit": "milligrams"
                    }},
                    "magnesium": {{
                    "amount": [amount],
                    "unit": "milligrams"
                    }},
                    "phosphorus": {{
                    "amount": [amount],
                    "unit": "milligrams"
                    }},
                    "potassium": {{
                    "amount": [amount],
                    "unit": "milligrams"
                    }},
                    "sodium": {{
                    "amount": [amount],
                    "unit": "milligrams"
                    }},
                    "zinc": {{
                    "amount": [amount],
                    "unit": "milligrams"
                    }},
                    "copper": {{
                    "amount": [amount],
                    "unit": "milligrams"
                    }},
                    "manganese": {{
                    "amount": [amount],
                    "unit": "milligrams"
                    }},
                    "selenium": {{
                    "amount": [amount],
                    "unit": "micrograms"
                    }}
                }}
                }}
            }}
        }}
    """
