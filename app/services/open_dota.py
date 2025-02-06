import requests
from app.domain.models.models import Hero, User
from app.repository.heroes_repository import HeroRepository
from app.repository.user_repository import UserRepository
from app.bootstrap.bootstrap import hero_collection
from app.bootstrap.bootstrap import user_collection

class OpenDotaService:
    def __init__(self, heroes_collection, user_collection):
        self.hero_collection = hero_collection
        self.user_collection = user_collection

    async def GetHeroByID(self, hero_id:str) -> dict:
        heroes = requests.get("https://api.opendota.com/api/heroes").json()
        for hero in heroes:
            if hero["id"] == int(hero_id):
                hero_data = Hero(
                    HeroID = str(hero["id"]),
                    HeroName = hero["localized_name"],
                    HeroRoles = hero["roles"],
                    AttackType = hero["attack_type"],
                    HeroImageURL = f"https://cdn.dota2.com/apps/dota2/images/heroes/{hero['name'].replace('npc_dota_hero_', '')}_full.png"
                )
                await HeroRepository(self.hero_collection).create_(hero_data)
                return hero_data
        return {"message":"Hero not found"}

    async def GetUserByID(self, steam_id:str) -> dict:
        user = requests.get(f"https://api.opendota.com/api/players/{steam_id}").json()
        if "profile" in user:
            user_data = User(
                AccountID=steam_id,
                PersonaName=user["profile"]["personaname"],
                Name=user["profile"]["name"],
                SteamID=user["profile"]["steamid"],
                LastLogin=user["profile"]["last_login"],
                SteamAvatar=user["profile"]["avatar"]
            )
            await UserRepository(self.user_collection).create_(user_data)
            return user_data

        return {"message":"User not found"}