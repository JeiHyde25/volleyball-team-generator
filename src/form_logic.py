from typing import Optional

from src.player import Player, create_player

INVALID_CHOICE = "Select..."


def process_player_form(
    name: str = "",
    position: str = "",
    skill_level: str = "",
    players: Optional[list[Player]] = None,
) -> str:
    if players is None:
        players = []
    if not name.strip():
        return "❌ Name cannot be empty"
    if position == INVALID_CHOICE or skill_level == INVALID_CHOICE:
        return "❌ Position and/or Skill Level cannot be empty"
    players.append(create_player(name, position, skill_level))
    return "✅ Player added"
