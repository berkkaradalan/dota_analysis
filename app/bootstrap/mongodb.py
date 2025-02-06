from app.bootstrap.env import env_variables
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

def connect_to_mongodb():
    client = MongoClient(env_variables.MONGODB_URL, server_api=ServerApi('1'), tlsAllowInvalidCertificates=True)
    
    # try:
    #     client.admin.command('ping')
    #     print("Pinged your deployment. You successfully connected to MongoDB!")
    # except Exception as e:
    #     print(e)
    
    return client