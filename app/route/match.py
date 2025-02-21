from fastapi import Depends
from fastapi import APIRouter
from app.services.service import MatchService, DetailedMatchService
from app.bootstrap.bootstrap import match_collection, detailed_match_collection

match_router = APIRouter()

@match_router.get("/{steam_id}")
async def get_user_match(steam_id:str, limit:int=10, page:int=1):
    service = MatchService(match_collection)
    return await service.get_(steam_id=steam_id, limit=limit, page=page)

@match_router.get("/detailed/{match_id}")
async def get_detailed_match(match_id:str, steam_id:str):
    service = DetailedMatchService(detailed_match_collection)
    return await service.get_(match_id=match_id, steam_id=steam_id)