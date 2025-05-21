from src.player import Player, create_player
import pytest

VALID_POSITIONS = ["Setter", "Outside Hitter", "Middle Blocker", "Opposite"]

VALID_SKILL_LEVELS = [
    "Beginner",
    "Intermediate",
    "Advanced",
]


def test_create_player_valid():
    player = create_player("Harold", "Setter", "Intermediate")
    assert isinstance(player, Player)
    assert player.name == "Harold"
    assert player.position == "Setter"
    assert player.skill_level == "Intermediate"


def test_create_player_invalid():
    with pytest.raises(ValueError, match="Name cannot be empty"):
        create_player("", "Setter", "Intermediate")


def test_create_player_invalid_position():
    with pytest.raises(ValueError, match="Position cannot be empty"):
        create_player("Setter", "", "Intermediate")


def test_create_player_invalid_skill_level():
    with pytest.raises(ValueError, match="Skill level cannot be empty"):
        create_player("Harold", "Setter", "")


def test_create_player_begin_name_in_whitespace():
    player = create_player("  Harold", "Setter", "Intermediate")
    assert player.name == "Harold"


def test_create_player_end_name_in_whitespace():
    player = create_player("Harold  ", "Setter", "Intermediate")
    assert player.name == "Harold"


def test_create_player_begin_end_name_in_whitespace():
    player = create_player("  Harold  ", "Setter", "Intermediate")
    assert player.name == "Harold"
