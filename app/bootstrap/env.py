from dotenv import load_dotenv
import os

load_dotenv()

class env_variables():
    MONGODB_URL = os.getenv("MONGODB_URL")
    PORT = os.getenv("PORT")
    URL = os.getenv("URL")
    ORIGINS = os.getenv("ORIGINS")
    OPEN_DOTA_API_URL = os.getenv("OPEN_DOTA_API_URL")
    DOTA_CDN_URL = os.getenv("DOTA_CDN_URL")