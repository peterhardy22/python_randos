import requests

from dataclasses import dataclass, asdict
import json
from typing import List


@dataclass
class Rank:
    rank: int
    appid: int
    concurrent_in_game: int
    peak_in_game: int

@dataclass
class Response:
    last_update: int
    ranks: List[Rank]

    def __post_init__(self):
        self.ranks = [Rank(**rank) for rank in self.ranks]

@dataclass
class TopSteamGames:
    response: Response

    def __post_init__(self):
        self.response = Response(**self.response)

    def toJson(self):
        # Turns it into a dictionary, then a JSON string.
        return json.dumps(asdict(self), indent=4)


if __name__ == "__main__":
    steam_top_games_url: str = "https://api.steampowered.com/ISteamChartsService/GetGamesByConcurrentPlayers/v1/"
    steam_response: dict = requests.get(steam_top_games_url).json()

    top_games = TopSteamGames(**steam_response)
    # print(top_games.response.ranks[:1])

    with open("randos_part_2/Top Games.json", "w") as top_games_json:
        top_games_json.write(top_games.toJson())