# app/repository/user_repository.py
from motor.motor_asyncio import AsyncIOMotorCollection
from app.utils.utils import load_json

class GameRepository:
    def __init__(self: AsyncIOMotorCollection):
        self.item_json = "items.json"
        self.abilities_json = "abilities.json"
        self.mods_json = "mods.json"


    async def GetItemByID(self, item_id: int) -> None:
        items = load_json("items.json")
        return next((item for item in items["items"] if item["id"] == int(item_id)), None)
        
    async def GetAbilityByID(self, ability_id: int) -> None:
        abilities = load_json("abilities.json")
        return next((ability for ability in abilities["abilities"] if ability["id"] == str(ability_id)), None)
    
    async def GetModsByID(self, mod_id:int) -> None:
        mods = load_json("mods.json")
        return next((mod for mod in mods["mods"] if mod["id"] == int(mod_id)), None)