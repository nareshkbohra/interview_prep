from enum import Enum


class DiskColor(Enum):
    RED = 1
    YELLOW = 2


class Player:
    def __init__(self, player_id: int, color: DiskColor):
        self.id = player_id
        self.color = color
