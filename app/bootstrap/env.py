from dotenv import load_dotenv
import os

load_dotenv()

class env_variables():
    MONGODB_URL = os.getenv("MONGODB_URL")
    PORT = os.getenv("PORT")
    URL = os.getenv("URL")