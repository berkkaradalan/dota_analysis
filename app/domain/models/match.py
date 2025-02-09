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

class DetailedMatch(BaseModel):
    AccountID:         str
    HeroID:            str
    Item0:             int
    Item1:             int
    Item2:             int
    Item3:             int
    Item4:             int
    Item5:             int
    Kills:             int
    Assists:           int
    Death:             int
    LastHits:          int
    Denies:            int
    GoldPerMinute:     int
    XPPerMinute:       int
    Level:             int
    NetWorth:          int
    HeroDamage:        int
    TowerDamage:       int
    HeroHealing:       int
    Gold:              int
    GoldSpent:         int
    AbilityUpgrades:   List[int]
    MatchStartTime:    float
    MatchDuration:     float
    GameMode:          int
    IsRadiant:         bool
    RadiantWin:        bool
    Win:               bool
    Lose:              bool
    KillDeathAssist:   float
    
    