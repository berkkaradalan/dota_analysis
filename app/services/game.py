from app.repository.game_repository import GameRepository
from app.domain.models.models import Items, Abilities, Mods

class GameService:
    def __init__(self):
        self.GameRepository = GameRepository()

    async def GetItemByID(self, item_id:int) -> dict:
        item = await self.GameRepository.GetItemByID(item_id=item_id)
        if not item:
            return {"error": "Item not found"}
        return Items(
            ItemID = item["id"],
            ItemName = item["name"],
            ItemImage = f"https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/items/{item['name']}.png"
        )
    
    async def GetAbilityByID(self, ability_id:int) -> dict:
        ability =  await self.GameRepository.GetAbilityByID(ability_id=ability_id)
        if not ability:
            return {"error": "Ability not found"}
        return Abilities(
            AbilityID = ability["id"],
            AbilityName = ability["name"],
            AbilityImage = f"https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/abilities/{ability['name']}.png"
        )
    
    async def GetModsByID(self, mod_id:int) -> dict:
        mod = await self.GameRepository.GetModsByID(mod_id=mod_id)
        if not mod:
            return {"error": "Mod not found"}
        return Mods(
            ModID = mod["id"],
            ModName = mod["name"]
        )