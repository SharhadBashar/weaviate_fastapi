import os

WEAVIATE_LIMIT_1 = 1
WEAVIATE_LIMIT_50 = 50
WEAVIATE_LIMIT_100 = 100
WEAVIATE_LIMIT_200 = 200
WEAVIATE_LIMIT_1000 = 1000
DEFAULT_LATITUDE = 40.720800
DEFAULT_LONGITUDE = -73.978940

DISTANCE_MILES = {
    1: 1609.34
}

DISTANCE_KM = {
    1: 1000
}

MAX_TOKENS = 4096
TEMPERATURE = 0.7
CLOSEST_NEIGHBOURHOOD_K = 3
RESPONSE_JSON = {'type': 'json_object'}

MODEL = {
    'gpt_4o': {'name': 'gpt-4o'},
    'gpt_4': {'name': 'gpt-4'},
    'gpt_35': {'name': 'gpt-3.5'}
}

SYSTEM = 'system'
USER = 'user'

SYSTEM_MESSAGE_GEN_MENU = 'You are a harvard educated AI nutritionist that provides single item meals that can be ordered through Uber Eats and Doordash. Respond only with valid JSON.'
SYSTEM_MESSAGE_GEN_NUTRITION_INFO = 'You are an expert nutritionist from Harvard that knows the exact nutrition in every take out dish based on FDA daily reccomendated standards. Respond only with valid JSON.'

PATH_CONFIG = './config/'
PATH_QUERY = './query/'
PATH_DB_CONFIG_CK = 'cockroach.json'
PATH_OPEN_AI_CONFIG = 'open_ai.json'
PATH_WEAVIATE_CONFIG = 'weaviate.json'
CURATED_CUISINES_FILE = os.path.join(PATH_QUERY, 'cuisines.json')
CURATED_DIETS_FILE = os.path.join(PATH_QUERY, 'diets.json')
CURATED_DISHES_FILE = os.path.join(PATH_QUERY, 'dishes.json')

CRISPY_V1 = 'Crispy_v1_search_nyc'
GEO_PROPERTY = 'geoCoordinates'
RETURN_PROPERTIES_HOURS = [
    'closeTime_UberEats_uber',
    'daysOpen_UberEats_uber',
    'friDoorDash',
    'linkDoorDash',
    'linkUber',
    'monDoorDash',
    'openCloseHours',
    'openingHours_UberEats_uber',
    'restaurantAddress',
    'restaurantName',
    'restaurantPhone',
    'satDoorDash',
    'sunDoorDash',
    'thuDoorDash',
    'tueDoorDash',
    'wedDoorDash',
]
RETURN_PROPERTIES = [
    #IDs
    'dishRes_ID',
    'dish_ID',
    'restaurant_ID',
    '_additional { id }'
    'geoCoordinates {latitude longitude}',

    # Dish data
    'dishName',
    'calorie_Count_Estimate',
    'cleanedDishName',
    'dietTags',
    'foodItemLinkUber',
    'foodItemLinkDoorDash',
    'foodItemUberCartLinks',
    'healthAlternatives',
    'mass_Carbs',
    'mass_Fat',
    'mass_Protein',
    'imageDoorDash',
    'imageUber',
    'linkUber',
    'linkDoorDash',
    'priceClean',

    # Restaurant data
    'closeTime_UberEats_uber',
    'daysOpen_UberEats_uber',
    'monDoorDash',
    'tueDoorDash',
    'wedDoorDash',
    'thuDoorDash',
    'friDoorDash',
    'satDoorDash',
    'sunDoorDash',
    'lat',
    'long',
    'neighborhood',
    'openCloseHours',
    'openingHours_UberEats_uber',
    'restaurantName',
    'restaurantPhone',
    'restaurantRating',
    'restaurantReviewCount',
    'stockImageDoorDash',
    'stockImageUber',
    # Review data
    'eater_ReviewDictVec',
    'infatuation_ReviewDictVec',
  ]
RETURN_PROPERTIES_ALL = [
    'dishRes_ID',
    'dish_ID',
    'restaurant_ID',
    '_additional { id }',
    'geoCoordinates { latitude longitude }',

    'dishName',
    'calorie_Count_Estimate',
    'cleanedDishName',
    'dietTags',
    'foodItemLinkUber',
    'foodItemLinkDoorDash',
    'foodItemUberCartLinks',
    'healthAlternatives',
    'specificBaseAlternatives',
    'alternativesWithinSameCuisine',
    'mass_Carbs',
    'mass_Fat',
    'mass_Protein',
    'imageDoorDash',
    'stockImageUber',
    'stockImageDoorDash',
    'imageUber',
    'linkUber',
    'linkDoorDash',
    'priceClean',

    'reviewCountCategory',
    'priceDescription',
    "texture_Tender",
    "texture_Juicy",
    "texture_Moist",
    "texture_Succulent",
    "texture_Soft",
    "texture_Crispy",
    "texture_Crunchy",
    "texture_Golden",

    "good_for_MuscleBuilding",

    "sodium",
    "fiber",
    "sugars",
    "cholesterol",
    "calcium",
    "iron",
    "potassium",
    "zinc",
    "magnesium",
    "vitamin_A",
    "vitamin_C",
    "vitamin_D",
    "vitamin_E",
    "vitamin_K",
    "b_Vitamins",
    "antioxidants",
    "omega_3_Fatty_Acids",
    "phytonutrients",
    'oil_Tags',
    "oil_NoOil",
    "oil_OliveOil",
    "oil_VegetableOil",
    "oil_CanolaOil",
    "oil_Butter",
    "oil_SesameOil",
    "oil_Ghee",
    "oil_CoconutOil",
    "oil_Mayonnaise",
    "oil_PeanutOil",
    "oil_PalmOil",
    "oil_SunflowerOil",
    "oil_CornOil",
    "oil_SoybeanOil",
    "oil_TruffleOil",
    "oil_AvocadoOil",
    "oil_AnimalFat",
    "oil_SeedOil",
    "oil_MiscellaneousOils",
    "oil_VariousUnknownOils",
    "feeling_Tags",
    "spice_Level",
    "sweetness_Level",
    "bitterness_Level",
    "sour_Level",
    "umami_Level",
    'emoji',
    'eater_ReviewDictVec',
    'infatuation_ReviewDictVec',
    'allergy_Dairy',
    'allergy_Eggs',
    'allergy_Fish',
    'allergy_Shellfish',
    'allergy_TreeNuts',
    'allergy_Peanuts',
    'allergy_Wheat',
    'allergy_Soy',
    'allergy_Sesame',
    'allergy_Mustard',
    'allergy_Corn',
    'allergy_Mushrooms',
    'allergy_Pork',

    'closeTime_UberEats_uber',
    'daysOpen_UberEats_uber',
    'monDoorDash',
    'tueDoorDash',
    'wedDoorDash',
    'thuDoorDash',
    'friDoorDash',
    'satDoorDash',
    'sunDoorDash',
    'lat',
    'long',
    'neighborhood',
    'openCloseHours',
    'openingHours_UberEats_uber',
    'restaurantName',
    'restaurantPhone',
    'restaurantRating',
    'restaurantReviewCount',
    "newCuisine",
    "dietTags",
    'infatuation_ReviewDictVec',
  ]
RETURN_PROPERTIES_V2 = [
    'cleanedDishName',
    'dietTags',
    'dishName',
    'dishRes_ID',
    'dish_ID',
    'dishDescription',
    'foodHistory',
    'eater_ReviewDictVec',
    'foodItemLinkDoorDash',
    'foodItemLinkUber',
    'foodItemUberCartLinks',
    'healthAlternatives',
    'imageDoorDash',
    'imageUber',
    'infatuation_ReviewDictVec',
    'lat',
    'linkDoorDash',
    'linkUber',
    'long',
    'neighborhood',
    'priceClean',
    'restaurantName',
    'restaurant_ID' 
]
RETURN_PROPERTIES_V3 = [
  'dish_ID',
  '_additional { id }',
  'alternativesWithinSameCuisine',
  'avoidanceDiseaseFoodVec',
  'calorie_Count_Estimate',
  'category_Carbs',
  'category_Fat',
  'category_Protein',
  'cleanedDishName',
  'closeTime_UberEats_uber',
  'daysOpen_UberEats_uber',
  'diet_Carnivore',
  'diet_Halal',
  'diet_Keto',
  'diet_Kosher',
  'diet_Mediterranean',
  'diet_Omnivore',
  'diet_Paleo',
  'diet_Pescatarian',
  'diet_Vegan',
  'diet_Vegetarian',
  'dishDescription',
  'dishName',
  'eater_ReviewDictVec',
  'foodHistory',
  'foodItemUberCartLinks',
  'foodItemLinkDoorDash',
  'foodItemLinkUber',
  'imageDoorDash',
  'imageUber',
  'infatuation_ReviewDictVec',
  'healthAlternatives',
  'lat',
  'linkDoorDash',
  'linkUber',
  'long',
  'normalizedIngredients',
  'mass_Carbs',
  'mass_Fat',
  'mass_Protein',
  'neighborhood',
  'priceClean',
  'priceDoorDash',
  'priceUber',
  'restaurantName',
  'restaurantPhone',
  'restaurantWebsite',
  'restaurant_ID',
  'specificBaseAlternatives',
  'monDoorDash',
  'tueDoorDash',
  'wedDoorDash',
  'thuDoorDash',
  'friDoorDash',
  'satDoorDash',
  'sunDoorDash',
  'stockImageDoorDash',
  'stockImageUber',
  'dietTags',
  'newCuisine',
  'dishType'
]
