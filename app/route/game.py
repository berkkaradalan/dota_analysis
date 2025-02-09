from app.services.game import GameService
from fastapi import APIRouter

game_router = APIRouter()


@game_router.get("/item/{item_id}")
async def get_item(item_id:int):
    service = GameService()
    return await service.GetItemByID(item_id=item_id)


@game_router.get("/ability/{ability_id}")
async def get_ability(ability_id:int):
    service = GameService()
    return await service.GetAbilityByID(ability_id=ability_id)


@game_router.get("/mod/{mod_id}")
async def get_mod(mod_id:int):
    service = GameService()
    return await service.GetModsByID(mod_id=mod_id)