from app.bootstrap.bootstrap import match_collection, user_collection, win_lose_collection, detailed_match_collection
from app.repository.match_repository import MatchRepository, DetailedMatchRepository
from .open_dota import OpenDotaService
from app.domain.models.models import Match, DetailedMatch

class MatchService:
    def __init__(self, user_collection):
        self.matchRepository = MatchRepository(user_collection)

    async def get_(self, steam_id: str, limit:int, page:int) -> dict:
        matches = await self.matchRepository.get_(steam_id, limit, page)

        if matches:
            return {"message": [Match(**match) for match in matches]} 
        
        service = OpenDotaService(self, user_collection=user_collection, win_lose_collection=win_lose_collection, match_collection=match_collection, detailed_match_collection=detailed_match_collection)
        return await service.GetUserMatchByID(steam_id=steam_id, limit=limit, page=page)

class DetailedMatchService:
    def __init__(self, detailed_match_collection):
        self.DetailedMatchRepository = DetailedMatchRepository(detailed_match_collection=detailed_match_collection)

    async def get_(self, match_id: str, steam_id:str) -> dict:
        detailed_match = await self.DetailedMatchRepository.get_(match_id, steam_id)
        if detailed_match:
            return {"message": DetailedMatch(**detailed_match)}
        
        service = OpenDotaService(self, user_collection=user_collection, win_lose_collection=win_lose_collection, match_collection=match_collection, detailed_match_collection=detailed_match_collection)
        return await service.GetDetailedMatchByID(match_id=match_id, steam_id=steam_id)