import re
import json

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
