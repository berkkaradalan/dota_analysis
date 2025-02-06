from app.bootstrap.bootstrap import win_lose_collection, user_collection, match_collection
from app.repository.user_wl_repository import UserWinLoseRepository
from .open_dota import OpenDotaService
from app.domain.models.models import UserWinLoose

class UserWinLoseService:
    def __init__(self, win_lose_collection):
        self.UserWinLoseRepository = UserWinLoseRepository(win_lose_collection)

    async def get_(self, steam_id: str) -> dict:
        user = await self.UserWinLoseRepository.get_(steam_id)
        if user:
            return {"message": UserWinLoose(**user)}
        
        if not user:
            service = OpenDotaService(self, win_lose_collection=win_lose_collection, user_collection=user_collection, match_collection=match_collection)
            return await service.GetUserWinLoseByID(steam_id=steam_id)

        return {"message":"raise exception here"}