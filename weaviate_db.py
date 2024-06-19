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
            .with_limit(WEAVIATE_LIMIT)
            .do()
        )
        return [i for i in response['data']['Get']['Crispy_v1_search_nyc']]

    def get_restaurant_dish_data(self, restaurant_id):
        collection = self.client.collections.get(CRISPY_V1)
        try:
            response = collection.query.bm25(
                query = restaurant_id,
                limit = WEAVIATE_LIMIT,
                group_by = GroupBy(
                    prop = 'dishRes_ID',
                    objects_per_group = 1,
                    number_of_groups = WEAVIATE_LIMIT
                )
            )
            return [i.properties for i in response.objects]
        except Exception as e:
            return []

if __name__ == '__main__':
    wv = Weaviate()
    res = wv.get_rez_data('d122ea')
    # res = wv.get_rez_data('pizza')
    pprint((res))
    # ids = []
    # for item in res:
    #     ids.append(item['dishRes_ID'])
    # print(len(ids))
    # print(len(set(ids)))
