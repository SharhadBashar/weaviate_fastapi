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
    google = {
        'client_id': '',
        'reversed_client_id': '',
        'api_key': '',
        'gcm_sender_id': '',
        'plist_version': '',
        'bundle_id': '',
        'project_id': '',
        'storage_bucket': '',
        'is_ads_enabled': False,
        'is_analytics_enabled': False,
        'is_appinvite_enabled': False,
        'is_gcm_enabled': False,
        'is_signin_enabled': False,
        'google_app_id': ''
    }
    with open('cockroach.json', 'w') as file:
        json.dump(cockroach, file)
    with open('open_ai.json', 'w') as file:
        json.dump(open_ai, file)
    with open('weaviate.json', 'w') as file:
        json.dump(weaviate, file)
    with open('google.json', 'w') as file:
        json.dump(google, file)
    print('Created configs. Make sure to populate them')
