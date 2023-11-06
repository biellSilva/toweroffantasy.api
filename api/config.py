

from dotenv import find_dotenv, get_key

API_KEY = get_key(find_dotenv(), key_to_get='API_KEY')
