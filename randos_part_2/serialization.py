from dataclasses import dataclass
from typing import List


@dataclass
class Rank:
    rank: int
    appid: int
    concurrent_in_game: int
    peak_in_game: int

@dataclass
class Response:
    pass