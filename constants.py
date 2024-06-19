WEAVIATE_LIMIT_50 = 50
WEAVIATE_LIMIT_200 = 200
DEAFULT_LATITUDE = 40.720800
DEFAULT_LONGITUDE = -73.978940

MAX_TOKENS = 4096
TEMPERATURE = 0.7
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
PATH_DB_CONFIG_CK = 'cockroach.json'
PATH_OPEN_AI_CONFIG = 'open_ai.json'
PATH_WEAVIATE_CONFIG = 'weaviate.json'

CRISPY_V1 = 'Crispy_v1_search_nyc'
GEO_PROPERTY = 'geoCoordinates'
RETURN_PROPERTIES = [
    #IDs
    'dishRes_ID',
    'dish_ID',
    'restaurant_ID',
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

    # Review data
    'eater_ReviewDictVec',
    'infatuation_ReviewDictVec',
  ]
RETURN_PROPERTIES_2 = [
    'dishRes_ID',
    'dish_ID',
    'restaurant_ID',
    '_additional { id }',
    '_additional { distance }',
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

    'eater_ReviewDictVec',
    'infatuation_ReviewDictVec',
  ]

DISTANCE_MILES = {
    1: 1609.34
}

DISTANCE_KM = {
    1: 1000
}