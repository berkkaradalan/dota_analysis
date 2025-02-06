from typing import List
from enum import Enum
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class User(BaseModel):
    AccountID:         str
    PersonaName:       str
    Name:              Optional[str]
    SteamID:           str
    LastLogin:         datetime
    SteamAvatar:       str

class UserWinLoose(BaseModel):
    AccountID:         str
    Win:                int
    Lose:              int