from src.player import Player, create_player


class PlayerManager:
    def __init__(self):
        self.players = []
        self.seen_players = set()

    def add_unique_player(
        self, name: str = "", position: str = "", skill_level: str = ""
    ) -> str:
        key = (name, position, skill_level)
        if key in self.seen_players:
            return "❌ Duplicate Player detected"
        self.seen_players.add(key)
        self.players.append(create_player(name, position, skill_level))
        return "✅ Player added"

    def get_player_count(self) -> int:
        return len(self.players)

    def get_player_list(self):
        return self.players
