WEAVIATE_LIMIT_50 = 50
WEAVIATE_LIMIT_200 = 200
WEAVIATE_LIMIT_1000 = 1000
DEAFULT_LATITUDE = 40.720800
DEFAULT_LONGITUDE = -73.978940

DISTANCE_MILES = {
    1: 1609.34
}

DISTANCE_KM = {
    1: 1000
}

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

    'eater_ReviewDictVec',
    'infatuation_ReviewDictVec',
  ]
CURATED_CUISINES = {
    'american': [
        'Buffalo Wings', 'BBQ Spare Ribs', 'Pulled Pork Sandwich', 'Sausage Egg Cheese Biscuit',
        'Clam Chowder', 'Scrambled Eggs', 'Fruit Salad', 'Pastrami Sandwich', 'Omelette', 'Cobb Salad',
        'Apple Pie', 'Cinnamon Bun', 'Hot Dog', 'Fried Chicken', 'Pot Pie', 'Mashed Potatoes', 'Pancakes',
        'Grilled Cheese Sandwich', 'BLT Sandwich', 'BBQ Ribs', 'Shashlik', 'Chili soup', 'Pancake Stack',
        'French Toast', 'Club Sandwich', 'Greek Yogurt Parfait', 'Pumpkin Soup', 'Breakfast Sandwich',
        'Shrimp and Grits', 'Blueberry Muffins', 'Eggs and Bacon', 'Crab Cake', 'Cheeseburger',
        'Peanut Butter Jelly', 'S\'mores', 'Brisket', 'Chicken and Waffles', 'Eggs Benedict', 'Cornbread',
        'Meatloaf', 'Hamburger', 'Chicken Tenders', 'Ribeye Steak', 'Korean Chicken Wings', 'Bacon and Eggs',
        'Chicken Wings', 'Beef Patty', 'New York Strip Steak', 'Pulled Pork', 'Filet Mignon', 'Bison',
        'Beef Ribs', 'Fried Pork Chops', 'Pork Belly', 'Pork Ribs', 'Grilled Chicken Breast', 'Roasted Turkey Breast',
        'Grilled Pork Chops', 'Baked Potato', 'Turkey Wraps', 'Gluten-Free Caesar Salad', 'Grilled Pork Tenderloin',
        'Tofu With Mixed Vegetables', 'Cauliflower Stir Fried', 'Gluten Free Fried Rice', 'Shrimp Stir Fry',
        'Gluten-Free Tofu Skewers', 'Sesame Tofu Stir Fry', 'Chicken With Mixed Vegetables', 'Quinoa Salad',
        'Spinach and Mushroom Omelette', 'Gluten Free Chow Mein', 'Beef and Broccoli Stir Fry', 'Gluten-Free Tofu Fried Rice',
        'Cauliflower Pizza Crust', 'Quinoa Salad', 'Gluten-Free Cauliflower Manchurian', 'Grilled Shrimp Salad',
        'Grilled Asparagus', 'Shrimp Kebab', 'Gluten-Free Pizza', 'Gluten-Free Pasta with Sauce', 'Mushroom Risotto',
        'Grilled Chicken Caesar Salad', 'Caprese Salad', 'Grilled Vegetable Frittata', 'Gluten-Free Frittata',
        'Cucumber Avocado Sushi Rolls', 'Teriyaki Glazed Fish', 'Teriyaki Glazed Chicken', 'Mediterranean Salad',
        'Grilled Lamb Kebabs with Yogurt Sauce', 'Chickpea Salad', 'Shrimp Tacos', 'Vegetarian Chilli',
        'Gluten-Free Fajita Bowl with Chicken', 'Gluten-free Fajita Bowl with Veggies', 'Gluten-Free Shrimp Tacos',
        'Gluten-Free Chili', 'Gluten-Free Spiced Pilaf', 'Avocado Salad', 'Grilled Salmon', 'Baked Salmon with Gluten Free Sauce',
        'Baked Cod with Gluten Free Sauce', 'Grilled Swordfish with Sauce', 'Sautéed Shrimp with Garlic', 'Thai Curry',
        'Chicken Lettuce Wrap', 'Steamed Mixed Vegetables', 'Eggs and Avocado', 'Baked Chicken', 'Vegetable Soup',
        'Grilled Steak with Gluten Free Sauce', 'Sautéed Spinach with Garlic', 'Veggie Gluten Free Wraps',
        'Salmon and Asparagus', 'Baked Halibut', 'Gluten-Free Avocado Toast', 'Grilled Portobello Mushrooms',
        'Grilled Vegetable Skewers', 'Gluten-Free Cauliflower Tenders', 'Gluten-Free Cauliflower', 'Roasted Brussels Sprouts',
        'Caesar Salad', 'Turkey Sandwich', 'Avocado Toast', 'Grilled Chicken Salad', 'Grilled Chicken Bowl',
        'Grilled Chicken Sandwich', 'Tomato Soup', 'Breakfast Sandwich', 'Buffalo Roasted Cauliflower', 'Baked Potato',
        'Kale and Apple Salad', 'Stir Fry Veggies with Tofu', 'Stir Fry Veggies', 'Stir Fry Veggies with Chicken',
        'Vegetable Noodle Soup', 'Beef Stir-Fry', 'Green Juice', 'Acai Bowls', 'Overnight Oats with Fruit',
        'Garlic String Beans', 'Roasted Veggies', 'Poke Bowl', 'Green Smoothie', 'Yogurt Parfait with Fruits',
        'Quinoa Salad', 'Minestrone Soup', 'Thin Crust Pizza', 'Sushi', 'Onigiri', 'Greek Salad',
        'Mediterranean Bowl', 'Breakfast Burrito', 'Burrito Bowl', 'Taco Salad', 'Falafel Wrap', 'Hummus and Pita',
        'Veggie Sandwich', 'Scrambled Eggs', 'Poached Eggs', 'Omelette', 'Tofu and Rice', 'Fruit Salad',
        'Chicken Noodle Soup', 'Grilled Chicken Nuggets', 'Vegan Chicken Nuggets', 'Chia Pudding',
        'Spaghetti Squash', 'Grilled Veggie Platter', 'Black Bean Sandwich', 'Banh Mi', 'Fish and Rice'
    ],
    'argentinian': [
        'Milanesa', 'Asado', 'Parrillada', 'Napolitana Pizza'
    ],
    'australian': [
        'Meat Pie', 'Macadamia Cookie'
    ],
    'brazilian': [
        'Coxinha', 'Tapioca', 'Açaí Bowl', 'Cachorro-Quente', 'Empada', 'Brigadeiro', 'Moqueca',
        'Pastel', 'Picanha'
    ],
    'british': [
        'Fish and Chips', 'Full Breakfast', 'Bread Pudding'
    ],
    'cajun': [
        'Shrimp Grits', 'Cajun Shrimp', 'Cajun Boil', 'Fried Catfish', 'Red Snapper Fish', 'Crawfish',
        'Shrimp Po\' Boy'
    ],
    'caribbean': [
        'Breadfruit', 'Callaloo', 'Rum Punch', 'Jerk Chicken', 'Rice and Peas'
    ],
    'chinese': [
        'Shanghai Noodle', 'Baozi (Steamed Buns)', 'Sweet and Sour Pork', 'Sesame Chicken', 'Char Siu (BBQ Pork)',
        'General Tso\'s Chicken', 'Moo Shu', 'Moo Shu Pork', 'Mongolian Beef', 'Lo Mein', 'Hot and Sour Soup',
        'Scallion Pancakes', 'Roast Duck', 'Chicken With Cashew Nuts', 'Orange Chicken', 'Peking Duck',
        'Kung Pao Chicken', 'Dim Sum', 'Egg Drop Soup', 'Chicken With Black Bean Sauce', 'Szechuan Chicken',
        'Wonton Soup', 'Chow Mein', 'Fried Rice', 'Steamed Dumplings', 'Buddha\'s Delight (Jai)', 'Hot Pot',
        'Hot And Sour Soup', 'Xiao Long Bao (Soup Dumplings)', 'Sticky Rice in Lotus Leaf'
    ],
    'ethiopian': [
        'Lamb Stew'
    ],
    'french': [
        'Chocolate Mousse', 'Quiche Lorraine', 'Croissant', 'Sole Fish', 'Crepes', 'French Onion Soup',
        'Crème Brûlée', 'Salade Niçoise'
    ],
    'fusion': [
        'California Roll Burrito'
    ],
    'german': [
        'Sour Cabbage', 'Beef Roll', 'Grilled Sausage', 'Potato Salad', 'Potato Pancake', 'Wurst',
        'Potato Soup', 'Stuffed Cabbage', 'Liverwurst'
    ],
    'greek': [
        'Tzatziki', 'Moussaka', 'Feta Dip', 'Spanakopita', 'Kufta', 'Lamb Gyros', 'Pastitsio Pasta',
        'Greek Salad', 'Stuffed Peppers', 'Chicken Gyro', 'Avgolemono Soup', 'Spanakopita Spinach Pie'
    ],
    'hawaiian': [
        'Spam Musubi', 'Poke Bowl'
    ],
    'indian': [
        'Kulfi', 'Malai Kofta', 'Rasmalai', 'Rogan Josh', 'Tikka Masala', 'Chole Bhature', 'Dal Makhani',
        'Roti', 'Kheer', 'Paneer Tikka', 'Butter Naan', 'Mango Lassi', 'Gulab Jamun', 'Bhindi Masala',
        'Biryani', 'Pulao', 'Fish Curry', 'Keema Naan', 'Tandoori Roti', 'Chana Masala', 'Raita',
        'Pav Bhaji', 'Aloo Gobi', 'Indian Butter Chicken', 'Chapati', 'Chaat', 'Pakora', 'Vada Pav',
        'Baingan Bharta', 'Samosa', 'Mutton Masala', 'Chicken Tikka Masala', 'Pani Puri', 'Tandoori Chicken',
        'Aloo Paratha'
    ],
    'italian': [
        'Amatriciana', 'Polpette', 'Rigatoni Alla Carbonara', 'Linguini Con Vongole', 'Eggplant Parmigiana',
        'Ossobuco', 'Chicken Parmesan', 'Cacio E Pepe', 'Gelato', 'Panna Cotta', 'Caprese Salad',
        'Gnocchi', 'Margherita Pizza', 'Lasagna', 'Tiramisu', 'Pasta Carbonara', 'Spaghetti Bolognese',
        'Risotto', 'Lobster Fra Diavolo', 'Minestrone Soup', 'Fettuccine Alfredo', 'Bruschetta',
        'Arancini'
    ],
    'japanese': [
        'Gyoza', 'Katsu', 'Sashimi', 'Udon', 'Tamagoyaki', 'Chashu Pork', 'Miso Soup', 'Unagi',
        'Japanese Pickles', 'Sushi', 'Karaage', 'Takoyaki', 'Ramen', 'Onigiri', 'Matcha Green Tea',
        'Matcha Ice Cream', 'Yakisoba', 'Okonomiyaki', 'Katsudon'
    ],
    'korean': [
        'Kimchi', 'Bulgogi', 'Bibimbap', 'Galbi', 'Japchae', 'Kimchi Stew', 'Korean BBQ', 'Pajeon',
        'Sundubu Jjigae', 'Soondae', 'Tteokbokki', 'Jajangmyeon', 'Dak Galbi', 'Korean Fried Chicken'
    ],
    'latin_american': [
        'Chicken Empanada', 'Arepa', 'Beef Empanada', 'Tamale'
    ],
    'lebanese': [
        'Hummus', 'Lamb Chops', 'Falafel', 'Lebanese Lentils', 'Labneh'
    ],
    'mediterranean': [
        'Baklava', 'Couscous', 'Fish with Herb Sauce'
    ],
    'mexican': [
        'Nachos', 'Tacos', 'Fajitas', 'Chiles Rellenos', 'Carne Asada', 'Taco Salad', 'Enchiladas',
        'Margarita', 'Quesadillas', 'Churros', 'Guacamole', 'Burritos', 'Huevos Rancheros', 'Tostada',
        'Salsa', 'Tamales', 'Taquitos', 'Sopaipillas'
    ],
    'middle_eastern': [
        'Lamb Kebab', 'Beef Shawarma', 'Hummus', 'Chicken Shawarma', 'Shish Kebab', 'Chicken Kebab', 'Baklava'
    ],
    'moroccan': [
        'Lamb Tagine', 'Couscous', 'Chicken Tagine'
    ],
    'nigerian': [
        'Jollof Rice', 'Fried Plantains', 'Egusi Soup', 'Fufu'
    ],
    'peruvian': [
        'Ceviche'
    ],
    'portuguese': [
        'Pastel De Nata', 'Bacalhau A Bras', 'Grilled Sardines', 'Portuguese Egg Tarts', 'Piri Piri Chicken'
    ],
    'spanish': [
        'Gazpacho', 'Patatas Bravas', 'Churros', 'Tortilla Española', 'Gambas Al Ajillo', 'Paella',
        'Jamon Iberico', 'Flan', 'Sangria', 'Serrano Ham', 'Pulpo A La Gallega', 'Croquetas'
    ],
    'swedish': [
        'Swedish Meatballs', 'Gravadlax', 'Lingonberry Jam'
    ],
    'thai': [
        'Pad Thai', 'Red Curry', 'Green Curry', 'Mango Sticky Rice', 'Thai Iced Tea', 'Thai Fish Cakes',
        'Tom Yum Soup', 'Papaya Salad', 'Massaman Curry', 'Basil Chicken', 'Larb', 'Yellow Curry'
    ],
    'turkish': [
        'Turkish Delight', 'Lamb Doner Kebab', 'Chicken Doner Kebab', 'Turkish Coffee', 'Pide', 'Lahmacun',
        'Baklava', 'Kofte', 'Adana Kebab'
    ],
    'vietnamese': [
        'Pho', 'Banh Mi', 'Goi Cuon', 'Bun Cha', 'Vietnamese Iced Coffee', 'Bun Bo Hue', 'Spring Rolls',
        'Com Tam', 'Nem Ran'
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
      'Eggplant Lasagna', 'Caprese Salad', 'Grilled Salmon with Asparagus'
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
