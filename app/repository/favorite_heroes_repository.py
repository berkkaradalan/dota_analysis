from motor.motor_asyncio import AsyncIOMotorCollection
from app.domain.models.models import TopHeroes
from app.bootstrap.bootstrap import favorite_heroes_collection

class FavoriteHeroesRepository:
    def __init__(self, favorite_heroes_collection: AsyncIOMotorCollection):
        self.favorite_heroes_collection = favorite_heroes_collection

    async def get_top_three_(self, steam_id: str) -> None:
        return self.favorite_heroes_collection.find({"AccountID":steam_id}).to_list(3)
    
    async def create_(self, hero: TopHeroes) -> None:
        self.favorite_heroes_collection.insert_one(hero.dict())