from app.repository.heroes_repository import HeroRepository
from app.repository.favorite_heroes_repository import FavoriteHeroesRepository
from app.domain.models.models import Hero, TopHeroes
from app.bootstrap.bootstrap import user_collection, win_lose_collection, hero_collection, match_collection, favorite_heroes_collection
from .open_dota import OpenDotaService

class HeroesService:
    def __init__(self, heroes_collection):
        self.HeroRepository = HeroRepository(heroes_collection)
        self.FavoriteHeroesRepository = FavoriteHeroesRepository(favorite_heroes_collection)

    async def GetHeroByID(self, hero_id:str) -> dict:
        hero = await self.HeroRepository.GetHeroByID(hero_id)
        if hero:
            return {"message":Hero(**hero)}
        
        if not hero:
            service = OpenDotaService(self, user_collection=user_collection,win_lose_collection=win_lose_collection, match_collection=match_collection)
            return await service.GetHeroByID(hero_id=hero_id)

        return {"message":"raise exception here"}
    
    async def GetFavoriteHeroes(self, steam_id:str) -> dict:
        top_heroes = await self.FavoriteHeroesRepository.get_top_three_(steam_id=steam_id)
        if top_heroes:
            return {"message":[TopHeroes(**hero) for hero in top_heroes]}
        if not top_heroes:
            service = OpenDotaService(self, user_collection=user_collection,win_lose_collection=win_lose_collection, match_collection=match_collection)
            return await service.GetFavoriteHeroes(steam_id=steam_id)
        return {"message":"raise exception here"}