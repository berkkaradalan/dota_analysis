from app.bootstrap.bootstrap import user_collection
from app.repository.user_repository import UserRepository
from .open_dota import OpenDotaService
from app.domain.models.models import User

class UserService:
    def __init__(self, user_collection):
        self.userRepository = UserRepository(user_collection)

    async def get_(self, steam_id: str) -> dict:
        user = await self.userRepository.get_(steam_id)
        if user:
            return {"message": User(**user)}
        
        if not user:
            service = OpenDotaService(self, user_collection)
            return await service.GetUserByID(steam_id=steam_id)
        
        return {"message":"raise exception here"}
        
