from fastapi import Depends
from fastapi import APIRouter
from app.services.service import UserService, UserWinLoseService
from app.bootstrap.bootstrap import user_collection, win_lose_collection

user_router = APIRouter()

@user_router.get("/{steam_id}")
async def get_user_profile(steam_id:str):
    service = UserService(user_collection)
    return await service.get_(steam_id=steam_id)

@user_router.get("/winlose/{steam_id}")
async def get_user_win_lose(steam_id:str):
    service = UserWinLoseService(win_lose_collection)
    return await service.get_(steam_id=steam_id)