from typing import List
from enum import Enum
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Match(BaseModel):
    AccountID:         str
    MatchID:           str
    PlayerSlot:        str
    RadiantWin:        bool
    Duration:          str
    GameMode:          str
    HeroID:            str
    StartTime:         datetime
    Kills:             int
    Deaths:            int
    Assists:           int