### FastAPI Setup

1. Run `pip install -r requirments.txt`
2. Run setup to create the configs: `python setup.py` -> make sure to populate them with the keys and url
3. Run the apis using the command: `uvicorn main:app --reload`
4. This will start running the apis at a link that is going to be in the terminal, but its usually `http://127.0.0.1:8000`
5. To see the docs for each endpoint, go to `http://127.0.0.1:8000/docs`

### Endpoints Info

Certainly! Here's a detailed documentation of the FastAPI routes provided, including descriptions of each endpoint, parameters, and examples of `curl` calls.

## API Endpoints

### 1. Get Cuisine Data

**Endpoint:** `/get_cuisine_data/{cuisine}`

**Method:** `GET`

**Description:** Retrieves cuisine data for a specific cuisine at a given location.

**Parameters:**

- `cuisine` (path parameter, `str`): The type of cuisine to search for.
- `latitude` (query parameter, `float`, optional): Latitude of the location. Default is `DEAFULT_LATITUDE`.
- `longitude` (query parameter, `float`, optional): Longitude of the location. Default is `DEFAULT_LONGITUDE`.

**Response:** JSON object containing cuisine data.

**Example Curl Call:**

```sh
curl -X GET "http://127.0.0.1:8000/get_cuisine_data/italian?latitude=40.7128&longitude=-74.0060"
```

### 2. Get Restaurant Dish Data

**Endpoint:** `/get_restaurant_dish_data/{restaurant_id}`

**Method:** `GET`

**Description:** Retrieves dish data for a specific restaurant.

**Parameters:**

- `restaurant_id` (path parameter, `str`): The ID of the restaurant.
- `offset` (query parameter, `float`, optional): Offset multiplier. Default is `0`.

**Response:** JSON object containing dish data for the restaurant.

**Example Curl Call:**

```sh
curl -X GET "http://127.0.0.1:8000/get_restaurant_dish_data/12345?offset=2"
```

### 3. Get Dish Data

**Endpoint:** `/get_dish_data/{dish_id}`

**Method:** `GET`

**Description:** Retrieves data for a specific dish.

**Parameters:**

- `dish_id` (path parameter, `str`): The ID of the dish.

**Response:** JSON object containing data for the dish.

**Example Curl Call:**

```sh
curl -X GET "http://127.0.0.1:8000/get_dish_data/67890"
```

### 4. Get Dish Base

**Endpoint:** `/get_dish_base/{neighborhoods}`

**Method:** `GET`

**Description:** Retrieves base dish data for a specific neighborhood.

**Parameters:**

- `neighborhoods` (path parameter, `str`): The neighborhoods to search within.

**Response:** JSON object containing base dish data for the neighborhoods.

**Example Curl Call:**

```sh
curl -X GET "http://127.0.0.1:8000/get_dish_base/chelsea"
```

### 5. Get Dish Combined

**Endpoint:** `/get_dish_combined/{neighborhoods}/{diets}/{cuisines}/{popular_dishes}`

**Method:** `GET`

**Description:** Retrieves combined dish data based on neighborhoods, diets, cuisines, and popular dishes.

**Parameters:**

- `neighborhoods` (path parameter, `str`): The neighborhoods to search within.
- `diets` (path parameter, `str`): The dietary preferences.
- `cuisines` (path parameter, `str`): The types of cuisines.
- `popular_dishes` (path parameter, `str`): The popular dishes to consider.

**Response:** JSON object containing combined dish data.

**Example Curl Call:**

```sh
curl -X GET "http://127.0.0.1:8000/get_dish_combined/chelsea/vegan/italian/pizza"
```

### 6. Get Dish Cuisine

**Endpoint:** `/get_dish_cusine/{neighborhoods}/{cuisines}`

**Method:** `GET`

**Description:** Retrieves dish data based on neighborhoods and cuisines.

**Parameters:**

- `neighborhoods` (path parameter, `str`): The neighborhoods to search within.
- `cuisines` (path parameter, `str`): The types of cuisines.

**Response:** JSON object containing dish data for the specified neighborhoods and cuisines.

**Example Curl Call:**

```sh
curl -X GET "http://127.0.0.1:8000/get_dish_cusine/chelsea/italian"
```

### 7. Get Dish Diets

**Endpoint:** `/get_dish_diets/{neighborhoods}/{diets}`

**Method:** `GET`

**Description:** Retrieves dish data based on neighborhoods and dietary preferences.

**Parameters:**

- `neighborhoods` (path parameter, `str`): The neighborhoods to search within.
- `diets` (path parameter, `str`): The dietary preferences.

**Response:** JSON object containing dish data for the specified neighborhoods and diets.

**Example Curl Call:**

```sh
curl -X GET "http://127.0.0.1:8000/get_dish_diets/chelsea/vegan"
```

### 8. Get Dish Popular

**Endpoint:** `/get_dish_popular/{neighborhoods}/{dishes}`

**Method:** `GET`

**Description:** Retrieves popular dish data based on neighborhoods and dishes.

**Parameters:**

- `neighborhoods` (path parameter, `str`): The neighborhoods to search within.
- `dishes` (path parameter, `str`): The popular dishes to consider.

**Response:** JSON object containing popular dish data for the specified neighborhoods and dishes.

**Example Curl Call:**

```sh
curl -X GET "http://127.0.0.1:8000/get_dish_popular/chelsea/pizza"
```

## Error Handling

Each endpoint may return the following errors:

- `404 Not Found`: Returned if no data is found for the given parameters.
  - Example response: `{"detail": "No data found for the given search term and location"}`

Make sure to replace `http://127.0.0.1:8000` with the actual base URL of your FastAPI application when making `curl` calls.