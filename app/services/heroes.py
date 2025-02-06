from app.repository.heroes_repository import HeroRepository
from app.domain.models.models import Hero
from app.bootstrap.bootstrap import user_collection
from .open_dota import OpenDotaService

class HeroesService:
    def __init__(self, heroes_collection):
        self.HeroRepository = HeroRepository(heroes_collection)

    async def GetHeroByID(self, hero_id:str) -> dict:
        hero = await self.HeroRepository.GetHeroByID(hero_id)
        if hero:
            return {"message":Hero(**hero)}
        
        if not hero:
            service = OpenDotaService(self, user_collection)
            return await service.GetHeroByID(hero_id=hero_id)

        return {"message":"raise exception here"}