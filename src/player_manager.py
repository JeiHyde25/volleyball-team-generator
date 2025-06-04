from src.player import Player, create_player


class PlayerManager:
    def __init__(self):
        self.players = []
        self.seen_players = set()
        self.position_counts = {
            "S": 0,
            "OH": 0,
            "MB": 0,
            "OP": 0
        }

    def add_unique_player(
        self, name: str = "", position: str = "", skill_level: str = ""
    ) -> str:
        key = (name, position, skill_level)
        if key in self.seen_players:
            return "❌ Duplicate Player detected"
        self.seen_players.add(key)
        self.players.append(create_player(name, position, skill_level))
        if position == "Setter":
            self.position_counts["S"] += 1
        elif position == "Open Hitter":
            self.position_counts["OH"] += 1
        elif position == "Middle Blocker":
            self.position_counts["MB"] += 1
        elif position == "Opposite Hitter":
            self.position_counts["OP"] += 1
        return "✅ Player added"

    def get_player_count(self) -> int:
        return len(self.players)

    def get_player_list(self) -> int:
        return self.players

    def has_valid_position_distribution(self) -> bool:
        return False

    def get_total_setter_count(self) -> int:
        return 1

    def get_total_open_hitter_count(self) -> int:
        return 1

    def get_total_middle_blocker_count(self) -> int:
        return 1

    def get_total_opposite_hitter_count(self) -> int:
        return 1

    def remove_all_players(self):
        self.players.clear()
        self.seen_players.clear()
