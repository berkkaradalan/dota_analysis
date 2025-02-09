import requests
from app.domain.models.models import Hero, User, UserWinLoose, Match, TopHeroes
from app.repository.heroes_repository import HeroRepository
from app.repository.user_repository import UserRepository
from app.repository.match_repository import MatchRepository
from app.repository.favorite_heroes_repository import FavoriteHeroesRepository
from pymongo.errors import DuplicateKeyError
from app.bootstrap.bootstrap import hero_collection, user_collection, win_lose_collection, match_collection, favorite_heroes_collection

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
    
    async def GetUserMatchByID(self, steam_id: str, limit: int, page: int) -> dict:
        offset = (page - 1) * limit
        matches = requests.get(f"https://api.opendota.com/api/players/{steam_id}/matches?limit={limit}&offset={offset}").json()
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
            try:
                await MatchRepository(self.match_collection).create_(match_data)
            except DuplicateKeyError:
                pass
        return {"message": matches}
    
    async def GetFavoriteHeroes(self, steam_id:str) -> dict:
        heroes = requests.get(f"https://api.opendota.com/api/players/{steam_id}/heroes").json()
        top_heroes = sorted(heroes, key=lambda x: x["games"], reverse=True)[:3]
        result = []
        for hero in top_heroes:
            hero_data = TopHeroes(
                AccountID=steam_id,
                HeroID=str(hero["hero_id"]),
                LastPlayed=hero["last_played"],
                Games=hero["games"],
                GamesWon=hero["win"]
            )
            await FavoriteHeroesRepository(favorite_heroes_collection).create_(hero_data)
            result.append(hero_data)
        return {"message":result}