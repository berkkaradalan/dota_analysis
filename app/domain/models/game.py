from pydantic import BaseModel

class Items(BaseModel):
    ItemID:         int
    ItemName:       str
    ItemImage:      str

class Abilities(BaseModel):
    AbilityID:      int
    AbilityName:    str
    AbilityImage:   str

class Mods(BaseModel):
    ModID:          int
    ModName:        str