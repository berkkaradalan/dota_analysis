import uvicorn
from .env import env_variables
from .mongodb import connect_to_mongodb
from .logging import setup_logging
from pymongo.mongo_client import MongoClient

mongo_client = connect_to_mongodb()
mongodb = mongo_client["dota_analysis"]
env_variables = env_variables

def migrade_mongodb(mongo_client:MongoClient):
    mongodb = mongo_client["dota_analysis"]
    collections = mongodb.list_collection_names()
    if "user" not in collections:
        mongodb.create_collection("user")
    if "hero" not in collections:
        mongodb.create_collection("hero")
    if "match" not in collections:
        mongodb.create_collection("match")

def start_app():
    migrade_mongodb(mongo_client)
    # uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

user_collection = mongodb["user"]
hero_collection = mongodb["hero"]
match_collection = mongodb["match"]