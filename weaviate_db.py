import os
import json
import time
import requests
from pprint import pprint

import weaviate
import weaviate.classes as wvc
from weaviate.classes.query import Filter, GroupBy, GeoCoordinate

from helper import *
from constants import *

class Weaviate:
    def __init__(self):
        weaviate_info = read_json(os.path.join(PATH_CONFIG, PATH_WEAVIATE_CONFIG))
        openai_info = read_json(os.path.join(PATH_CONFIG, PATH_OPEN_AI_CONFIG))
        self.client = weaviate.connect_to_wcs(
            cluster_url = weaviate_info['url'],
            auth_credentials = weaviate.auth.AuthApiKey(api_key = weaviate_info['key']),
            headers = {
                'X-OpenAI-Api-key': openai_info['key']
            }
        )
        self.client_v3 = weaviate.Client(
            url = weaviate_info['url'],
            auth_client_secret = weaviate.auth.AuthApiKey(api_key = weaviate_info['key']),
            additional_headers = {
                'X-OpenAI-Api-key': openai_info['key']
            }
        )

    def connection_status(self):
        return True if self.client.is_live() else False
    
    def close_connection(self):
        try:
            assert self.client.is_live()
            pass
        finally:
            self.client.close() 

    def get_cuisine_data(self, cusine, latitude = DEAFULT_LATITUDE, longitude = DEFAULT_LONGITUDE):
        try:
            response = (
                self.client_v3.query.get(
                    CRISPY_V1,
                    RETURN_PROPERTIES
                )
                .with_where({
                    'operator': 'And',
                    'operands': [{
                        'path': ['cleanedDishName'],
                        'operator': 'Like',
                        'valueText': f'*${cusine}*'
                    }]
                })
                .with_limit(WEAVIATE_LIMIT_200)
                .do()
            )
            return [i for i in response['data']['Get']['Crispy_v1_search_nyc']]
        except Exception as e:
            print(e)
            return []

    def get_restaurant_dish_data(self, restaurant_id, offset = 0):
        dish_id = set()
        dishes = []
        try:
            response = (
                self.client_v3.query.get(
                    CRISPY_V1,
                    RETURN_PROPERTIES_ALL
                )
                .with_where({
                    'operator': 'And',
                    'operands': [{
                        'path': ['restaurant_ID'],
                        'operator': 'Equal',
                        'valueText': restaurant_id
                    }]
                })
                .with_offset(int(offset * WEAVIATE_LIMIT_50))
                .with_limit(WEAVIATE_LIMIT_50)
                .do()
            )
            for dish in response['data']['Get']['Crispy_v1_search_nyc']:
                if (dish['dish_ID'] not in dish_id):
                    dish_id.add(dish['dish_ID'])
                    dishes.append(dish)
        except Exception as e:
            print(e)
        return dishes
    
    def get_dish_data(self, dish_id):
        try:
            collection = self.client.collections.get(CRISPY_V1)
            dish = collection.query.fetch_object_by_id(dish_id)
            return dish.properties
        except:
            return {}

    def get_dish_base(self, neighborhoods):
        try:
            response = (
                self.client_v3.query.get(
                    CRISPY_V1,
                    RETURN_PROPERTIES_ALL
                )
                .withWhere({
                    'operator': 'And',
                    'operands': [
                        {
                            'path': ['neighborhood'],
                            'operator': 'ContainsAny',
                            'valueTextArray': neighborhoods
                        },
                        {
                            'operator': 'Or',
                            'operands': [
                                {
                                    'path': ['stockImageUber'],
                                    'operator': 'Equal',
                                    'valueText': 'UniqueImage'
                                },
                                {
                                    'path': ['stockImageDoorDash'],
                                    'operator': 'Equal',
                                    'valueText': 'UniqueImage'
                                }
                            ]
                        },
                        {
                            'operator': 'Or',
                            'operands': [
                                {
                                    'path': ['dishType'],
                                    'operator': 'Like',
                                    'valueText': '*Lunch*',
                                },
                                {
                                    'path': ['dishType'],
                                    'operator': 'Like',
                                    'valueText': '*Dinner*',
                                },
                                {
                                    'path': ['dishType'],
                                    'operator': 'Like',
                                    'valueText': '*Breakfast*',
                                },
                                {
                                    'path': ['dishType'],
                                    'operator': 'Like',
                                    'valueText': '*Brunch*',
                                }
                                ,
                                {
                                    'path': ['dishType'],
                                    'operator': 'Like',
                                    'valueText': '*Snack*',
                                },
                                {
                                    'path': ['dishType'],
                                    'operator': 'Like',
                                    'valueText': '*Salad*',
                                },
                                {
                                    'path': ['dishType'],
                                    'operator': 'Like',
                                    'valueText': '*Dessert*'
                                },
                            ]
                        }
                    ]
                })
                .with_limit(WEAVIATE_LIMIT_1000)
                .do()
            )
            return response
        except Exception as e:
            print(e)
            return []

    def get_dish_combined(self, neighborhoods, diets, cuisines, popular_dishes):
        try:
            response = (
                self.client_v3.query.get(
                    CRISPY_V1,
                    RETURN_PROPERTIES_ALL
                )
                .withWhere({
                    'operator': 'And',
                    'operands': [
                        {
                            'path': ['neighborhood'],
                            'operator': 'ContainsAny',
                            'valueTextArray': neighborhoods
                        },
                        {
                            'operator': 'Or',
                            'operands': [
                                {
                                    'path': ['infatuation_ReviewDictVec'],
                                    'operator': 'NotEqual',
                                    'valueText': 'None'
                                },
                                {
                                    'path': ['eater_ReviewDictVec'],
                                    'operator': 'NotEqual',
                                    'valueText': 'None'
                                }
                            ]
                        },
                        {
                            'operator': 'Or',
                            'operands': [
                                {
                                    'path': ['stockImageUber'],
                                    'operator': 'Equal',
                                    'valueText': 'UniqueImage'
                                },
                                {
                                    'path': ['stockImageDoorDash'],
                                    'operator': 'Equal',
                                    'valueText': 'UniqueImage'
                                }
                            ]
                        },
                        {
                            'operator': 'Or',
                            'operands': [
                                {
                                    'path': ['dishType'],
                                    'operator': 'Like',
                                    'valueText': '*Lunch*',
                                },
                                {
                                    'path': ['dishType'],
                                    'operator': 'Like',
                                    'valueText': '*Dinner*',
                                },
                                {
                                    'path': ['dishType'],
                                    'operator': 'Like',
                                    'valueText': '*Breakfast*',
                                },
                                {
                                    'path': ['dishType'],
                                    'operator': 'Like',
                                    'valueText': '*Brunch*',
                                },
                                {
                                    'path': ['dishType'],
                                    'operator': 'Like',
                                    'valueText': '*Salad*',
                                },
                            ]
                        }
                    ]
                })
                .with_limit(WEAVIATE_LIMIT_1000)
                .do()
            )
            return response
        except Exception as e:
            print(e)
            return []
    
    def get_dish_cusine(self, neighborhoods, cuisines):
        try:
            response = (
                self.client_v3.query.get(
                    CRISPY_V1,
                    RETURN_PROPERTIES_ALL
                )
                .withWhere({
                    'operator': 'And',
                    'operands': [
                        {
                            'path': ['cleanedDishName'],
                            'operator': 'ContainsAny',
                            'valueTextArray': CURATED_CUISINES[cuisines]
                        },
                        {
                            'path': ['neighborhood'],
                            'operator': 'ContainsAny',
                            'valueTextArray': neighborhoods
                        },
                        {
                            'operator': 'Or',
                            'operands': [
                                {
                                'path': ["stockImageUber"],
                                'operator': 'Equal',
                                'valueText': "UniqueImage"
                                },
                                {
                                'path': ["stockImageDoorDash"],
                                'operator': 'Equal',
                                'valueText': "UniqueImage"
                                }
                            ]
                        },
                        {
                            'operator': "Or",
                            'operands': [
                                {
                                    'path': ["dishType"],
                                    'operator': "Like",
                                    'valueText': "*Lunch*",
                                },
                                {
                                    'path': ["dishType"],
                                    'operator': "Like",
                                    'valueText': "*Dinner*",
                                },
                                {
                                    'path': ["dishType"],
                                    'operator': "Like",
                                    'valueText': "*Breakfast*",
                                },
                                {
                                    'path': ["dishType"],
                                    'operator': "Like",
                                    'valueText': "*Brunch*",
                                },
                                {
                                    'path': ["dishType"],
                                    'operator': "Like",
                                    'valueText': "*Snack*",
                                },
                                {
                                    'path': ["dishType"],
                                    'operator': "Like",
                                    'valueText': "*Salad*",
                                },
                                {
                                    'path': ["dishType"],
                                    'operator': "Like",
                                    'valueText': "*Dessert*"
                                }
                            ]
                        }
                    ]
                })
                .with_limit(WEAVIATE_LIMIT_1000)
                .do()
            )
            return response
        except Exception as e:
            print(e)
            return []

    def get_dish_diets(self, neighborhoods, diets):
        try:
            response = (
                self.client_v3.query.get(
                    CRISPY_V1,
                    RETURN_PROPERTIES_ALL
                )
                .withWhere({
                    'operator': 'And',
                    'operands': [
                        {
                            'path': ['neighborhood'],
                            'operator': 'ContainsAny',
                            'valueTextArray': neighborhoods
                        },
                        {
                            'path': ['cleanedDishName'],
                            'operator': 'ContainsAny',
                            'valueTextArray': CURATED_DIETS[diets]
                        },
                        {
                            'operator': 'Or',
                            'operands': [
                                {
                                    'path': ['stockImageUber'],
                                    'operator': 'Equal',
                                    'valueText': 'UniqueImage'
                                },
                                {
                                    'path': ['stockImageDoorDash'],
                                    'operator': 'Equal',
                                    'valueText': 'UniqueImage'
                                }
                            ]
                        },
                        {
                            'operator': 'Or',
                            'operands': [
                                {
                                    'path': ['dishType'],
                                    'operator': 'Like',
                                    'valueText': '*Lunch*',
                                },
                                {
                                    'path': ['dishType'],
                                    'operator': 'Like',
                                    'valueText': '*Dinner*',
                                },
                                {
                                    'path': ['dishType'],
                                    'operator': 'Like',
                                    'valueText': '*Breakfast*',
                                },
                                {
                                    'path': ['dishType'],
                                    'operator': 'Like',
                                    'valueText': '*Brunch*',
                                },
                                {
                                    'path': ['dishType'],
                                    'operator': 'Like',
                                    'valueText': '*Snack*',
                                },
                                {
                                    'path': ['dishType'],
                                    'operator': 'Like',
                                    'valueText': '*Salad*',
                                },
                                {
                                    'path': ['dishType'],
                                    'operator': 'Like',
                                    'valueText': '*Dessert*'
                                }
                            ]
                        }
                    ]
                })
                .with_limit(WEAVIATE_LIMIT_1000)
                .do()
            )
            return response
        except Exception as e:
            print(e)
            return []

if __name__ == '__main__':
    wv = Weaviate()
    # res = wv.get_dish_data('bafd7ba5-344b-4fb9-9b2f-a02d5e54f1c4')
    # res = wv.get_rez_data('pizza')
    res = wv.get_dish_base('SoHo')
    pprint((res))
    # ids = []
    # for item in res:
    #     ids.append(item['dishRes_ID'])
    # print(len(ids))
    # print(len(set(ids)))
