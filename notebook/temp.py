import os
import weaviate
from fastapi import FastAPI, Query, HTTPException
from typing import List, Dict, Optional
import uvicorn
from dotenv import load_dotenv
from constants import *
import random
from pprint import pprint

load_dotenv()  # Load environment variables from .env file

app = FastAPI()

# Constants



# Predefined arrays for diets, cuisines, and popular dishes
CURATED_DIETS = {
    "vegan": ["Vegan Burger", "Tofu Stir-Fry", "Vegan Sushi"],
    "keto": ["Beef Stir-Fry with Mixed Vegetables", "Chicken Lettuce Wrap", "Butter Filet"],
}

CURATED_CUISINES = {
    "italian": ["Pizza", "Pasta", "Lasagna"],
    "chinese": ["Dim Sum", "Sweet and Sour Pork", "Kung Pao Chicken"],
}

CURATED_DISHES = {
    "desserts": ["Chocolate Cake", "Ice Cream", "Cupcakes"],
    "breakfasts": ["Pancakes", "Omelette", "French Toast"],
}


# Function to initialize Weaviate client
def initialize_weaviate_client():
    openai_key = os.getenv("OPENAI_KEY", "your_openai_key")
    weaviate_key = os.getenv("WEAVIATE_KEY", "your_weaviate_key")
    weaviate_url = os.getenv("WEAVIATE_URL", "your_weaviate_url")

    auth_config = weaviate.AuthApiKey(api_key=weaviate_key)

    # Setting up client
    client = weaviate.Client(
        url=weaviate_url,
        auth_client_secret=auth_config,
        additional_headers={
            "X-OpenAI-Api-Key": openai_key,  # Replace with your OpenAI key
        },
    )

    return client


def build_where_filter_dish(
    dish: str, neighborhoods: Optional[List[str]], has_unique_image: bool
) -> Dict:
    filter_clauses = [
        {"path": ["cleanedDishName"], "operator": "Like", "valueText": f"*{dish}*"}
    ]

    if neighborhoods:
        neighborhood_filters = [
            {"path": ["neighborhood"], "operator": "Equal", "valueString": neighborhood}
            for neighborhood in neighborhoods
        ]
        filter_clauses.append(
            {
                "operator": "Or",
                "operands": neighborhood_filters,
            }
        )

    if has_unique_image:
        filter_clauses.append(
            {
                "operator": "Or",
                "operands": [
                    {
                        "path": ["stockImageUber"],
                        "operator": "Equal",
                        "valueText": "UniqueImage",
                    },
                    {
                        "path": ["stockImageDoorDash"],
                        "operator": "Equal",
                        "valueText": "UniqueImage",
                    },
                ],
            }
        )

    return {"operator": "And", "operands": filter_clauses}


def get_dish_data_elastic(
    client, search_term: str, limit: int, where_filter: Dict
) -> List[Dict]:
    try:
        response = (
            client.query.get(CRISPY_V1, RETURN_PROPERTIES_V2)
            .with_additional(["id", "distance"])
            .with_where(where_filter)
            .with_limit(limit)
            .do()
        )

        return response["data"]["Get"][CRISPY_V1]
    except Exception as err:
        print(err)
        return []


def get_dish_data_vector(
    client, search_term: str, limit: int, where_filter: Dict
) -> List[Dict]:
    try:
        response = (
            client.query.get(CRISPY_V1, RETURN_PROPERTIES_V2)
            .with_near_text({"concepts": [search_term]})
            .with_additional(["id", "distance"])
            .with_where(where_filter)
            .with_limit(limit)
            .do()
        )
        return response["data"]["Get"][CRISPY_V1]
    except Exception as err:
        print(err)
        return []


def get_dish_data_standard(
    client_v3,
    search_term: str,
    latitude=DEFAULT_LATITUDE,
    longitude=DEFAULT_LONGITUDE,
    offset=0,
    neighborhoods: List[str] = None,
    has_unique_image: bool = False,
    limit: int = 10,  # Default number of results per dish
) -> List[Dict]:
    if not search_term:
        return []

    where_filter = build_where_filter_dish(search_term, neighborhoods, has_unique_image)
    pprint(where_filter)
    elastic_resp = get_dish_data_elastic(client_v3, search_term, limit, where_filter)

    vector_resp = get_dish_data_vector(client_v3, search_term, limit, where_filter)
    print(elastic_resp)
    print()
    print(vector_resp)
    unique_dish_res_ids = set()

    unique_dishes = []

    def add_unique_dishes(dishes):
        for dish in dishes:
            if dish["dishRes_ID"] not in unique_dish_res_ids:
                unique_dish_res_ids.add(dish["dishRes_ID"])
                unique_dishes.append(dish)

    if len(elastic_resp) <= 8:
        add_unique_dishes(vector_resp)
        add_unique_dishes(elastic_resp)
    else:
        half_length = len(vector_resp) // 2
        half_vector_response = vector_resp[:half_length]
        add_unique_dishes(elastic_resp)
        add_unique_dishes(half_vector_response)

    return unique_dishes

def combine_alternatives(dishes: List[Dict], max_alternatives: int) -> List[str]:
    alternatives = []
    count = 0
    for dish in dishes:
        if count >= max_alternatives:
            break
        for key in [
            "specificBaseAlternatives",
            "alternativesWithinSameCuisine",
            "healthAlternatives",
        ]:
            if key in dish and dish[key] and dish[key] != "None":
                alternatives.extend(dish[key].strip("[]").replace("'", "").split(", "))
                count += len(dish[key].strip("[]").replace("'", "").split(", "))
        if count >= max_alternatives:
            break
    return list(set(alternatives[:max_alternatives]))


def get_alternative_dish_data(
    client_v3,
    alternatives: List[str],
    latitude=DEFAULT_LATITUDE,
    longitude=DEFAULT_LONGITUDE,
    offset=0,
    neighborhoods: List[str] = None,
    has_unique_image: bool = False,
    limit: int = 10,  # Default number of results per alternative dish
) -> List[Dict]:
    alternative_data = []
    for alt in alternatives:
        where_filter = build_where_filter_dish(alt, neighborhoods, has_unique_image)
        data = get_dish_data_standard(client_v3, alt, limit, where_filter)
        alternative_data.extend(data)
    return alternative_data


def get_diet_dishes(
    client,
    dishes: List[str],
    latitude=DEFAULT_LATITUDE,
    longitude=DEFAULT_LONGITUDE,
    offset=0,
    neighborhoods: List[str] = None,
    has_unique_image: bool = False,
    limit: int = 10,  # Default number of results per dish
    max_alternatives: int = 9,  # Default number of alternatives
    num_dishes: int = 10,  # Number of dishes to select
) -> Dict:
    combined_results = {}
    for dish in random.sample(dishes, min(num_dishes, len(dishes))):
        dish_results = get_dish_data_standard(
            client,
            dish,
            latitude,
            longitude,
            offset,
            neighborhoods,
            has_unique_image,
            limit,
        )
        # alternatives = combine_alternatives(dish_results, max_alternatives)
        # alternative_data = get_alternative_dish_data(
        #     client,
        #     alternatives,
        #     latitude,
        #     longitude,
        #     offset,
        #     neighborhoods,
        #     has_unique_image,
        #     limit,
        # )
        # combined_results[dish] = dish_results + alternative_data
    return dish_results


@app.get("/get_search_dishes")
def search_categories_for_dishes(
    query_type: str,
    query_value: str,
    neighborhoods: Optional[List[str]] = Query(None),
    has_unique_image: bool = Query(False),
    limit: int = Query(10),
    max_alternatives: int = Query(9),
    num_dishes: int = Query(10),
):
    client_v3 = initialize_weaviate_client()

    if query_type == "cuisine":
        dishes = CURATED_CUISINES.get(query_value.lower(), [])
    elif query_type == "diet":
        dishes = CURATED_DIETS.get(query_value.lower(), [])
    elif query_type == "popular":
        dishes = CURATED_DISHES.get(query_value.lower(), [])
    else:
        raise HTTPException(status_code=400, detail="Invalid query type")

    if not dishes:
        raise HTTPException(
            status_code=404, detail="No dishes found for the given query value"
        )

    results = get_diet_dishes(
        client_v3,
        dishes,
        neighborhoods=neighborhoods,
        has_unique_image=has_unique_image,
        limit=limit,
        max_alternatives=max_alternatives,
        num_dishes=num_dishes,
    )
    return results


# Run the server
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)