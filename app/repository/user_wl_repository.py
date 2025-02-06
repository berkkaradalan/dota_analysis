# app/repository/user_repository.py
from motor.motor_asyncio import AsyncIOMotorCollection
from app.domain.models.models import User
from app.bootstrap.bootstrap import win_lose_collection

class UserWinLoseRepository:
    def __init__(self, win_lose_collection: AsyncIOMotorCollection):
        self.win_lose_collection = win_lose_collection

    async def get_(self, steam_id: str) -> None:
        return self.win_lose_collection.find_one({"AccountID":steam_id})
    
    async def create_(self, user: User) -> None:
        self.win_lose_collection.insert_one(user.dict())
