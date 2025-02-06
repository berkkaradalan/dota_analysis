# app/repository/user_repository.py
from motor.motor_asyncio import AsyncIOMotorCollection
from app.domain.models.models import Hero
from app.bootstrap.bootstrap import hero_collection

class HeroRepository:
    def __init__(self, hero_collection: AsyncIOMotorCollection):
        self.hero_collection = hero_collection

    async def GetHeroByID(self, hero_id: str) -> None:
        return self.hero_collection.find_one({"HeroID":hero_id})
    
    #todo - check this service
    async def create_(self, hero: Hero) -> None:
        self.hero_collection.insert_one(hero.dict())