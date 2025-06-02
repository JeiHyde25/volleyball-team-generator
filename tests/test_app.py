from unittest.mock import MagicMock

import pandas as pd
from streamlit.testing.v1 import AppTest

from src.csv_importer import import_players_from_df
from src.player_manager import PlayerManager


def test_add_player_button_click_wont_succeed_when_name_position_and_skill_level_dont_have_values():
    at = AppTest.from_file("../src/app.py")
    at.run()
    name_input = at.text_input[0].value
    position_select = at.selectbox[0].value
    skill_level_select = at.selectbox[1].value

    assert name_input == ""
    assert position_select == "Select..."
    assert skill_level_select == "Select..."

    at.button[0].click()
    at.run(timeout=10)
    assert "❌" in at.error[0].value


def test_add_player_button_click_succeeds_when_name_position_and_skill_level_have_values():
    at = AppTest.from_file("../src/app.py")
    at.run()
    at.text_input[0].input("Jei")
    at.selectbox[0].select("Setter")
    at.selectbox[1].select("Developmental")

    name_input = at.text_input[0].value
    position_select = at.selectbox[0].value
    skill_level_select = at.selectbox[1].value

    assert name_input != ""
    assert position_select != "Select..."
    assert skill_level_select != "Select..."

    at.button[0].click()
    at.run()
    assert "✅" in at.success[0].value


def test_add_player_button_click_wont_succeed_with_invalid_values():
    at = AppTest.from_file("../src/app.py")
    at.run()
    at.text_input[0].set_value("Jei")
    at.selectbox[0].select("Setter")

    at.button[0].click()
    at.run()
    assert "❌" in at.error[0].value


def test_generate_teams_button_wont_succeed_if_players_less_than_twelve():
    at = AppTest.from_file("../src/app.py")

    mock_manager = MagicMock()
    mock_manager.get_player_count = MagicMock(return_value=11)
    mock_manager.has_valid_position_distribution = MagicMock(return_value=False)

    at.session_state.player_manager = mock_manager
    at.run()
    at.button[1].click()
    at.run()
    assert any("❌" in e.value for e in at.error)
    assert not at.success

def test_generate_teams_button_succeeds_if_players_count_twelve():
    at = AppTest.from_file("../src/app.py")
    mock_manager = MagicMock()
    mock_manager.get_player_count = MagicMock(return_value=0)
    at.session_state.player_manager = mock_manager
    at.run()
    assert at.session_state["player_manager"].get_player_count() == 0
    at.button[1].click()
    at.run()
    assert any("❌" in e.value for e in at.error)

    mock_manager.get_player_count = MagicMock(return_value=12)
    at.button[1].click()
    at.run()
    assert at.success


def test_generate_teams_button_wont_succeed_if_position_distribution_is_invalid():
    at = AppTest.from_file("../src/app.py")
    mock_manager = MagicMock()
    mock_manager.get_player_count = MagicMock(return_value=0)
    mock_manager.has_valid_position_distribution = MagicMock(return_value=False)
    at.session_state.player_manager = mock_manager
    at.run()
    assert at.session_state["player_manager"].get_player_count() == 0
    at.button[1].click()
    at.run()
    assert any("❌" in e.value for e in at.error)

    mock_manager.get_player_count = MagicMock(return_value=12)
    at.button[1].click()
    at.run()
    assert any("❌" in e.value for e in at.error)
