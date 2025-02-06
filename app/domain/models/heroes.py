from typing import List
from enum import Enum
from pydantic import BaseModel

class AttackTypes(str, Enum):
    MELEE = "Melee"
    RANGED = "Ranged"

class HeroRoles(str, Enum):
    CARRY = "Carry"
    ESCAPE = "Escape"
    NUKER = "Nuker"
    INITIATOR = "Initiator"
    DURABLE = "Durable"
    SUPPORT = "Support"
    DISABLER = "Disabler"
    PUSHER = "Pusher"


class Hero(BaseModel):
    HeroID:         str
    HeroName:       str
    HeroRoles:      List[HeroRoles]
    AttackType:     AttackTypes
    HeroImageURL:   str