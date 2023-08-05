from os import getenv
from dotenv import load_dotenv

load_dotenv()
API_ID = int(getenv("18189325"))
API_HASH = getenv("7cb3b3ea70ba49f0721a511013eefe53")

BOT_TOKEN = getenv("6053302756:AAGeet_aitOe1nP7IHLM0vRFnNIcgGkBj4c")
OWNER_ID = int(getenv("2095495680"))

MONGO_DB_URI = getenv("MONGO_DB_URI")
MUST_JOIN = getenv("MUST_JOIN", None)
