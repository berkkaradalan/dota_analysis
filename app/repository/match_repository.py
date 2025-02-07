from motor.motor_asyncio import AsyncIOMotorCollection
from app.domain.models.models import User
from app.bootstrap.bootstrap import match_collection

class MatchRepository:
    def __init__(self, match_collection: AsyncIOMotorCollection):
        self.match_collection = match_collection

    async def get_(self, steam_id: str, limit: int, page: int) -> list:
        skip = (page - 1) * limit
        return self.match_collection.find({"AccountID": steam_id}).skip(skip).limit(limit).to_list(None)
    
    async def create_(self, user: User) -> None:
        self.match_collection.insert_one(user.dict())