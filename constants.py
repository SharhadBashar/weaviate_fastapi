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
DB_CONFIG_CK = 'cockroach.json'
OPEN_AI_CONFIG = 'open_ai.json'
