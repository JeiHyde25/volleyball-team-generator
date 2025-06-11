from src.player import Player, create_player


class PlayerManager:
    def __init__(self):
        self.players = []
        self.seen_players = set()
        self.position_bucket = {
            "Setter": [],
            "Oopen Hitter": [],
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

    def get_player_list(self) -> int:
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

    def get_player_list(self, position: str = "") -> list:
        return self.position_bucket[position]
