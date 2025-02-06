import requests
from app.domain.models.models import Hero, User, UserWinLoose, Match
from app.repository.heroes_repository import HeroRepository
from app.repository.user_repository import UserRepository
from app.repository.match_repository import MatchRepository
from app.bootstrap.bootstrap import hero_collection, user_collection, win_lose_collection, match_collection

class OpenDotaService:
    def __init__(self, heroes_collection, user_collection, win_lose_collection, match_collection):
        self.hero_collection = hero_collection
        self.user_collection = user_collection
        self.win_lose_collection = win_lose_collection
        self.match_collection = match_collection

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
    
    async def GetUserWinLoseByID(self, steam_id:str) -> dict:
        user = requests.get(f"https://api.opendota.com/api/players/{steam_id}/wl").json()
        if "win" in user:
            win_lose_data = UserWinLoose(
                AccountID=steam_id,
                Win=user["win"],
                Lose=user["lose"]
            )
            await UserRepository(self.win_lose_collection).create_(win_lose_data)
            return win_lose_data
        return {"message":"User not found"}
    
    async def GetUserMatchByID(self, steam_id:str) -> dict:
        matches = requests.get(f"https://api.opendota.com/api/players/{steam_id}/matches").json()
        for match in matches:
            match_data = Match(
                AccountID=steam_id,
                MatchID=str(match["match_id"]),
                PlayerSlot=str(match["player_slot"]),
                RadiantWin=match["radiant_win"],
                Duration=str(match["duration"]),
                GameMode=str(match["game_mode"]),
                HeroID=str(match["hero_id"]),
                StartTime=match["start_time"],
                Kills=match["kills"],
                Deaths=match["deaths"],
                Assists=match["assists"],
            )
            await MatchRepository(self.match_collection).create_(match_data)
        return {"message":matches}