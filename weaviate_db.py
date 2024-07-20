import os
import json
import time
import random
import requests
from pprint import pprint

import weaviate
import weaviate.classes as wvc
from weaviate.classes.query import Filter, GroupBy, GeoCoordinate

from helper import *
from constants import *

class Weaviate:
    def __init__(self):
        if (os.path.exists(PATH_CONFIG)):
            weaviate_info = read_json(os.path.join(PATH_CONFIG, PATH_WEAVIATE_CONFIG))
            weavate_key = weaviate_info['key']
            weaviate_url = weaviate_info['url']
            openai_info = read_json(os.path.join(PATH_CONFIG, PATH_OPEN_AI_CONFIG))
            openai_key = openai_info['key']
        else:
            weavate_key = os.getenv('WEAVIATE_KEY')
            weaviate_url = os.getenv('WEAVIATE_URL')
            openai_key = os.getenv('OPENAI_KEY')

        self.client = weaviate.connect_to_wcs(
            cluster_url = weaviate_url,
            auth_credentials = weaviate.auth.AuthApiKey(api_key = weavate_key),
            headers = {
                'X-OpenAI-Api-key': openai_key
            }
        )
        self.client_v3 = weaviate.Client(
            url = weaviate_url,
            auth_client_secret = weaviate.AuthApiKey(api_key = weavate_key),
            additional_headers = {
                'X-OpenAI-Api-key': openai_key
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

    def get_master_dish_static(self):
        data = []
        collection = self.client.collections.get('MasterGoogleFile3')
        try:
            for item in collection.iterator():
                data.append(item.properties)
            return data
        except Exception as e:
            print(e)
            return []
    
    def get_cuisine_static(self):
        collection = self.client.collections.get('GoogleCuisineFinal2')
        try:
            response = collection.query.fetch_objects()
            return [i.properties for i in response.objects]
        except Exception as e:
            print(e)
            return []

    def get_diets_static(self):
        collection = self.client.collections.get('GoogleDietFinal2')
        try:
            response = collection.query.fetch_objects()
            return [i.properties for i in response.objects]
        except Exception as e:
            print(e)
            return []

    def get_popular_dish_static(self):
        collection = self.client.collections.get('GooglePopularDishesFinal2')
        try:
            response = collection.query.fetch_objects()
            return [i.properties for i in response.objects]
        except Exception as e:
            print(e)
            return []

    def get_restaurant_data_hours(self, restaurant_id):
        collection = self.client.collections.get(CRISPY_V1)
        try:
            response = collection.query.bm25(
                query = restaurant_id,
                limit = WEAVIATE_LIMIT_1,
                return_properties = RETURN_PROPERTIES_HOURS
            )
            return response.objects[0].properties
        except Exception as e:
            print(e)
            return {}

    def get_cuisine_data(self, cusine, latitude = DEFAULT_LATITUDE, longitude = DEFAULT_LONGITUDE, offset = 0):
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
                .with_limit(WEAVIATE_LIMIT_100)
                .with_offset(int(WEAVIATE_LIMIT_100 * offset))
                .do()
            )
            return [i for i in response['data']['Get']['Crispy_v1_search_nyc']]
        except Exception as e:
            print(e)
            return []

    def _get_all_properties(self, item):
        item.properties['_additional'] = {'id': item.uuid}
        return item.properties
    def get_restaurant_dish_data(self, restaurant_id, offset = 0):
        collection = self.client.collections.get(CRISPY_V1)
        try:
            response = collection.query.bm25(
                query = restaurant_id,
                offset = int(offset * WEAVIATE_LIMIT_50),
                limit = WEAVIATE_LIMIT_50,
                group_by = GroupBy(
                    prop = 'dishRes_ID',
                    objects_per_group = 1,
                    number_of_groups = WEAVIATE_LIMIT_50
                )
            )
            return [self._get_all_properties(item) for item in response.objects]
        except Exception as e:
            print(e)
            return []
    
    def get_dish_data(self, dish_id):
        try:
            collection = self.client.collections.get(CRISPY_V1)
            dish = collection.query.fetch_object_by_id(dish_id)
            dish.properties['_additional'] = {'id': dish_id}
            return dish.properties
        except:
            return {}

    def get_dish_base(self, neighborhoods, offset = 0):
        neighborhoods = str_to_list(neighborhoods)
        try:
            response = (
                self.client_v3.query.get(
                    CRISPY_V1,
                    RETURN_PROPERTIES_ALL
                )
                .with_where({
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
                .with_limit(WEAVIATE_LIMIT_50)
                .with_offset(int(WEAVIATE_LIMIT_50 * offset))
                .do()
            )
            return response
        except Exception as e:
            print(e)
            return []

    def get_dish_combined(self, neighborhoods, offset = 0):
        neighborhoods = str_to_list(neighborhoods)
        try:
            response = (
                self.client_v3.query.get(
                    CRISPY_V1,
                    RETURN_PROPERTIES_V3
                )
                .with_where({
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
                .with_limit(WEAVIATE_LIMIT_50)
                .with_offset(int(WEAVIATE_LIMIT_50 * offset))
                .do()
            )
            return response
        except Exception as e:
            print(e)
            return []
    
    def get_dish_cuisine(self, neighborhoods, cuisines, offset = 0):
        neighborhoods = str_to_list(neighborhoods)
        try:
            response = (
                self.client_v3.query.get(
                    CRISPY_V1,
                    RETURN_PROPERTIES_V3
                )
                .with_where({
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
                .with_limit(WEAVIATE_LIMIT_50)
                .with_offset(int(WEAVIATE_LIMIT_50 * offset))
                .do()
            )
            return response
        except Exception as e:
            print(e)
            return []

    def get_dish_diets(self, neighborhoods, diets, offset = 0):
        neighborhoods = str_to_list(neighborhoods)
        diets = diets.lower()
        try:
            response = (
                self.client_v3.query.get(
                    CRISPY_V1,
                    RETURN_PROPERTIES_V3
                )
                .with_where({
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
                .with_limit(WEAVIATE_LIMIT_50)
                .with_offset(int(WEAVIATE_LIMIT_50 * offset))
                .do()
            )
            return response
        except Exception as e:
            print(e)
            return []

    def get_dish_popular(self, neighborhoods, dishes, offset = 0):
        neighborhoods = str_to_list(neighborhoods)
        dishes = dishes.lower()
        try:
            response = (
                self.client_v3.query.get(
                    CRISPY_V1,
                    RETURN_PROPERTIES_V3
                )
                .with_where({
                    'operator': 'And',
                    'operands': [
                        {
                            'path': ['cleanedDishName'],
                            'operator': 'ContainsAny',
                            'valueTextArray': ['acai'] if dishes == 'açaí bowls' else CURATED_DISHES['breakfasts'] if dishes == 'breakfasts' else [dishes]
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
                .with_limit(WEAVIATE_LIMIT_50)
                .with_offset(int(WEAVIATE_LIMIT_50 * offset))
                .do()
            )
            return response
        except Exception as e:
            print(e)
            return []

    def _get_elastic_search(self, where_filter, weaviate_limit = 10):
        try:
            response = (
                self.client_v3.query.get(CRISPY_V1, RETURN_PROPERTIES_V2)
                .with_additional(['id', 'distance'])
                .with_where(where_filter)
                .with_limit(weaviate_limit)
                .do()
            )
            return response['data']['Get'][CRISPY_V1]
        except Exception as err:
            print(err)
            return []

    def _get_vector_search(self, search_term, where_filter, weaviate_limit = 10):
        try:
            response = (
                self.client_v3.query.get(CRISPY_V1, RETURN_PROPERTIES_V2)
                .with_near_text({'concepts': [search_term]})
                .with_additional(['id', 'distance'])
                .with_where(where_filter)
                .with_limit(weaviate_limit)
                .do()
            )
            return response['data']['Get'][CRISPY_V1]
        except Exception as err:
            print(err)
            return []
        
    def get_single_dish_search(self, dish, neighborhoods = None, has_unique_image = False, weaviate_limit = 10, latitude = DEFAULT_LATITUDE, longitude = DEFAULT_LONGITUDE, offset = 0):
        if not dish:
            return []
        wv_filter = build_where_filter(dish, neighborhoods, has_unique_image)

        elastic_resp = self._get_elastic_search(wv_filter, weaviate_limit)
        vector_resp = self._get_vector_search(dish, wv_filter, weaviate_limit)

        unique_dish_res_ids = set()
        unique_dishes = []

        def add_unique_dishes(dishes):
            for dish in dishes:
                if (dish['dishRes_ID'] not in unique_dish_res_ids):
                    unique_dish_res_ids.add(dish['dishRes_ID'])
                    unique_dishes.append(dish)

        if (len(elastic_resp) <= 8):
            add_unique_dishes(vector_resp)
            add_unique_dishes(elastic_resp)
        else:
            half_length = len(vector_resp) // 2
            half_vector_response = vector_resp[:half_length]
            add_unique_dishes(elastic_resp)
            add_unique_dishes(half_vector_response)

        return unique_dishes

    def get_dish_data_ios(self, search_term: str, weaviate_limit: int, neighborhoods: Optional[List[str]] = None, has_unique_image: bool = False) -> List[Dict]:
        if not search_term:
            return []

        wv_filter = build_where_filter(search_term, neighborhoods, has_unique_image)

        elastic_resp = self._get_elastic_search(wv_filter, weaviate_limit)
        vector_resp = self._get_vector_search(search_term, wv_filter, weaviate_limit)

        if len(elastic_resp) <= 8:
            return vector_resp + elastic_resp
        else:
            half_length = len(vector_resp) // 2
            half_vector_response = vector_resp[:half_length]
            return elastic_resp + half_vector_response
    
    def combine_alternatives_ios(self, dishes: List[Dict], max_alternatives: int) -> Set[str]:
        alternatives = set()
        count = 0
        for dish in dishes:
            if (count >= max_alternatives):
                break
            for key in ['specificBaseAlternatives', 'alternativesWithinSameCuisine', 'healthAlternatives']:
                if (key in dish and dish[key] and dish[key] != 'None'):
                    alternatives.update(dish[key].strip('[]').replace("'", "").split(', '))
                    count += len(dish[key].strip('[]').replace("'", "").split(', '))
            if (count >= max_alternatives):
                break
        return set(list(alternatives)[:max_alternatives])
    
    def get_alternative_dish_data_ios(self, alternatives: Set[str], weaviate_limit: int, neighborhoods: Optional[List[str]], has_unique_image: bool) -> Dict:
        alternative_data = {}
        for alt in alternatives:
            data = self.get_dish_data_ios(
                alt,
                weaviate_limit,
                neighborhoods = neighborhoods,
                has_unique_image = has_unique_image,
            )
            alternative_data[alt] = data
        return alternative_data

    def combine_alternatives(self, dishes: List[Dict], max_alternatives: int) -> List[str]:
        alternatives = []
        count = 0
        for dish in dishes:
            if (count >= max_alternatives):
                break
            for key in ['specificBaseAlternatives', 'alternativesWithinSameCuisine', 'healthAlternatives',]:
                if (key in dish and dish[key] and dish[key] != 'None'):
                    alternatives.extend(dish[key].strip('[]').replace("'", '').split(', '))
                    count += len(dish[key].strip('[]').replace("'", '').split(', '))
                if count >= max_alternatives:
                    break
        return list(set(alternatives[:max_alternatives]))

    def get_alternative_dish_data(self, alternatives, neighborhoods = None, has_unique_image = False, weaviate_limit = 10, latitude = DEFAULT_LATITUDE, longitude = DEFAULT_LONGITUDE, offset = 0):
        alternative_data = []
        for alt in alternatives:
            data = self.get_single_dish_search(alt, neighborhoods, has_unique_image, weaviate_limit, latitude, longitude, offset)
            alternative_data.extend(data)
        return alternative_data

    def get_search_dishes(
            self, 
            query_type: str, 
            query_value: str, 
            neighborhoods: List[str] = None, 
            has_unique_image: bool = False, 
            weaviate_limit: int = 10,
            max_alternatives: int = 9,
            num_dishes: int = 10,
            latitude = DEFAULT_LATITUDE,
            longitude = DEFAULT_LONGITUDE,
            offset: int = 0,
        ):
        if (query_type == 'cuisine'): dishes = CURATED_CUISINES.get(query_value.lower(), [])
        elif (query_type == 'diet'): dishes = CURATED_DIETS.get(query_value.lower(), [])
        elif (query_type == 'popular'): dishes = CURATED_DISHES.get(query_value.lower(), [])
        else: return None

        combined_results = {}
        for dish in random.sample(dishes, min(num_dishes, len(dishes))):
            dish_results = self.get_single_dish_search(dish, neighborhoods, has_unique_image, weaviate_limit, latitude, longitude, offset)
            alternatives = self.combine_alternatives(dish_results, max_alternatives)
            alternative_data = self.get_alternative_dish_data(alternatives, neighborhoods, has_unique_image, weaviate_limit, latitude, longitude, offset)
            combined_results[dish] = dish_results + alternative_data

        return combined_results

if __name__ == '__main__':
    wv = Weaviate()
    # res = wv.get_dish_data('bafd7ba5-344b-4fb9-9b2f-a02d5e54f1c4')
    # res = wv.get_cuisine_data('pizza')
    # res = wv.get_restaurant_dish_data('b91041')
    # res = wv.get_dish_diets('MORNINGSIDE%20HEIGHTS', 'High%20Protein')
    res = wv.get_master_dish_static()
    # res = wv.get_restaurant_data_hours('03d267')
    pprint(len(res))
    # ids = []
    # for item in res:
    #     ids.append(item['dishRes_ID'])
    # print(len(ids))
    # print(len(set(ids)))
