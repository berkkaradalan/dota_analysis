from fastapi import Depends
from fastapi import APIRouter
from app.services.service import UserService
from app.bootstrap.bootstrap import user_collection

user_router = APIRouter()

@user_router.get("/{steam_id}")
async def get_user_profile(steam_id:str):
    service = UserService(user_collection)
    return await service.get_(steam_id=steam_id)