from beartype import beartype
from beartype.roar import BeartypeException

from src.player_manager import PlayerManager

INVALID_CHOICE = "Select..."


@beartype
def process_player_form(
    name: str = "",
    position: str = "",
    skill_level: str = "",
    manager: PlayerManager = None,
) -> str:
    if manager is None:
        raise BeartypeException(INVALID_CHOICE)
    if not name.strip():
        return "❌ Name cannot be empty"
    if position == INVALID_CHOICE or skill_level == INVALID_CHOICE:
        return "❌ Position and/or Skill Level cannot be empty"
    return manager.add_unique_player(name, position, skill_level)
