import os
import json

if not (os.path.exists('./config')):
    os.mkdir('./config')
    cockroach = {
        'key': '',
        'url': ''
    }
    open_ai = {
        'key': ''
    }
    weaviate = {
        'key': '',
        'url': ''
    }
    with open('cockroach.json', 'w') as file:
        json.dump(cockroach, file)
    with open('open_ai.json', 'w') as file:
        json.dump(open_ai, file)
    with open('weaviate.json', 'w') as file:
        json.dump(weaviate, file)
    print('Created configs. Make sure to populate them')
