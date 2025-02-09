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
        user_collection = mongodb["user"]
        user_collection.create_index("AccountID", unique=True)
    if "hero" not in collections:
        mongodb.create_collection("hero")
        hero_collection = mongodb["hero"]
        hero_collection.create_index("HeroID", unique=True)
    if "match" not in collections:
        mongodb.create_collection("match")
        match_collection = mongodb["match"]
        match_collection.create_index("MatchID", unique=True)
    if "winlose" not in collections:
        mongodb.create_collection("winlose")
        win_lose_collection = mongodb["winlose"]
        win_lose_collection.create_index("AccountID", unique=True)
    if "favorite_heroes" not in collections:
        mongodb.create_collection("favorite_heroes")
        # favorite_heroes_collection = mongodb["favorite_heroes"]
        # favorite_heroes_collection.create_index("AccountID")
    if "detailed_match" not in collections:
        mongodb.create_collection("detailed_match")
        detailed_match_collection = mongodb["detailed_match"]
        detailed_match_collection.create_index("CollectionHash", unique=True)

def start_app():
    migrade_mongodb(mongo_client)
    # uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

user_collection = mongodb["user"]
hero_collection = mongodb["hero"]
match_collection = mongodb["match"]
win_lose_collection = mongodb["winlose"]
favorite_heroes_collection = mongodb["favorite_heroes"]
detailed_match_collection = mongodb["detailed_match"]