from app.bootstrap.bootstrap import hero_collection
from app.services.service import HeroesService
from fastapi import Depends
from fastapi import APIRouter

heroes_router = APIRouter()

@heroes_router.get("/{hero_id}")
async def get_heroes(hero_id:str):
    service = HeroesService(hero_collection)
    return await service.GetHeroByID(hero_id=hero_id)

@heroes_router.get("/favorites/{steam_id}")
async def get_favorite_heroes(steam_id:str):
    service = HeroesService(hero_collection)
    return await service.GetFavoriteHeroes(steam_id=steam_id)