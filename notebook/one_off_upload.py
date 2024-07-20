from weaviate.classes.config import Property, DataType
from tqdm import tqdm
import json
import re
import logging
from pprint import pprint

# Configure logging
logging.basicConfig(level=logging.INFO)

def clean_key_name(key):
    """Clean the key names by replacing spaces and capital letters."""
    if key == "Dish":
        return "dish"
    elif key == "Cuisine":
        return "cuisine"
    elif key == "CountryOfOrigin":
        return "country_of_origin"
    elif key == "DietTags":
        return "diet_tags"
    elif key == "MasterKey":
        return "master_key"
    elif key == "ImageUrl":
        return "image_url"
    elif key == "KeyType":
        return "key_type"

def load_and_clean_data(file_path):
    """Load JSON data and clean key names."""
    with open(file_path, 'r') as f:
        data = json.load(f)
    cleaned_data = []
    for item in data:
        cleaned_item = {clean_key_name(k): v for k, v in item.items()}
        cleaned_data.append(cleaned_item)
    return cleaned_data

def create_schema(client):
    """Create the schema in Weaviate."""
    schema = {
        "class": "Static_Cusines",
        "properties": [
            {"name": "dish", "dataType": ["string"]},
            {"name": "cuisine", "dataType": ["string"]},
            {"name": "country_of_origin", "dataType": ["string"]},
            {"name": "diet_tags", "dataType": ["string"]},
            {"name": "master_key", "dataType": ["string"]},
            {"name": "image_url", "dataType": ["string"]},
            {"name": "key_type", "dataType": ["string"]}
        ]
    }
    client.schema.create({"classes": [schema]})

def upload_data_to_weaviate(client, class_name, data):
    """Upload data to Weaviate using batch operations."""
    with client.batch as batch:
        for item in tqdm(data):
            food_object = {k: str(v) for k, v in item.items()}
            logging.info(f"Uploading to {class_name}: {food_object}")
            batch.add_data_object(food_object, class_name)

# Setup Weaviate client
# auth_config = weaviate.AuthApiKey(api_key="AD88gas7nFZKgmR1Yr0d084yvhI5YVe3a2yZ")
# client = weaviate.Client(
#     url="https://pjokperctzqnvi34i1omg.c0.us-central1.gcp.weaviate.cloud",
#     auth_client_secret=auth_config
# )

# Create schema
# create_schema(client)

# Load and clean data
file_path = 'data_CategoriesJson_MergedCleanMaster.json'
cleaned_data = load_and_clean_data(file_path)
cusines = set()
for item in cleaned_data:
    cusines.add(item['cuisine'])

pprint(len(cusines))


# Upload data to Weaviate
# upload_data_to_weaviate(client, "Static_Cusines", cleaned_data)

# Check if data is uploaded
# result = client.query.get("Static_Cusines", ["dish"])
# print(result)