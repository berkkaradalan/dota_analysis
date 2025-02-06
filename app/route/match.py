from fastapi import Depends
from fastapi import APIRouter
from app.services.service import MatchService
from app.bootstrap.bootstrap import match_collection

match_router = APIRouter()

@match_router.get("/{steam_id}")
async def get_user_match(steam_id:str):
    service = MatchService(match_collection)
    return await service.get_(steam_id=steam_id)

