import requests
from app.utils.utils import get_hash
from app.domain.models.models import Hero, User, UserWinLoose, Match, TopHeroes, DetailedMatch
from app.repository.heroes_repository import HeroRepository
from app.repository.user_repository import UserRepository
from app.repository.match_repository import MatchRepository, DetailedMatchRepository
from app.repository.favorite_heroes_repository import FavoriteHeroesRepository
from pymongo.errors import DuplicateKeyError
from app.bootstrap.bootstrap import hero_collection, user_collection, win_lose_collection, match_collection, favorite_heroes_collection, detailed_match_collection

class OpenDotaService:
    def __init__(self, heroes_collection, user_collection, win_lose_collection, match_collection, detailed_match_collection):
        self.hero_collection = hero_collection
        self.user_collection = user_collection
        self.win_lose_collection = win_lose_collection
        self.match_collection = match_collection
        self.detailed_match_collection = detailed_match_collection

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
    
    async def GetDetailedMatchByID(self, match_id: str, steam_id:str) -> dict:
        match = requests.get(f"https://api.opendota.com/api/matches/{match_id}").json()
        if "players" in match:
            match = match["players"]
            player_data = next((player for player in match if player.get('account_id') == int(steam_id)), None)
            if player_data:
                detailed_match_data = DetailedMatch(
                    MatchID=match_id,
                    AccountID=steam_id,
                    HeroID=str(player_data["hero_id"]),
                    Item0=player_data["item_0"],
                    Item1=player_data["item_1"],
                    Item2=player_data["item_2"],
                    Item3=player_data["item_3"],
                    Item4=player_data["item_4"],
                    Item5=player_data["item_5"],
                    Kills=player_data["kills"],
                    Assists=player_data["assists"],
                    Death=player_data["deaths"],
                    LastHits=player_data["last_hits"],
                    Denies=player_data["denies"],
                    GoldPerMinute=player_data["gold_per_min"],
                    XPPerMinute=player_data["xp_per_min"],
                    Level=player_data["level"],
                    NetWorth=player_data["net_worth"],
                    HeroDamage=player_data["hero_damage"],
                    TowerDamage=player_data["tower_damage"],
                    HeroHealing=player_data["hero_healing"],
                    Gold=player_data["gold"],
                    GoldSpent=player_data["gold_spent"],
                    AbilityUpgrades=player_data["ability_upgrades_arr"],
                    MatchStartTime=player_data["start_time"],
                    MatchDuration=player_data["duration"],
                    GameMode=player_data["game_mode"],
                    IsRadiant=player_data["isRadiant"],
                    RadiantWin=player_data["radiant_win"],
                    Win=player_data["win"],
                    Lose=player_data["lose"],
                    KillDeathAssist=player_data["kda"],
                    CollectionHash=str(match_id + steam_id)
            )   
                await DetailedMatchRepository(self.detailed_match_collection).create_(detailed_match=detailed_match_data)
                return detailed_match_data
        
        return {"message":"Match or User not found"}