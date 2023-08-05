from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("29028317"))
API_HASH = getenv("8f2831819e4f3fdc44945d2e4d2aa095")

BOT_TOKEN = getenv("6540492667:AAHhF4QSufK_VHwTwxUT749r0vQBiLoAkug")
OWNER_ID = int(getenv("5848055044"))

MONGO_DB_URI = getenv("MONGO_DB_URI")
MUST_JOIN = getenv("MUST_JOIN", None)
