# app/repository/user_repository.py
from motor.motor_asyncio import AsyncIOMotorCollection
from app.domain.models.models import User
from app.bootstrap.bootstrap import user_collection

class UserRepository:
    def __init__(self, user_collection: AsyncIOMotorCollection):
        self.user_collection = user_collection

    async def get_(self, steam_id: str) -> None:
        return self.user_collection.find_one({"AccountID":steam_id})
    
    async def create_(self, user: User) -> None:
        self.user_collection.insert_one(user.dict())