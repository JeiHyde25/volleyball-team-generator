import pytest
from beartype.roar import BeartypeCallHintParamViolation, BeartypeException

from src import player_manager
from src.form_logic import process_player_form
from src.player_manager import PlayerManager


def test_process_player_form_success():
    manager = PlayerManager()
    msg = process_player_form("Harold", "Setter", "Beginner", manager)
    assert msg == "✅ Player added"
    assert manager.get_player_count() == 1


def test_process_player_form_empty_name_not_accepted():
    manager = PlayerManager()
    msg = process_player_form("", "Setter", "Beginner", manager)
    assert msg == "❌ Name cannot be empty"
    assert manager.get_player_count() == 0


def test_process_player_form_empty_position_not_accepted():
    manager = PlayerManager()
    msg = process_player_form("Jei", "Select...", "Beginner", manager)
    assert msg == "❌ Position and/or Skill Level cannot be empty"
    assert manager.get_player_count() == 0


def test_process_player_form_empty_skill_level_not_accepted():
    manager = PlayerManager()
    msg = process_player_form("Je", "Setter", "Select...", manager)
    assert msg == "❌ Position and/or Skill Level cannot be empty"
    assert manager.get_player_count() == 0


def test_process_player_form_multiple_players_accepted():
    manager = PlayerManager()
    msg = process_player_form("Harold", "Setter", "Beginner", manager)
    assert msg == "✅ Player added"
    assert manager.get_player_count() == 1
    msg = process_player_form("Jei", "Setter", "Beginner", manager)
    assert msg == "✅ Player added"
    assert manager.get_player_count() == 2
    msg = process_player_form("Jei", "Setter", "Beginner", manager)
    assert msg == "❌ Duplicate Player detected"
    assert manager.get_player_count() == 2


def test_process_player_form_duplicate_player_not_accepted():
    manager = PlayerManager()
    msg = process_player_form("Harold", "Setter", "Beginner", manager)
    assert msg == "✅ Player added"
    assert manager.get_player_count() == 1
    msg = process_player_form("Harold", "Setter", "Beginner", manager)
    assert msg == "❌ Duplicate Player detected"
    assert manager.get_player_count() == 1


def test_process_player_form_raises_exception_from_invalid_name_type():
    with pytest.raises(Exception):
        manager = PlayerManager()
        process_player_form(123, "Setter", "Beginner", manager)


def test_process_player_form_raises_exception_when_player_manager_is_none():
    with pytest.raises(BeartypeException):
        process_player_form("Jei", "Setter", "Beginner")


def test_process_player_form_raises_exception_when_player_manager_is_not_of_type_PlayerManager():
    with pytest.raises(BeartypeException):
        process_player_form("Jei", "Setter", "Beginner", manager=[])
    with pytest.raises(BeartypeException):
        process_player_form("Jei", "Setter", "Beginner", manager=12)
