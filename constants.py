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
PATH_DB_CONFIG_CK = 'cockroach.json'
PATH_OPEN_AI_CONFIG = 'open_ai.json'
PATH_WEAVIATE_CONFIG = 'weaviate.json'

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
    'dish_ID',
    'dishRes_ID',
    '_additional { id }',
    'alternativesWithinSameCuisine',
    'cleanedDishName',
    'closeTime_UberEats_uber',
    'daysOpen_UberEats_uber',
    'dishDescription',
    'dishName',
    'foodItemUberCartLinks',
    'foodItemLinkDoorDash',
    'foodItemLinkUber',
    'imageDoorDash',
    'imageUber',
    'healthAlternatives',
    'lat',
    'linkDoorDash',
    'linkUber',
    'long',
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
CURATED_CUISINES = {
    'american': [
        'Buffalo Wings', 'BBQ Spare Ribs', 'Pulled Pork Sandwich', 'Sausage Egg Cheese Biscuit',
        'Clam Chowder', 'Scrambled Eggs', 'Fruit Salad', 'Pastrami Sandwich', 'Omelette', 'Cobb Salad',
        'Apple Pie', 'Cinnamon Bun', 'Hot Dog', 'Fried Chicken', 'Pot Pie', 'Mashed Potatoes', 'Pancakes',
        'Grilled Cheese Sandwich', 'BLT Sandwich', 'BBQ Ribs', 'Chili', 'Pancake Stack', 'French Toast',
        'Club Sandwich', 'Greek Yogurt Parfait', 'Pumpkin Soup', 'Breakfast Sandwich', 'Shrimp and Grits',
        'Blueberry Muffins', 'Eggs and Bacon', 'Crab Cake', 'Cheeseburger', 'Peanut Butter Jelly', 'S\'mores',
        'Brisket', 'Chicken and Waffles', 'Eggs Benedict', 'Cornbread', 'Meatloaf', 'Hamburger', 'Chicken Tenders',
        'Ribeye Steak', 'Bacon and Eggs', 'Chicken Wings', 'Beef Patty', 'New York Strip Steak', 'Pulled Pork',
        'Filet Mignon', 'Bison Burger', 'Beef Ribs', 'Fried Pork Chops', 'Pork Belly', 'Pork Ribs', 'Grilled Chicken Breast',
        'Roasted Turkey Breast', 'Grilled Pork Chops', 'Baked Potato', 'Turkey Wrap', 'Grilled Pork Tenderloin',
        'Tofu with Mixed Vegetables', 'Cauliflower Stir-Fry', 'Fried Rice', 'Shrimp Stir-Fry', 'Tofu Skewers',
        'Sesame Tofu Stir-Fry', 'Chicken with Mixed Vegetables', 'Quinoa Salad', 'Spinach and Mushroom Omelette',
        'Beef and Broccoli Stir-Fry', 'Cauliflower Pizza Crust', 'Grilled Shrimp Salad', 'Grilled Asparagus',
        'Shrimp Kebab', 'Gluten-Free Pizza', 'Gluten-Free Pasta with Sauce', 'Mushroom Risotto', 'Grilled Chicken Caesar Salad',
        'Caprese Salad', 'Grilled Vegetable Frittata', 'Cucumber Avocado Sushi Rolls', 'Teriyaki Glazed Fish',
        'Teriyaki Glazed Chicken', 'Mediterranean Salad', 'Grilled Lamb Kebabs with Yogurt Sauce', 'Chickpea Salad',
        'Shrimp Tacos', 'Vegetarian Chili', 'Fajita Bowl with Chicken', 'Fajita Bowl with Veggies', 'Shrimp Tacos',
        'Spiced Pilaf', 'Avocado Salad', 'Grilled Salmon', 'Baked Salmon with Sauce', 'Baked Cod with Sauce',
        'Grilled Swordfish with Sauce', 'Sautéed Shrimp with Garlic', 'Thai Curry', 'Chicken Lettuce Wrap',
        'Steamed Mixed Vegetables', 'Eggs and Avocado', 'Baked Chicken', 'Vegetable Soup', 'Grilled Steak with Sauce',
        'Sautéed Spinach with Garlic', 'Veggie Wraps', 'Salmon and Asparagus', 'Baked Halibut', 'Avocado Toast',
        'Grilled Portobello Mushrooms', 'Grilled Vegetable Skewers', 'Cauliflower Tenders', 'Roasted Brussels Sprouts',
        'Caesar Salad', 'Turkey Sandwich', 'Grilled Chicken Salad', 'Grilled Chicken Bowl', 'Grilled Chicken Sandwich',
        'Tomato Soup', 'Breakfast Sandwich', 'Buffalo Roasted Cauliflower', 'Baked Potato', 'Kale and Apple Salad',
        'Stir-Fry Veggies with Tofu', 'Stir-Fry Veggies', 'Stir-Fry Veggies with Chicken', 'Vegetable Noodle Soup',
        'Beef Stir-Fry', 'Green Juice', 'Acai Bowls', 'Overnight Oats with Fruit', 'Garlic String Beans', 'Roasted Veggies',
        'Poke Bowl', 'Green Smoothie', 'Yogurt Parfait with Fruits', 'Quinoa Salad', 'Minestrone Soup', 'Thin Crust Pizza',
        'Sushi', 'Onigiri', 'Greek Salad', 'Mediterranean Bowl', 'Breakfast Burrito', 'Burrito Bowl', 'Taco Salad',
        'Falafel Wrap', 'Hummus and Pita', 'Veggie Sandwich', 'Scrambled Eggs', 'Poached Eggs', 'Omelette', 'Tofu and Rice',
        'Fruit Salad', 'Chicken Noodle Soup', 'Grilled Chicken Nuggets', 'Vegan Chicken Nuggets', 'Chia Pudding',
        'Spaghetti Squash', 'Grilled Veggie Platter', 'Black Bean Sandwich', 'Banh Mi', 'Fish and Rice'
    ],
    'argentinian': [
        'Milanesa', 'Asado', 'Parrillada', 'Empanadas', 'Chimichurri Sauce', 'Provoleta', 'Choripán',
        'Matambre a la Pizza', 'Napolitana Pizza', 'Locro', 'Carbonada', 'Humita', 'Pastel de Papa',
        'Pollo al Disco', 'Flan con Dulce de Leche', 'Dulce de Leche', 'Alfajores', 'Tarta de Ricota',
        'Sopa Paraguaya', 'Revuelto Gramajo', 'Arroz con Leche', 'Budín de Pan', 'Fainá', 'Ravioles'
    ],
    'australian': [
        'Meat Pie', 'Macadamia Cookie', 'Pavlova', 'Lamington', 'ANZAC Biscuits', 'Fairy Bread', 'Vegemite on Toast',
        'Sausage Roll', 'Barramundi', 'Chiko Roll', 'Chicken Parmigiana', 'Damper Bread', 'Tim Tams',
        'Vanilla Slice', 'Pumpkin Soup', 'Kangaroo Steak', 'Smashed Avocado', 'Beetroot Salad', 'Seafood Platter'
    ],
    'brazilian': [
        'Coxinha', 'Tapioca', 'Açaí Bowl', 'Cachorro-Quente', 'Empada', 'Brigadeiro', 'Moqueca', 'Pastel', 'Picanha',
        'Feijoada', 'Farofa', 'Vatapá', 'Bobó de Camarão', 'Caruru', 'Quindim', 'Pão de Queijo', 'Acarajé', 'Cuscuz Paulista',
        'Beijinho', 'Pudim de Leite', 'Romeu e Julieta', 'Bolinho de Bacalhau', 'Cocada', 'Frango com Quiabo'
    ],
    'british': [
        'Fish and Chips', 'Full Breakfast', 'Bread Pudding', 'Shepherd\'s Pie', 'Cornish Pasty', 'Yorkshire Pudding',
        'Roast Beef', 'Sticky Toffee Pudding', 'Bangers and Mash', 'Scotch Egg', 'Black Pudding', 'Beef Wellington',
        'Ploughman\'s Lunch', 'Welsh Rarebit', 'Scones', 'Victoria Sponge', 'Eton Mess', 'Pork Pie', 'Trifle',
        'Steak and Kidney Pie', 'Chicken Tikka Masala', 'Prawn Cocktail', 'Bubble and Squeak', 'Spotted Dick', 'Treacle Tart'
    ],
    'cajun': [
        'Shrimp Grits', 'Cajun Shrimp', 'Cajun Boil', 'Fried Catfish', 'Red Snapper Fish', 'Crawfish', 'Shrimp Po\' Boy',
        'Jambalaya', 'Gumbo', 'Boudin', 'Cajun Crab Cakes', 'Étouffée', 'Dirty Rice', 'Maque Choux', 'Hush Puppies',
        'Beignets', 'Cajun Chicken Wings', 'Crawfish Pie', 'Andouille Sausage', 'Cajun Fried Turkey'
    ],
    'caribbean': [
        'Breadfruit', 'Callaloo', 'Rum Punch', 'Jerk Chicken', 'Rice and Peas', 'Ackee and Saltfish', 'Roti',
        'Doubles', 'Curry Goat', 'Pelau', 'Bakes', 'Saltfish Fritters', 'Fried Plantains', 'Mofongo', 'Pepperpot',
        'Conch Fritters', 'Soursop Juice', 'Jamaican Patties', 'Festival', 'Escovitch Fish', 'Oxtail Stew', 'Pineapple Chow'
    ],
    'chinese': [
        'Har Gow', 'Siu Mai', 'Char Siu Bao', 'Cheung Fun', 'Lo Mai Gai', 'Egg Tarts', 'Turnip Cake', 'Chicken Feet',
        'Sesame Balls', 'Xiao Long Bao', 'Zhajiangmian', 'Lanzhou Beef Noodles', 'Chongqing Noodles', 'Dan Dan Noodles',
        'Biang Biang Noodles', 'Guilin Rice Noodles', 'Beijing Zha Jiang Mian', 'Wuhan Hot Dry Noodles',
        'Sichuan Cold Noodles', 'Yunnan Rice Noodles', 'Yangzhou Fried Rice', 'Hainanese Chicken Rice', 'Claypot Rice',
        'Fujian Fried Rice', 'Lotus Leaf Rice', 'Cantonese Salted Fish and Chicken Fried Rice', 'Eight Treasures Rice',
        'Egg Fried Rice', 'Congee', 'Red Bean Rice', 'Hot and Sour Soup', 'Winter Melon Soup', 'Bird’s Nest Soup',
        'West Lake Beef Soup', 'Egg Drop Soup', 'Wonton Soup', 'Fish Maw Soup', 'Lotus Root Soup', 'Herbal Chicken Soup',
        'Snake Soup', 'Steamed Fish with Ginger and Scallion', 'Salt and Pepper Shrimp', 'Braised Abalone', 'Crispy Fried Squid',
        'Stir-Fried Clams with Black Bean Sauce', 'Steamed Scallops with Garlic Vermicelli', 'Sweet and Sour Fish',
        'Crab with Ginger and Scallions', 'Drunken Shrimp', 'Grilled Eel', 'Red Braised Pork Belly', 'Sweet and Sour Pork',
        'Twice Cooked Pork', 'Moo Shu Pork', 'Dongpo Pork', 'Salt and Pepper Pork', 'Peking Pork Chops', 'Stir-Fried Pork with Green Peppers',
        'Honey Garlic Pork', 'Shredded Pork with Garlic Sauce', 'Kung Pao Chicken', 'White Cut Chicken', 'Beggar’s Chicken',
        'Sichuan Spicy Chicken', 'Soy Sauce Chicken', 'Hakka Salt Baked Chicken', 'Chicken with Black Bean Sauce',
        'Lemon Chicken', 'Steamed Chicken with Mushrooms', 'Mongolian Beef', 'Beef with Broccoli', 'Beef Chow Fun',
        'Black Pepper Beef', 'Beef with Oyster Sauce', 'Braised Beef with Radish', 'Sichuan Boiled Beef', 'Cumin Beef',
        'Beef with Bitter Melon', 'Dry Fried Beef Strips', 'Stir-Fried Bok Choy', 'Mapo Tofu', 'Braised Eggplant',
        'Garlic Stir-Fried Green Beans', 'Stir-Fried Snow Pea Leaves', 'Eggplant with Garlic Sauce', 'Stir-Fried Water Spinach',
        'Braised Tofu with Mushrooms', 'Stuffed Tofu', 'Chinese Cabbage with Vinegar'
    ],
    'ethiopian': [
        'Doro Wat', 'Tibs', 'Kitfo', 'Injera', 'Shiro Wat', 'Misir Wat', 'Gomen', 'Atayef', 'Azifa', 'Firfir'
    ],
    'french': [
        'Chocolate Mousse', 'Quiche Lorraine', 'Croissant', 'Sole Meunière', 'Crepes', 'French Onion Soup',
        'Crème Brûlée', 'Salade Niçoise', 'Coq au Vin', 'Ratatouille', 'Boeuf Bourguignon', 'Duck Confit',
        'Cassoulet', 'Bouillabaisse', 'Tarte Tatin', 'Madeleines', 'Macarons', 'Pain Perdu', 'Rillettes',
        'Croque Monsieur', 'Croque Madame'
    ],
    'fusion': [
        'California Roll Burrito', 'Korean Tacos', 'Sushi Pizza', 'Ramen Burger', 'Pho Tacos', 'Bulgogi Burrito',
        'Kimchi Fries', 'Poke Nachos', 'Sushi Burrito', 'Tikka Masala Poutine'
    ],
    'german': [
        'Sauerkraut', 'Rouladen', 'Bratwurst', 'Kartoffelsalat', 'Reibekuchen', 'Weisswurst', 'Eintopf',
        'Kohlrouladen', 'Leberwurst', 'Sauerbraten', 'Schnitzel', 'Pretzel', 'Black Forest Cake', 'Apfelstrudel',
        'Rote Grütze', 'Marzipan', 'Rindergulasch', 'Schwarzwälder Kirschtorte', 'Stollen', 'Frikadellen'
    ],
    'greek': [
        'Tzatziki', 'Moussaka', 'Feta Dip', 'Spanakopita', 'Keftedes', 'Lamb Gyros', 'Pastitsio', 'Greek Salad',
        'Stuffed Peppers', 'Chicken Gyro', 'Avgolemono Soup', 'Souvlaki', 'Baklava', 'Dolmades', 'Galaktoboureko',
        'Loukoumades', 'Saganaki', 'Horta', 'Fasolada', 'Gemista'
    ],
    'hawaiian': [
        'Spam Musubi', 'Poke Bowl', 'Kalua Pork', 'Loco Moco', 'Huli Huli Chicken', 'Haupia', 'Lomi Lomi Salmon',
        'Plate Lunch', 'Chicken Long Rice', 'Manapua', 'Poi', 'Malasadas', 'Butter Mochi', 'Saimin', 'Shave Ice',
        'Garlic Shrimp', 'Laulau', 'Hawaiian Sweet Bread', 'Taro Chips', 'Ahi Tuna'
    ],
    'indian': [
        'Kulfi', 'Malai Kofta', 'Rasmalai', 'Rogan Josh', 'Chicken Tikka Masala', 'Chole Bhature', 'Dal Makhani',
        'Roti', 'Kheer', 'Paneer Tikka', 'Butter Naan', 'Mango Lassi', 'Gulab Jamun', 'Bhindi Masala',
        'Biryani', 'Pulao', 'Fish Curry', 'Keema Naan', 'Tandoori Roti', 'Chana Masala', 'Raita',
        'Pav Bhaji', 'Aloo Gobi', 'Butter Chicken', 'Chapati', 'Chaat', 'Pakora', 'Vada Pav',
        'Baingan Bharta', 'Samosa', 'Mutton Masala', 'Pani Puri', 'Tandoori Chicken', 'Aloo Paratha'
    ],
    'italian': [
        'Amatriciana', 'Polpette', 'Rigatoni alla Carbonara', 'Linguine con Vongole', 'Eggplant Parmigiana',
        'Ossobuco', 'Chicken Parmesan', 'Cacio e Pepe', 'Gelato', 'Panna Cotta', 'Caprese Salad', 'Gnocchi',
        'Margherita Pizza', 'Lasagna', 'Tiramisu', 'Pasta Carbonara', 'Spaghetti Bolognese', 'Risotto',
        'Lobster Fra Diavolo', 'Minestrone Soup', 'Fettuccine Alfredo', 'Bruschetta', 'Arancini', 'Polenta',
        'Saltimbocca', 'Cannoli', 'Panettone', 'Pesto Pasta', 'Focaccia', 'Porchetta', 'Osso Buco', 'Scaloppine'
    ],
    'japanese': [
        'Gyoza', 'Katsu', 'Sashimi', 'Udon', 'Tamagoyaki', 'Chashu Pork', 'Miso Soup', 'Unagi', 'Japanese Pickles',
        'Sushi', 'Karaage', 'Takoyaki', 'Ramen', 'Onigiri', 'Matcha Green Tea', 'Matcha Ice Cream', 'Yakisoba',
        'Okonomiyaki', 'Katsudon', 'Tempura', 'Shabu Shabu', 'Sukiyaki', 'Tonkatsu', 'Yudofu', 'Zaru Soba', 'Taiyaki'
    ],
    'korean': [
        'Kimchi', 'Bulgogi', 'Bibimbap', 'Galbi', 'Japchae', 'Kimchi Stew', 'Korean BBQ', 'Pajeon',
        'Sundubu Jjigae', 'Soondae', 'Tteokbokki', 'Jajangmyeon', 'Dak Galbi', 'Korean Fried Chicken',
        'Samgyeopsal', 'Doenjang Jjigae', 'Haemul Pajeon', 'Bossam', 'Gyeran Jjim', 'Gopchang', 'Banchan', 'Mul Naengmyeon'
    ],
    'latin_american': [
        'Chicken Empanada', 'Arepa', 'Beef Empanada', 'Tamale', 'Tostones', 'Pupusa', 'Ceviche', 'Ropa Vieja',
        'Lechón', 'Feijoada', 'Chimichurri', 'Asado', 'Churros', 'Tres Leches Cake', 'Arroz con Pollo', 'Lomo Saltado',
        'Pão de Queijo', 'Mole Poblano', 'Pozole', 'Mofongo', 'Ajiaco', 'Aguadito', 'Bandeja Paisa', 'Patacones', 'Anticuchos'
    ],
    'lebanese': [
        'Hummus', 'Lamb Chops', 'Falafel', 'Lebanese Lentils', 'Labneh', 'Tabbouleh', 'Fattoush', 'Baba Ghanoush',
        'Shish Tawook', 'Kibbeh', 'Kafta', 'Manakish', 'Warak Enab', 'Sfeeha', 'Mujaddara', 'Sambousek', 'Baklava',
        'Knafeh', 'Shawarma', 'Arayes', 'Makanek', 'Mujadara', 'Mhammara'
    ],
    'mediterranean': [
        'Baklava', 'Couscous', 'Fish with Herb Sauce', 'Hummus', 'Falafel', 'Shakshuka', 'Tabbouleh', 'Dolmas',
        'Gyro', 'Kebabs', 'Spanakopita', 'Moussaka', 'Tzatziki', 'Baba Ghanoush', 'Pita Bread', 'Fattoush',
        'Kibbeh', 'Kefta', 'Grilled Octopus', 'Souvlaki', 'Lamb Kofta', 'Chicken Shawarma', 'Lentil Soup', 'Koulouri'
    ],
    'mexican': [
        'Nachos', 'Tacos', 'Fajitas', 'Chiles Rellenos', 'Carne Asada', 'Taco Salad', 'Enchiladas', 'Margarita',
        'Quesadillas', 'Churros', 'Guacamole', 'Burritos', 'Huevos Rancheros', 'Tostada', 'Salsa', 'Tamales', 'Taquitos',
        'Sopaipillas', 'Pozole', 'Mole', 'Carnitas', 'Al Pastor', 'Elote', 'Birria', 'Sopes', 'Horchata', 'Menudo', 'Flan'
    ],
    'middle_eastern': [
        'Lamb Kebab', 'Beef Shawarma', 'Hummus', 'Chicken Shawarma', 'Shish Kebab', 'Chicken Kebab', 'Baklava',
        'Falafel', 'Tabbouleh', 'Baba Ghanoush', 'Fattoush', 'Labneh', 'Manakeesh', 'Kibbeh', 'Dolma', 'Mutabal', 'Arayes',
        'Knafeh', 'Mujaddara', 'Sfiha', 'Lamb Chops', 'Sumac Chicken', 'Sambousek', 'Kunafa'
    ],
    'moroccan': [
        'Lamb Tagine', 'Couscous', 'Chicken Tagine', 'Harira', 'Bastilla', 'Zaalouk', 'Kefta Mkaouara', 'Rfissa',
        'Briouats', 'Mechoui', 'Tangia', 'Baklava', 'Maakouda', 'Seffa', 'Bissara', 'Chebakia', 'Sfinge', 'Mrouzia', 'Harissa'
    ],
    'nigerian': [
        'Jollof Rice', 'Fried Plantains', 'Egusi Soup', 'Fufu', 'Pepper Soup', 'Suya', 'Moi Moi', 'Boli', 'Afang Soup',
        'Pounded Yam', 'Efo Riro', 'Ogbono Soup', 'Akara', 'Nkwobi', 'Ewedu Soup', 'Banga Soup', 'Kilishi', 'Tuwo Shinkafa',
        'Ofada Rice', 'Gbegiri', 'Moin Moin'
    ],
    'peruvian': [
        'Ceviche', 'Lomo Saltado', 'Aji de Gallina', 'Pollo a la Brasa', 'Papa a la Huancaína', 'Anticuchos', 'Rocoto Relleno',
        'Causa Rellena', 'Tacu Tacu', 'Seco de Cabrito', 'Arroz con Pollo', 'Chicha Morada', 'Leche de Tigre', 'Ocopa',
        'Chupe de Camarones', 'Carapulcra', 'Picarones', 'Suspiro a la Limeña', 'Mazamorra Morada', 'Papa Rellena'
    ],
    'portuguese': [
        'Pastel de Nata', 'Bacalhau a Bras', 'Grilled Sardines', 'Portuguese Egg Tarts', 'Piri Piri Chicken',
        'Francesinha', 'Caldo Verde', 'Feijoada', 'Bifana', 'Arroz de Pato', 'Polvo à Lagareiro', 'Cataplana', 'Amêijoas à Bulhão Pato',
        'Sopa da Pedra', 'Queijo da Serra', 'Alheira', 'Ginjinha', 'Açorda', 'Dobrada', 'Arroz Doce'
    ],
    'spanish': [
        'Gazpacho', 'Patatas Bravas', 'Churros', 'Tortilla Española', 'Gambas al Ajillo', 'Paella', 'Jamón Ibérico',
        'Flan', 'Sangria', 'Serrano Ham', 'Pulpo a la Gallega', 'Croquetas', 'Pimientos de Padrón', 'Albóndigas', 'Salmorejo',
        'Tarta de Santiago', 'Pulpo a Feira', 'Calamares a la Romana', 'Empanada Gallega', 'Rabo de Toro'
    ],
    'swedish': [
        'Swedish Meatballs', 'Gravadlax', 'Lingonberry Jam', 'Raggmunk', 'Jansson\'s Temptation', 'Köttbullar', 'Kroppkakor',
        'Toast Skagen', 'Knäckebröd', 'Smörgåstårta', 'Prinsesstårta', 'Sill', 'Semla', 'Pytt i Panna', 'Ärtsoppa', 'Lutfisk', 'Surströmming'
    ],
    'thai': [
        'Pad Thai', 'Red Curry', 'Green Curry', 'Mango Sticky Rice', 'Thai Iced Tea', 'Thai Fish Cakes', 'Tom Yum Soup',
        'Papaya Salad', 'Massaman Curry', 'Basil Chicken', 'Larb', 'Yellow Curry', 'Som Tum', 'Pad See Ew', 'Tom Kha Gai',
        'Moo Ping', 'Khao Soi', 'Kai Jeow', 'Gaeng Keow Wan', 'Yam Woon Sen'
    ],
    'turkish': [
        'Turkish Delight', 'Lamb Doner Kebab', 'Chicken Doner Kebab', 'Turkish Coffee', 'Pide', 'Lahmacun', 'Baklava',
        'Kofte', 'Adana Kebab', 'Manti', 'Borek', 'Menemen', 'Simit', 'Imam Bayildi', 'Dolma', 'Kumpir', 'Iskender Kebab',
        'Cacik', 'Sarma', 'Karnıyarık'
    ],
    'vietnamese': [
        'Pho', 'Banh Mi', 'Goi Cuon', 'Bun Cha', 'Vietnamese Iced Coffee', 'Bun Bo Hue', 'Spring Rolls', 'Com Tam', 'Nem Ran',
        'Ca Kho To', 'Banh Xeo', 'Cha Ca La Vong', 'Mi Quang', 'Bo Luc Lac', 'Canh Chua', 'Hu Tieu', 'Ga Nuong', 'Xoi', 'Che',
        'Bun Rieu'
    ]
}
CURATED_DIETS = {
    'carnivore diet': [
      'Ribeye Steak', 'Korean Chicken Wings', 'Bacon and Eggs', 'Chicken Wings', 'Beef Patty', 'New York Strip Steak',
      'Pulled Pork', 'Filet Mignon', 'Bison', 'Beef Ribs', 'Fried Pork Chops', 'Pork Belly', 'Pork Ribs', 'Steak Tartare',
      'Beef Liver', 'Sashimi', 'Grilled Lamb Chops', 'Grilled Salmon', 'Bone Soup'
    ],
    'gluten free': [
      'Grilled Chicken Breast', 'Roasted Turkey Breast', 'Grilled Pork Chops', 'Baked Potato', 'Turkey Wraps',
      'Gluten-Free Caesar Salad', 'Grilled Pork Tenderloin', 'Tofu With Mixed Vegetables', 'Cauliflower Stir Fried',
      'Gluten Free Fried Rice', 'Shrimp Stir Fry', 'Gluten-Free Tofu Skewers', 'Sesame Tofu Stir Fry', 'Chicken With Mixed Vegetables',
      'Quinoa Salad', 'Spinach and Mushroom Omelette', 'Gluten Free Chow Mein', 'Beef and Broccoli Stir Fry', 'Gluten-Free Tofu Fried Rice',
      'Cauliflower Pizza Crust', 'Quinoa Salad', 'Gluten-Free Cauliflower Manchurian', 'Grilled Shrimp Salad', 'Grilled Asparagus',
      'Shrimp Kebab', 'Gluten-Free Pizza', 'Gluten-Free Pasta with Sauce', 'Mushroom Risotto', 'Grilled Chicken Caesar Salad', 'Caprese Salad',
      'Grilled Vegetable Frittata', 'Gluten-Free Frittata', 'Cucumber Avocado Sushi Rolls', 'Teriyaki Glazed Fish', 'Teriyaki Glazed Chicken',
      'Mediterranean Salad', 'Grilled Lamb Kebabs with Yogurt Sauce', 'Chickpea Salad', 'Shrimp Tacos', 'Vegetarian Chilli',
      'Gluten-Free Fajita Bowl with Chicken', 'Gluten-free Fajita Bowl with Veggies', 'Gluten-Free Shrimp Tacos', 'Gluten-Free Chili',
      'Gluten-Free Spiced Pilaf', 'Avocado Salad', 'Grilled Salmon', 'Baked Salmon with Gluten Free Sauce', 'Baked Cod with Gluten Free Sauce',
      'Grilled Swordfish with Sauce', 'Sautéed Shrimp with Garlic', 'Thai Curry', 'Chicken Lettuce Wrap', 'Steamed Mixed Vegetables',
      'Eggs and Avocado', 'Baked Chicken', 'Vegetable Soup', 'Grilled Steak with Gluten Free Sauce', 'Sautéed Spinach with Garlic',
      'Veggie Gluten Free Wraps', 'Salmon and Asparagus', 'Baked Halibut', 'Gluten-Free Avocado Toast', 'Grilled Portobello Mushrooms',
      'Grilled Vegetable Skewers', 'Gluten-Free Cauliflower Tenders', 'Gluten-Free Cauliflower', 'Roasted Brussels Sprouts'
    ],
    'halal': [
      'Halal Burgers', 'Gyro', 'Lamb Gyro', 'Chicken Tandoori', 'Samosas', 'Beef Seekh Kebab', 'Indian Butter Chicken',
      'Biryani', 'Baba Ghanouj', 'Baklava', 'Hummus', 'Shawarma', 'Tabbouleh', 'Kebab', 'Shish Kebab', 'Chicken Over Rice',
      'Kofta Kebab', 'Mixed Grill Platter'
    ],
    'healthy': [
      'Caesar Salad', 'Turkey Sandwich', 'Avocado Toast', 'Grilled Chicken Salad', 'Grilled Chicken Bowl', 'Grilled Chicken Sandwich',
      'Tomato Soup', 'Breakfast Sandwich', 'Buffalo Roasted Cauliflower', 'Baked Potato', 'Kale and Apple Salad', 'Stir Fry Veggies with Tofu',
      'Stir Fry Veggies', 'Stir Fry Veggies with Chicken', 'Vegetable Noodle Soup', 'Beef Stir-Fry', 'Green Juice', 'Acai Bowls',
      'Overnight Oats with Fruit', 'Garlic String Beans', 'Roasted Veggies', 'Poke Bowl', 'Green Smoothie', 'Yogurt Parfait with Fruits',
      'Quinoa Salad', 'Minestrone Soup', 'Thin Crust Pizza', 'Sushi', 'Onigiri', 'Greek Salad', 'Mediterranean Bowl', 'Breakfast Burrito',
      'Burrito Bowl', 'Taco Salad', 'Falafel Wrap', 'Hummus and Pita', 'Veggie Sandwich', 'Scrambled Eggs', 'Poached Eggs', 'Omelette',
      'Tofu and Rice', 'Fruit Salad', 'Chicken Noodle Soup', 'Grilled Chicken Nuggets', 'Vegan Chicken Nuggets', 'Chia Pudding',
      'Spaghetti Squash', 'Grilled Veggie Platter', 'Black Bean Sandwich', 'Banh Mi', 'Fish and Rice'
    ],
    'keto': [
      'Cobb Salad', 'Bacon and Eggs', 'Egg Salad', 'Caesar Salad', 'Butter Filet', 'Chicken Lettuce Wrap', 'Buffalo Wings',
      'Shrimp and Avocado Salad', 'Pork Belly with Green Pepper', 'Beef Stir-Fry with Mixed Vegetables', 'Meatballs in Marinara Sauce',
      'Eggplant Lasagna', 'Caprese Salad', 'Grilled Salmon with Asparagus', 'Keto Salad', 'Keto Chicken', 'Keto Beef'
    ],
    'paleo': [
      'Grilled Chicken', 'Sweet Potato Fries', 'Brussels Sprout Salad', 'Butternut Squash Soup', 'Beef and Broccoli Stir-Fry',
      'Cucumber Salad', 'Prosciutto Melon Salad', 'Beet Salad', 'Lettuce Wraps', 'Grilled Salmon'
    ],
    'pescatarian': [
      'Crab Cakes', 'Clam Chowder', 'Lobster Roll', 'Vegetable Stir Fry with Tofu', 'Avocado Toast with Poached Egg', 'Shrimp Scampi',
      'Grilled Octopus', 'Fish Tacos', 'Mushroom Taco', 'Black Beans and Cilantro Lime Rice', 'Falafel with Tzatziki Sauce', 'Grilled Salmon',
      'Pan-Seared Tuna Steaks', 'Seared Scallops', 'Seafood Paella', 'Homemade Southwest Black Bean Burger', 'Quinoa Salad with Roasted Vegetables'
    ],
    'sibo friendly': [
      'Roasted Turkey Breast', 'Roasted Pork Loin', 'Egg Salad', 'Sautéed Beef Strips with Bell Peppers and Ginger', 'Stir-fried Tofu with Bamboo Shoots and Carrots',
      'Lamb Chops', 'Chicken and Ginger Soup', 'Egg Frittata with Spinach', 'Baked Cod', 'Baked Chicken', 'Baked Salmon with Lemon', 'Grilled Shrimp',
      'Sautéed Scallops with Lemon and Parsley', 'Grilled Chicken Breast with Herbs', 'Beef Stew', 'Homemade Chicken Soup', 'Mackerel',
      'Quinoa Salad with Cucumbers and Carrots'
    ],
    'vegan': [
      'Vegan Caesar Salad', 'Vegan Overnight Oats', 'Vegan Stir Fry', 'Tofu Stir Fry', 'Vegan Noodles', 'Vegan Spring Rolls', 'Vegan Acai Bowl',
      'Vegan Ice Cream', 'Daal', 'Vegan Curry with Chickpeas', 'Vegan Pasta', 'Vegan Pizza', 'Vegan Sushi', 'Avocado Cucumber Roll',
      'Vegan Tempura with Vegetables', 'Vegan Kimchi Tofu Stew', 'Vegan Tacos', 'Vegan Breakfast Burritos', 'Vegan Quesadillas', 'Vegan Pad Thai',
      'Vegan Curry', 'Vegan Salad', 'Vegan Sandwich', 'Vegan Chilli', 'Vegan Burger', 'Vegan Lentil Soup', 'Vegan Soup', 'Vegan Wings',
      'Vegan Breakfast Sandwich', 'Vegan Wrap', 'Vegan Cake', 'Vegan Chocolate Cake', 'Vegan Mushroom Burger', 'Vegan Oatmeal', 'Vegan Cheese Fries',
      'Vegan Waffles', 'Vegan Bagel', 'Vegan Mac and Cheese', 'Vegan Chia Seed Pudding', 'Vegan Fried Chicken', 'Chickpea Sandwich', 'Vegan Butternut Squash',
      'Vegan Vegetable Bowl with Quinoa', 'Vegan Pho'
    ],
    'vegetarian': [
      'Vegetarian Mac n Cheese', 'Vegetarian Broccoli Cheddar Soup', 'Vegetarian Stir Fry', 'Tofu Stir Fry', 'Vegetarian Noodles', 'Vegetarian Spring Rolls',
      'Vegetarian Stir Fry with Tofu', 'Spinach Quiche', 'Vegetarian Quiche', 'Daal', 'Paneer Tikka Masala', 'Channa Masala', 'Vegetable Korma',
      'Vegetarian Pasta', 'Vegetarian Pizza', 'Margherita Pizza', 'Caprese Salad', 'Spinach and Ricotta Ravioli', 'Vegetarian Ravioli', 'Mushroom Risotto',
      'Vegetarian Risotto', 'Vegetarian Fettuccine Alfredo', 'Vegetarian Sushi', 'Avocado Cucumber Roll', 'Greek Salad', 'Vegetarian Chilli', 'Vegetable Tacos',
      'Vegetarian Breakfast Burritos', 'Vegetarian Quesadillas', 'Vegetarian Cheese', 'Enchiladas', 'Vegetarian Burger', 'Vegetarian Lentil Soup', 'Vegetarian Curry',
      'Vegetarian Breakfast Sandwich', 'Vegetarian Sandwich', 'Vegetarian Wrap', 'Chickpea Sandwich', 'Roasted Beet and Goat Cheese Salad', 'Vegetarian Pho with Tofu'
    ]
}
CURATED_DISHES = {
    'Açaí bowls': [
        'Banana Açaí Bowl', 'Mixed Berry Açaí Bowl', 'Peanut Butter Açaí Bowl', 'Coconut Açaí Bowl', 'Mango Açaí Bowl',
        'Granola Açaí Bowl', 'Blueberry Açaí Bowl', 'Tropical Açaí Bowl', 'Chocolate Açaí Bowl', 'Raspberry Açaí Bowl',
        'Strawberry Açaí Bowl', 'Pineapple Açaí Bowl', 'Kiwi Açaí Bowl', 'Almond Açaí Bowl', 'Spinach Açaí Bowl',
        'Apple Açaí Bowl', 'Dragon Fruit Açaí Bowl', 'Hemp Seed Açaí Bowl', 'Chia Seed Açaí Bowl', 'Pomegranate Açaí Bowl'
    ],
    'Beef bulgogi': [
        'Classic Beef Bulgogi', 'Beef Bulgogi with Rice', 'Beef Bulgogi Bowl', 'Beef Bulgogi with Noodles',
        'Spicy Beef Bulgogi', 'Beef Bulgogi Wrap', 'Beef Bulgogi Salad', 'Beef Bulgogi Tacos',
        'Beef Bulgogi Lettuce Wraps', 'Beef Bulgogi Stir-Fry', 'Beef Bulgogi Skewers', 'Beef Bulgogi Bibimbap'
    ],
    'Beef stroganoff': [
        'Classic Beef Stroganoff', 'Beef Stroganoff with Sour Cream', 'Beef Stroganoff over Noodles',
        'Beef Stroganoff with Mushrooms', 'Beef Stroganoff over Rice', 'Chicken Stroganoff',
        'Vegetarian Stroganoff (Mushroom)', 'Pork Stroganoff', 'Beef Stroganoff with Mustard',
        'Beef Stroganoff with Red Wine', 'Beef Stroganoff with Paprika', 'Beef Stroganoff with Parsley'
    ],
    'Bibimbap': [
        'Classic Beef Bibimbap', 'Chicken Bibimbap', 'Vegetable Bibimbap', 'Spicy Pork Bibimbap', 'Tofu Bibimbap',
        'Mushroom Bibimbap', 'Bibimbap with Kimchi', 'Seafood Bibimbap', 'Shrimp Bibimbap', 'Salmon Bibimbap',
        'Egg Bibimbap', 'Beef and Vegetable Bibimbap'
    ],
    'Biryani': [
        'Chicken Biryani', 'Lamb Biryani', 'Vegetable Biryani', 'Beef Biryani', 'Shrimp Biryani',
        'Hyderabadi Biryani', 'Egg Biryani', 'Mutton Biryani', 'Fish Biryani', 'Paneer Biryani', 'Goat Biryani',
        'Jackfruit Biryani', 'Quinoa Biryani', 'Cauliflower Biryani'
    ],
    'Breakfasts': [
        'Avocado Toast (Vegan)', 'Pancakes (Gluten-Free)', 'French Toast', 'Eggs Benedict', 'Breakfast Burrito (Vegan)',
        'Omelette', 'Smoothie Bowl', 'Granola with Yogurt', 'Waffles (Gluten-Free)', 'Muffins (Vegan)',
        'Bagel with Lox', 'Hash Browns (Vegan)', 'Tofu Scramble (Vegan)', 'Fruit Salad (Vegan and Gluten-Free)',
        'Chia Pudding', 'Acai Bowl', 'Breakfast Sandwich', 'Huevos Rancheros', 'Biscuits and Gravy', 'Frittata',
        'Muesli', 'Croissant', 'English Breakfast', 'Breakfast Tacos', 'Shakshuka', 'Protein Pancakes'
    ],
    'Burritos': [
        'Burrito Bowl', 'Burrito with Avocado', 'Burrito with Guacamole', 'Classic Burrito', 'Grilled Chicken Burrito',
        'Beef Burrito', 'Breakfast Burrito', 'Vegetarian Burrito', 'Vegan Burrito', 'Gluten-Free Burrito',
        'Pork Burrito', 'Fish Burrito', 'Shrimp Burrito', 'Spicy Burrito', 'Steak and Shrimp Burrito',
        'Chorizo Burrito', 'Chipotle Burrito', 'California Burrito', 'Burrito with Rice and Beans', 'Cheese Burrito'
    ],
    'Cannoli': [
        'Classic Ricotta Cannoli', 'Chocolate Chip Cannoli', 'Chocolate Dipped Cannoli', 'Mini Cannoli',
        'Strawberry Cannoli', 'Pistachio Cannoli', 'Vanilla Cannoli', 'Lemon Cannoli', 'Coconut Cannoli',
        'Almond Cannoli', 'Hazelnut Cannoli'
    ],
    'Chicken parmesan': [
        'Classic Chicken Parmesan', 'Baked Chicken Parmesan', 'Chicken Parmesan Sandwich', 'Chicken Parmesan Pizza',
        'Grilled Chicken Parmesan', 'Spaghetti Chicken Parmesan', 'Vegan Chicken Parmesan', 'Gluten-Free Chicken Parmesan',
        'Chicken Parmesan with Marinara', 'Chicken Parmesan with Mozzarella', 'Chicken Parmesan Sub', 'Chicken Parmesan Sliders'
    ],
    'Desserts': [
        'Apple Pie', 'Banana Bread', 'Brownies', 'Cheesecake', 'Chocolate Cake', 'Chocolate Chip Cookies',
        'Chocolate Covered Strawberries', 'Chocolate Mousse', 'Cinnamon Rolls', 'Cupcakes', 'Eclairs', 'Fruit Tart',
        'Gelato', 'Ice Cream Sundae', 'Key Lime Pie', 'Lava Cake', 'Lemon Bars', 'Macarons', 'Peach Cobbler',
        'Pumpkin Pie', 'Red Velvet Cake', 'Rice Pudding', 'Strawberry Shortcake', 'Tiramisu',
        'Vegan Brownies', 'Gluten-Free Chocolate Cake', 'Vegan Ice Cream', 'Gluten-Free Apple Pie',
        'Chocolate Souffle', 'Creme Brulee', 'Churros', 'Baklava', 'Pecan Pie', 'Carrot Cake', 'Mango Pineapple Smoothie',
        'Chocolate Protein Smoothie', 'Raspberry Sorbet', 'Pumpkin Cheesecake', 'Tart Tatin', 'Molten Chocolate Cake',
        'Peanut Butter Pie', 'Bread Pudding', 'Chocolate Fondue', 'Caramel Apples', 'Blueberry Cobbler',
        'Lemon Meringue Pie', 'Strawberry Cheesecake'
    ],
    'Drunken noodles': [
        'Classic Drunken Noodles', 'Chicken Drunken Noodles', 'Beef Drunken Noodles', 'Shrimp Drunken Noodles',
        'Tofu Drunken Noodles (Vegan)', 'Vegetarian Drunken Noodles', 'Gluten-Free Drunken Noodles',
        'Pork Drunken Noodles', 'Seafood Drunken Noodles', 'Salmon Drunken Noodles', 'Udon Drunken Noodles',
        'Drunken Noodles with Basil'
    ],
    'Dumplings': [
        'Pork Dumplings', 'Chicken Dumplings', 'Shrimp Dumplings', 'Beef Dumplings', 'Vegetable Dumplings (Vegan)',
        'Mushroom Dumplings (Vegan)', 'Gluten-Free Dumplings', 'Soup Dumplings', 'Spinach and Ricotta Dumplings',
        'Cheese Dumplings', 'Crab Dumplings', 'Turkey Dumplings', 'Duck Dumplings'
    ],
    'Empanadas': [
        'Beef Empanadas', 'Chicken Empanadas', 'Cheese Empanadas', 'Spinach Empanadas', 'Vegetable Empanadas (Vegan)',
        'Mushroom Empanadas (Vegan)', 'Gluten-Free Empanadas', 'Shrimp Empanadas', 'Ham and Cheese Empanadas',
        'Corn Empanadas', 'Pork Empanadas', 'Sweet Potato Empanadas', 'Chorizo Empanadas', 'Lentil Empanadas'
    ],
    'Fajitas': [
        'Beef Fajitas', 'Chicken Fajitas', 'Shrimp Fajitas', 'Vegetable Fajitas (Vegan)', 'Tofu Fajitas (Vegan)',
        'Gluten-Free Fajitas', 'Pork Fajitas', 'Steak Fajitas', 'Mixed Fajitas', 'Spicy Fajitas', 'Fajitas with Guacamole'
    ],
    'Fish and chips': [
        'Classic Fish and Chips', 'Crispy Fish and Chips', 'Fish and Chips with Tartar Sauce', 'Grilled Fish and Chips',
        'Spicy Fish and Chips', 'Gluten-Free Fish and Chips', 'Fish and Chips with Lemon Wedges', 'Beer Battered Fish and Chips',
        'Fish and Chips with Coleslaw', 'Fish and Chips with Mushy Peas', 'Fish and Chips with Sweet Potato Fries'
    ],
    'Goulash': [
        'Beef Goulash', 'Chicken Goulash', 'Pork Goulash', 'Vegetarian Goulash', 'Vegan Goulash', 'Gluten-Free Goulash',
        'Hungarian Goulash', 'Lamb Goulash', 'Turkey Goulash', 'Goulash with Dumplings'
    ],
    'Hot dogs': [
        'Classic Hot Dog', 'Chili Cheese Hot Dog', 'Chicago Style Hot Dog', 'New York Style Hot Dog',
        'Vegan Hot Dog', 'Gluten-Free Hot Dog', 'Grilled Hot Dog', 'Sauerkraut Hot Dog', 'Bacon Wrapped Hot Dog',
        'Corn Dog', 'Slaw Dog', 'Spicy Hot Dog'
    ],
    'Jambalaya': [
        'Classic Jambalaya', 'Chicken and Sausage Jambalaya', 'Shrimp Jambalaya', 'Spicy Jambalaya',
        'Vegetarian Jambalaya', 'Vegan Jambalaya', 'Gluten-Free Jambalaya', 'Seafood Jambalaya', 'Crawfish Jambalaya',
        'Lobster Jambalaya', 'Jambalaya with Ham', 'Spicy Jambalaya Pasta'
    ],
    'Juices': [
        'Apple Juice', 'Orange Juice', 'Grape Juice', 'Carrot Juice', 'Green Juice', 'Beet Juice',
        'Pineapple Juice', 'Watermelon Juice', 'Mango Juice', 'Cranberry Juice', 'Pomegranate Juice',
        'Detox Juice', 'Immunity Boosting Juice', 'Energy Boosting Juice', 'Celery Juice', 'Cucumber Juice',
        'Ginger Juice', 'Mixed Berry Juice', 'Lemonade', 'Limeade', 'Passion Fruit Juice', 'Papaya Juice',
        'Spinach Juice', 'Superfood Juice', 'Turmeric Juice', 'Aloe Vera Juice', 'Guava Juice', 'Kiwi Juice',
        'Mint Juice', 'Chlorophyll Juice', 'Coconut Water', 'Tomato Juice', 'Hydrating Juice', 'Digestive Juice'
    ],
    'Lasagna': [
        'Classic Lasagna', 'Beef Lasagna', 'Chicken Lasagna', 'Vegetable Lasagna (Vegan)', 'Seafood Lasagna',
        'Spinach Lasagna', 'Gluten-Free Lasagna', 'Lasagna with Ricotta', 'Meatball Lasagna', 'Pesto Lasagna',
        'Zucchini Lasagna', 'Eggplant Lasagna', 'Mushroom Lasagna', 'Turkey Lasagna', 'Four Cheese Lasagna'
    ],
    'Milkshakes': [
        'Chocolate Milkshake', 'Strawberry Milkshake', 'Vanilla Milkshake', 'Banana Milkshake',
        'Peanut Butter Milkshake', 'Cookies and Cream Milkshake', 'Mango Milkshake', 'Vegan Milkshake',
        'Gluten-Free Milkshake', 'Blueberry Milkshake', 'Pineapple Milkshake', 'Coffee Milkshake', 'Nutella Milkshake',
        'Mint Chocolate Chip Milkshake', 'Salted Caramel Milkshake'
    ],
    'Moussaka': [
        'Classic Moussaka', 'Beef Moussaka', 'Lamb Moussaka', 'Vegetarian Moussaka', 'Vegan Moussaka',
        'Gluten-Free Moussaka', 'Eggplant Moussaka', 'Greek Moussaka', 'Potato Moussaka', 'Turkey Moussaka'
    ],
    'Pad thai': [
        'Classic Pad Thai', 'Chicken Pad Thai', 'Shrimp Pad Thai', 'Beef Pad Thai', 'Tofu Pad Thai (Vegan)',
        'Vegetable Pad Thai', 'Gluten-Free Pad Thai', 'Pork Pad Thai', 'Seafood Pad Thai', 'Spicy Pad Thai',
        'Pad Thai with Peanut Sauce'
    ],
    'Pho': [
        'Classic Pho', 'Beef Pho', 'Chicken Pho', 'Seafood Pho', 'Shrimp Pho', 'Vegetable Pho (Vegan)',
        'Gluten-Free Pho', 'Pork Pho', 'Duck Pho', 'Pho with Meatballs', 'Spicy Pho', 'Pho with Bone Broth'
    ],
    'Pizza': [
        'Cheese Pizza', 'Pepperoni Pizza', 'Margherita Pizza', 'BBQ Chicken Pizza', 'Buffalo Chicken Pizza',
        'Vegetarian Pizza', 'Hawaiian Pizza', 'Meat Lovers Pizza', 'Gluten-Free Pizza', 'Vegan Pizza',
        'Sicilian Pizza', 'Greek Pizza', 'Spinach and Feta Pizza', 'Supreme Pizza', 'Four Cheese Pizza',
        'White Pizza', 'Prosciutto Pizza', 'Mushroom Pizza', 'Pesto Pizza', 'Taco Pizza', 'Truffle Pizza'
    ],
    'Poke bowls': [
        'Classic Poke Bowl', 'Ahi Tuna Poke Bowl', 'Chicken Poke Bowl', 'Shrimp Poke Bowl', 'Spicy Salmon Poke Bowl',
        'Spicy Tuna Poke Bowl', 'Vegetable Poke Bowl (Vegan)', 'Gluten-Free Poke Bowl', 'Tofu Poke Bowl (Vegan)',
        'Salmon Poke Bowl', 'Tuna Poke Bowl', 'Mango Poke Bowl', 'Avocado Poke Bowl', 'Octopus Poke Bowl'
    ],
    'Quesadillas': [
        'Classic Quesadilla', 'Chicken Quesadilla', 'Beef Quesadilla', 'Vegetable Quesadilla (Vegan)',
        'Mushroom Quesadilla', 'Shrimp Quesadilla', 'Gluten-Free Quesadilla', 'Cheese Quesadilla',
        'Spinach Quesadilla', 'Steak Quesadilla', 'Pork Quesadilla', 'Chorizo Quesadilla'
    ],
    'Ramen': [
        'Classic Ramen', 'Chicken Ramen', 'Beef Ramen', 'Pork Ramen', 'Shrimp Ramen', 'Vegetarian Ramen (Vegan)',
        'Miso Ramen', 'Spicy Ramen', 'Gluten-Free Ramen', 'Seafood Ramen', 'Tofu Ramen (Vegan)', 'Egg Ramen',
        'Kimchi Ramen', 'Shoyu Ramen', 'Tonkotsu Ramen'
    ],
    'Salads': [
        'Caesar Salad', 'Greek Salad', 'Chicken Caesar Salad', 'Cobb Salad', 'Caprese Salad', 'Spinach Salad',
        'Mixed Green Salad', 'Taco Salad', 'Chicken Avocado Salad', 'Pasta Salad', 'Potato Salad', 'Tuna Salad',
        'Waldorf Salad', 'Cranberry Walnut Salad', 'Vegan Caesar Salad', 'Gluten-Free Salad',
        'Kale Salad', 'Quinoa Salad', 'Asian Chicken Salad', 'Arugula Salad', 'Beet Salad', 'Fattoush Salad',
        'Chickpea Salad', 'Niçoise Salad', 'Chopped Salad', 'Apple Walnut Salad', 'Black Bean Salad', 'Lentil Salad'
    ],
    'Sandwiches': [
        'BLT', 'Club Sandwich', 'Grilled Cheese', 'Philly Cheesesteak', 'Pulled Pork Sandwich', 'Turkey Sandwich',
        'Roast Beef Sandwich', 'Egg Salad Sandwich', 'Veggie Sandwich (Vegan)', 'Ham and Cheese Sandwich',
        'Meatball Sub', 'PB&J', 'Cubano', 'Reuben', 'Italian Sub', 'Gluten-Free Sandwich', 'Caprese Sandwich',
        'Chicken Salad Sandwich', 'Tuna Melt', 'French Dip', 'Banh Mi', 'Pastrami Sandwich', 'Falafel Sandwich',
        'Avocado Sandwich', 'Hummus Sandwich', 'Steak Sandwich', 'Tofu Sandwich (Vegan)', 'Smoked Salmon Sandwich'
    ],
    'Smoothies': [
        'Strawberry Smoothie', 'Banana Smoothie', 'Blueberry Smoothie', 'Mango Smoothie', 'Peanut Butter Smoothie',
        'Green Smoothie', 'Detox Smoothie', 'Acai Smoothie', 'Energy Smoothie', 'Raspberry Smoothie',
        'Chocolate Banana Smoothie', 'Carrot Smoothie', 'Kale Smoothie', 'Vegan Smoothie', 'Gluten-Free Smoothie',
        'Pineapple Smoothie', 'Protein Smoothie', 'Strawberry Banana Smoothie', 'Tropical Smoothie',
        'Chocolate Protein Smoothie', 'Cherry Almond Smoothie', 'Citrus Smoothie', 'Peach Smoothie',
        'Watermelon Smoothie', 'Apple Smoothie', 'Cucumber Smoothie', 'Spinach Smoothie'
    ],
    'Soups': [
        'Chicken Noodle Soup', 'Tomato Soup', 'Minestrone', 'French Onion Soup', 'Clam Chowder', 'Lentil Soup',
        'Butternut Squash Soup', 'Pho', 'Potato Soup', 'Ramen', 'Gazpacho', 'Broccoli Cheddar Soup',
        'Cream of Mushroom Soup', 'Split Pea Soup', 'Vegetable Soup (Vegan)', 'Wonton Soup', 'Beef Stew',
        'Gluten-Free Soup', 'Chicken Tortilla Soup', 'Egg Drop Soup', 'Miso Soup', 'Carrot Ginger Soup',
        'Black Bean Soup', 'Cauliflower Soup', 'Pumpkin Soup', 'Corn Chowder', 'Italian Wedding Soup',
        'Zucchini Soup', 'Seafood Bisque'
    ],
    'Spaghetti carbonara': [
        'Classic Spaghetti Carbonara', 'Spaghetti Carbonara with Bacon', 'Spaghetti Carbonara with Peas',
        'Spaghetti Carbonara with Sausage', 'Spicy Spaghetti Carbonara', 'Vegetarian Carbonara (Vegan)',
        'Gluten-Free Carbonara', 'Spaghetti Carbonara with Chicken', 'Spaghetti Carbonara with Ham',
        'Spaghetti Carbonara with Mushrooms', 'Spaghetti Carbonara with Parmesan', 'Spaghetti Carbonara with Pancetta'
    ],
    'Sushi': [
        'California Roll', 'Spicy Tuna Roll', 'Dragon Roll', 'Rainbow Roll', 'Vegetable Roll (Vegan)',
        'Sushi Combo', 'Sushi Platter', 'Sushi Nigiri', 'Gluten-Free Sushi', 'Salmon Roll', 'Shrimp Tempura Roll',
        'Avocado Roll', 'Eel Roll', 'Philadelphia Roll', 'Crunchy Roll', 'Dynamite Roll', 'Spider Roll', 'Volcano Roll',
        'Yellowtail Roll', 'Toro Roll'
    ],
    'Tacos': [
        'Beef Tacos', 'Chicken Tacos', 'Fish Tacos', 'Shrimp Tacos', 'Pork Tacos', 'Vegetarian Tacos (Vegan)',
        'Spicy Tacos', 'Steak Tacos', 'Gluten-Free Tacos', 'Carnitas Tacos', 'Barbacoa Tacos', 'Chorizo Tacos',
        'Tofu Tacos (Vegan)', 'Breakfast Tacos', 'Grilled Vegetable Tacos', 'Baja Fish Tacos', 'Al Pastor Tacos',
        'Cheese Tacos', 'Lamb Tacos', 'Duck Tacos'
    ],
    'Tofu stir-fry': [
        'Classic Tofu Stir-Fry (Vegan)', 'Tofu and Broccoli Stir-Fry (Vegan)', 'Tofu and Vegetable Stir-Fry (Vegan)',
        'Tofu and Mushroom Stir-Fry (Vegan)', 'Tofu Stir-Fry with Garlic Sauce (Vegan)', 'Tofu Stir-Fry with Cashews',
        'Tofu Stir-Fry with Black Bean Sauce', 'Tofu Stir-Fry with Teriyaki Sauce', 'Gluten-Free Tofu Stir-Fry',
        'Spicy Tofu Stir-Fry (Vegan)', 'Sweet and Sour Tofu Stir-Fry', 'General Tso’s Tofu Stir-Fry', 'Orange Tofu Stir-Fry'
    ],
    'Waffles': [
        'Classic Waffles', 'Belgian Waffles', 'Chocolate Chip Waffles', 'Blueberry Waffles', 'Fruit Waffles',
        'Protein Waffles', 'Vegan Waffles', 'Gluten-Free Waffles', 'Strawberry Waffles', 'Pumpkin Waffles',
        'Banana Waffles', 'Nutella Waffles', 'Cinnamon Waffles', 'Peanut Butter Waffles', 'Apple Cinnamon Waffles'
    ]
}
