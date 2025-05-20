from dataclasses import dataclass

@dataclass
class Player:
    name: str
    position: str
    skill_level: str

def create_player(name: str="", position: str="", skill_level: str=""):
    validate_player_fields(name, position, skill_level)
    return Player(name=name.strip(),
                  position=position.strip(),
                  skill_level=skill_level.strip())

def validate_player_fields(name: str, position: str, skill_level: str):
    if not name:
        raise ValueError("Name cannot be empty")
    if not position.strip():
        raise ValueError("Position cannot be empty")
    if not skill_level.strip():
        raise ValueError("Skill level cannot be empty")