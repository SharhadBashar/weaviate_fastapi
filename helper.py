import re
import json
from typing import *
from datetime import datetime
from geopy.distance import geodesic

def str_to_list(string):
    return string.split(',')

def read_json(file_name):
    with open(file_name) as file:
        return json.load(file)

def cleanse_json_string(json_str):
    """Clean up common JSON string issues to make it more likely to be parsed successfully."""

    # Remove control characters, except for tab, newline, and carriage return
    json_str = ''.join(ch for ch in json_str if ch >= ' ' or ch in ('\t', '\n', '\r'))

    # Remove trailing commas before closing braces/brackets
    json_str = re.sub(r',\s*([}\]])', r'\1', json_str)

    # Handle escape sequences - this might be dangerous if you're not sure about the input format
    json_str = json_str.replace('\\n', '\n').replace('\\t', '\t')

    # Additional corrections can be added here as needed...

    return json_str


def convert_json(json_str):
    """Convert JSON string to dict, attempting to fix common issues if needed."""

    json_str = cleanse_json_string(json_str)

    try:
        data = json.loads(json_str)
    except json.JSONDecodeError as e:
        # For debugging: print the error and a snippet around the problematic area
        start = max(e.pos - 20, 0)
        end = min(e.pos + 20, len(json_str))
        print(f'JSONDecodeError at position {e.pos}: ...{json_str[start: end]}...')
        raise

    return data


def save_json_to_file(data: dict, file_path: str):
    """
    Save a dictionary as a JSON file.

    Args:
    - data (dict): The dictionary to save.
    - file_path (str): The path where the JSON file should be saved.
    """
    with open(file_path, 'w', encoding = 'utf-8') as f:
        json.dump(data, f, ensure_ascii = False, indent = 4)


def is_valid_json(data):
    """Return True if the given string is a valid JSON. Otherwise, return False."""
    try:
        json.loads(data)
        return True
    except json.JSONDecodeError:
        return False

def calculate_distance(loc1: dict, loc2: dict) -> dict:
    loc1_coords = (loc1['latitude'], loc1['longitude'])
    loc2_coords = (loc2['latitude'], loc2['longitude'])
    distance_km = geodesic(loc1_coords, loc2_coords).kilometers
    distance_miles = geodesic(loc1_coords, loc2_coords).miles
    distance_label = f'{round(distance_miles * 100) / 100} miles'
    if (distance_miles < 0.2):
        distance_label = f'{round(distance_miles * 5280)} feet'
    return {'distance_miles': distance_miles, 'distance_km': distance_km, 'distance_label': distance_label}

def get_format_price(price: str) -> str:
    try:
        return f'{float(price):.2f}'
    except ValueError:
        return ''

def _default_client_latitude():
    return 40.7128

def _default_client_longitude():
    return -74.0060

def get_current_location():
    # Replace with actual implementation to get the current location
    return {'latitude': _default_client_latitude(), 'longitude': _default_client_longitude()}

def get_day_of_week(timestamp):
    return datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S').strftime('%a').lower()

def build_where_filter(text: str, neighborhoods: List[str], has_unique_image: bool) -> Dict:
    filter_clauses = [
        {
            'path': ['cleanedDishName'], 
            'operator': 'Like', 
            'valueText': f'*{text}*'
        }
    ]

    if neighborhoods:
        neighborhood_clauses = [
            {
                'path': ['neighborhood'], 
                'operator': 'Equal', 
                'valueString': neighborhood
            }
            for neighborhood in neighborhoods
        ]
        filter_clauses.append({'operator': 'Or', 'operands': neighborhood_clauses})

    if has_unique_image:
        filter_clauses.append(
            {
                'operator': 'Or',
                'operands': [
                    {
                        'path': ['stockImageUber'],
                        'operator': 'Equal',
                        'valueString': 'UniqueImage',
                    },
                    {
                        'path': ['stockImageDoorDash'],
                        'operator': 'Equal',
                        'valueString': 'UniqueImage',
                    },
                ],
            }
        )

    return {'operator': 'And', 'operands': filter_clauses}

def build_where_filter_dish(dish: str, neighborhoods: Optional[List[str]], has_unique_image: bool) -> Dict:
    filter_clauses = [
        {
            'path': ['cleanedDishName'], 
            'operator': 'Like', 
            'valueText': f'*{dish}*'
        }
    ]

    if neighborhoods:
        neighborhood_filters = [
            {
                'path': ['neighborhood'], 
                'operator': 'Equal', 
                'valueString': neighborhood
            }
            for neighborhood in neighborhoods
        ]
        filter_clauses.append(
            {
                'operator': 'Or',
                'operands': neighborhood_filters,
            }
        )

    if has_unique_image:
        filter_clauses.append(
            {
                'operator': 'Or',
                'operands': [
                    {
                        'path': ['stockImageUber'],
                        'operator': 'Equal',
                        'valueText': 'UniqueImage',
                    },
                    {
                        'path': ['stockImageDoorDash'],
                        'operator': 'Equal',
                        'valueText': 'UniqueImage',
                    },
                ],
            }
        )

    return {'operator': 'And', 'operands': filter_clauses}
