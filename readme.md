### FastAPI

1. first run `pip install -r requirments.txt`
2. then run setup to create the configs: `python setup.py` -> make sure to populate them with the keys and url
3. run the apis using the command: `uvicorn main:app --reload`
4. this will start running the apis at a link that is going to be in the terminal, but its usually `http://127.0.0.1:8000`
5. to see the docs for each endpoint, go to `http://127.0.0.1:8000/docs`

### Endpoints Info

The provided FastAPI code defines several endpoint functions that interact with a backend service (weaviate) to retrieve data based on various criteria. Here’s a detailed explanation of each endpoint and its parameters:

Endpoint 1: /get_cuisine_data/{cusine}
Purpose: Retrieves cuisine-related data based on a specified cuisine.
Parameters:
cusine: Path parameter (str) representing the cuisine type.
latitude: Optional query parameter (float) representing the latitude of the location (default value provided).
longitude: Optional query parameter (float) representing the longitude of the location (default value provided).
Functionality:
Calls weaviate.get_cuisine_data(cusine, latitude, longitude) to fetch cuisine data.
Raises a 404 HTTPException if no data is found for the specified cuisine and location.


Endpoint 2: /get_restaurant_dish_data/{restaurant_id}
Purpose: Retrieves dish data from a specific restaurant.
Parameters:
restaurant_id: Path parameter (str) representing the restaurant ID.
offset: Optional query parameter (float) indicating the offset multiplier (default value is 0).
Functionality:
Calls weaviate.get_restaurant_dish_data(restaurant_id, offset) to fetch dish data for the restaurant.
Raises a 404 HTTPException if no data is found for the given restaurant ID.


Endpoint 3: /get_dish_data/{dish_id}
Purpose: Retrieves data for a specific dish.
Parameters:
dish_id: Path parameter (str) representing the dish ID.
Functionality:
Calls weaviate.get_dish_data(dish_id) to fetch data for the specified dish.
Raises a 404 HTTPException if no data is found for the given dish ID.


Endpoint 4: /get_dish_base/{neighborhoods}
Purpose: Retrieves dish data based on specified neighborhoods.
Parameters:
neighborhoods: Path parameter (str) containing names of neighborhoods.
Functionality:
Calls weaviate.get_dish_base(neighborhoods) to fetch dish data based on neighborhoods.
Raises a 404 HTTPException if no data is found for the given neighborhoods.


Endpoint 5: /get_dish_combined/{neighborhoods}/{diets}/{cuisines}/{popular_dishes}
Purpose: Retrieves dish data based on combined criteria.
Parameters:
neighborhoods: Path parameter (str) containing names of neighborhoods.
diets: Path parameter (str) containing dietary preferences.
cuisines: Path parameter (str) containing cuisine types.
popular_dishes: Path parameter (str) containing popular dish names.
Functionality:
Calls weaviate.get_dish_combined(neighborhoods, diets, cuisines, popular_dishes) to fetch dish data based on combined criteria.
Raises a 404 HTTPException if no data is found for the given combined criteria.


Endpoint 6: /get_dish_cusine/{neighborhoods}/{cuisines}
Purpose: Retrieves dish data based on neighborhoods and cuisine types.
Parameters:
neighborhoods: Path parameter (str) containing names of neighborhoods.
cuisines: Path parameter (str) containing cuisine types.
Functionality:
Calls weaviate.get_dish_cusine(neighborhoods, cuisines) to fetch dish data based on neighborhoods and cuisine types.
Raises a 404 HTTPException if no data is found for the given neighborhoods and cuisines.


Endpoint 7: /get_dish_diets/{neighborhoods}/{diets}
Purpose: Retrieves dish data based on neighborhoods and dietary preferences.
Parameters:
neighborhoods: Path parameter (str) containing names of neighborhoods.
diets: Path parameter (str) containing dietary preferences.
Functionality:
Calls weaviate.get_dish_diets(neighborhoods, diets) to fetch dish data based on neighborhoods and dietary preferences.
Raises a 404 HTTPException if no data is found for the given neighborhoods and diets.


Endpoint 8: /get_dish_popular/{neighborhoods}/{dishes}
Purpose: Retrieves dish data based on neighborhoods and popular dish names.
Parameters:
neighborhoods: Path parameter (str) containing names of neighborhoods.
dishes: Path parameter (str) containing popular dish names.
Functionality:
Calls weaviate.get_dish_popular(neighborhoods, dishes) to fetch dish data based on neighborhoods and popular dish names.
Raises a 404 HTTPException if no data is found for the given neighborhoods and dishes.


## Documentation Notes:
Each endpoint performs data retrieval based on specific criteria and handles potential errors by raising appropriate HTTP exceptions (404).
Path parameters are used to specify main identifiers (cusine, restaurant_id, dish_id, neighborhoods, diets, cuisines, popular_dishes).
Optional query parameters (latitude, longitude, offset) provide additional filtering or pagination options.
Ensure that weaviate functions (get_cuisine_data, get_restaurant_dish_data, etc.) are correctly implemented to handle the respective data retrieval logic.
This documentation should help in understanding how each endpoint operates and how to interact with them using FastAPI. Adjustments may be needed based on specific requirements or the implementation details of weaviate

### Curl Calls:
To make `curl` calls for the provided FastAPI endpoints, you need to structure the URL and optionally include query parameters. Here's how you can do it for each endpoint:

1. **`/get_cuisine_data/{cuisine}`**

   ```sh
   curl -X GET "http://http://127.0.0.1:8000/get_cuisine_data/{cuisine}?latitude={latitude}&longitude={longitude}"
   ```

   Replace `{cuisine}`, `{latitude}`, and `{longitude}` with the actual values. `latitude` and `longitude` are optional.

   Example:

   ```sh
   curl -X GET "http://http://127.0.0.1:8000/get_cuisine_data/italian?latitude=40.7128&longitude=-74.0060"
   ```

2. **`/get_restaurant_dish_data/{restaurant_id}`**

   ```sh
   curl -X GET "http://http://127.0.0.1:8000/get_restaurant_dish_data/{restaurant_id}?offset={offset}"
   ```

   Replace `{restaurant_id}` and `{offset}` with the actual values. `offset` is optional.

   Example:

   ```sh
   curl -X GET "http://http://127.0.0.1:8000/get_restaurant_dish_data/12345?offset=2"
   ```

3. **`/get_dish_data/{dish_id}`**

   ```sh
   curl -X GET "http://http://127.0.0.1:8000/get_dish_data/{dish_id}"
   ```

   Replace `{dish_id}` with the actual value.

   Example:

   ```sh
   curl -X GET "http://http://127.0.0.1:8000/get_dish_data/67890"
   ```

4. **`/get_dish_base/{neighborhoods}`**

   ```sh
   curl -X GET "http://http://127.0.0.1:8000/get_dish_base/{neighborhoods}"
   ```

   Replace `{neighborhoods}` with the actual value.

   Example:

   ```sh
   curl -X GET "http://http://127.0.0.1:8000/get_dish_base/chelsea"
   ```

5. **`/get_dish_combined/{neighborhoods}/{diets}/{cuisines}/{popular_dishes}`**

   ```sh
   curl -X GET "http://http://127.0.0.1:8000/get_dish_combined/{neighborhoods}/{diets}/{cuisines}/{popular_dishes}"
   ```

   Replace `{neighborhoods}`, `{diets}`, `{cuisines}`, and `{popular_dishes}` with the actual values.

   Example:

   ```sh
   curl -X GET "http://http://127.0.0.1:8000/get_dish_combined/chelsea/vegan/italian/pizza"
   ```

6. **`/get_dish_cusine/{neighborhoods}/{cuisines}`**

   ```sh
   curl -X GET "http://http://127.0.0.1:8000/get_dish_cusine/{neighborhoods}/{cuisines}"
   ```

   Replace `{neighborhoods}` and `{cuisines}` with the actual values.

   Example:

   ```sh
   curl -X GET "http://http://127.0.0.1:8000/get_dish_cusine/chelsea/italian"
   ```

7. **`/get_dish_diets/{neighborhoods}/{diets}`**

   ```sh
   curl -X GET "http://http://127.0.0.1:8000/get_dish_diets/{neighborhoods}/{diets}"
   ```

   Replace `{neighborhoods}` and `{diets}` with the actual values.

   Example:

   ```sh
   curl -X GET "http://http://127.0.0.1:8000/get_dish_diets/chelsea/vegan"
   ```

8. **`/get_dish_popular/{neighborhoods}/{dishes}`**

   ```sh
   curl -X GET "http://http://127.0.0.1:8000/get_dish_popular/{neighborhoods}/{dishes}"
   ```

   Replace `{neighborhoods}` and `{dishes}` with the actual values.

   Example:

   ```sh
   curl -X GET "http://http://127.0.0.1:8000/get_dish_popular/chelsea/pizza"
   ```

Make sure to replace `http://http://127.0.0.1:8000` with the actual base URL of your FastAPI application.