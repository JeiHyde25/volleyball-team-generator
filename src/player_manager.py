from typing import Any

import pandas as pd

from src.player import Player, create_player


class PlayerManager:
    def __init__(self):
        self.players = []
        self.seen_players = set()
        self.position_bucket = {
            "Setter": [],
            "Open Hitter": [],
            "Middle Blocker": [],
            "Opposite Hitter": [],
        }

    def add_unique_player(
        self, name: str = "", position: str = "", skill_level: str = ""
    ) -> str:
        key = (name, position, skill_level)
        if key in self.seen_players:
            return "❌ Duplicate Player detected"
        self.seen_players.add(key)
        player = create_player(name, position, skill_level)
        self.players.append(player)
        if player.position in self.position_bucket:
            self.position_bucket[player.position].append(player)
        return "✅ Player added"

    def get_player_count(self) -> int:
        return len(self.players)

    def get_player_list(self) -> list[Any]:
        return self.players

    def has_valid_position_distribution(self) -> bool:
        return (
            self.get_total_setter_count() == self.get_total_opposite_hitter_count()
            and self.get_total_open_hitter_count()
            == self.get_total_middle_blocker_count()
            and (self.get_total_open_hitter_count() / self.get_total_setter_count())
            == 2
        )

    def get_total_setter_count(self) -> int:
        return len([p for p in self.players if p.position == "Setter"])

    def get_total_open_hitter_count(self) -> int:
        return len([p for p in self.players if p.position == "Open Hitter"])

    def get_total_middle_blocker_count(self) -> int:
        return len([p for p in self.players if p.position == "Middle Blocker"])

    def get_total_opposite_hitter_count(self) -> int:
        return len([p for p in self.players if p.position == "Opposite Hitter"])

    def remove_all_players(self):
        self.players.clear()
        self.seen_players.clear()

    def get_position_list(self, position: str = "") -> list[Any]:
        return self.position_bucket[position]

    def generate_teams(self) -> pd.DataFrame:
        if self.has_valid_position_distribution():
            data, roles = self._distribute_players_by_position()
            df = pd.DataFrame(data, index=roles)
            print(df)
            return df
        return pd.DataFrame()

    def _distribute_players_by_position(self) -> tuple[dict[str, list[str]], list[str]]:
        roles = [
            "Setter",
            "Open Hitter",
            "Open Hitter",
            "Middle Blocker",
            "Middle Blocker",
            "Opposite Hitter",
        ]
        role_to_row = {
            "Setter": [0],
            "Open Hitter": [1, 2],
            "Middle Blocker": [3, 4],
            "Opposite Hitter": [5],
        }
        number_of_teams = self.get_player_count() // 6
        teams = [f"Team {chr(65 + i)}" for i in range(number_of_teams)]
        data = {team: [""] * len(roles) for team in teams}

        for role, rows in role_to_row.items():
            print(role, rows)
            players = self.position_bucket[role]
            for i, player in enumerate(players):
                print(i, player)
                team_index = i % number_of_teams
                print(team_index, teams[team_index])

                row_index = (
                    rows[i % len(rows)] if len(rows) > i % len(rows) else rows[0]
                )
                data[teams[team_index]][row_index] = player.name
        return data, roles
