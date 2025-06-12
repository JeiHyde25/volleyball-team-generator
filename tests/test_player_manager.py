from src.csv_importer import import_players_from_df
from src.player import Player
from src.player_manager import PlayerManager
import pandas as pd


def test_add_unique_player_succeeds_when_adding_first_player():
    player_manager = PlayerManager()
    msg = player_manager.add_unique_player("Jei", "Setter", "Developmental")
    assert msg == "✅ Player added"
    assert player_manager.get_player_count() == 1
    assert (
        any(
            player.name == "Jei"
            for player in player_manager.get_position_list("Setter")
        )
        == True
    )
    assert player_manager.get_total_setter_count() == 1


def test_add_unique_player_succeeds_when_adding_second_unique_player():
    player_manager = PlayerManager()
    player_manager.add_unique_player("Jei", "Setter", "Developmental")
    msg = player_manager.add_unique_player("Carl", "Setter", "Developmental")
    assert msg == "✅ Player added"
    assert player_manager.get_player_count() == 2
    assert (
        any(
            player.name == "Carl"
            for player in player_manager.get_position_list("Setter")
        )
        == True
    )
    assert player_manager.get_total_setter_count() == 2


def test_add_unique_player_failes_when_adding_a_duplicate_player():
    player_manager = PlayerManager()
    player_manager.add_unique_player("Jei", "Setter", "Developmental")
    msg = player_manager.add_unique_player("Jei", "Setter", "Developmental")
    assert msg == "❌ Duplicate Player detected"
    assert player_manager.get_player_count() == 1
    assert any(
        player.name == "Jei" for player in player_manager.get_position_list("Setter")
    )


def test_has_valid_position_distribution_returns_true_if_player_positions_are_balanced():
    player_manager = PlayerManager()
    imported_players_df = pd.read_csv("tests/players_twelve.csv")
    import_players_from_df(imported_players_df, player_manager)
    assert player_manager.has_valid_position_distribution()


def test_has_valid_position_distribution_returns_false_if_player_positions_are_not_balanced():
    player_manager = PlayerManager()
    imported_players_df = pd.read_csv(
        "tests/players_twelve_lacking_player_position.csv"
    )
    import_players_from_df(imported_players_df, player_manager)
    assert not player_manager.has_valid_position_distribution()


def test_generate_teams_returns_dataframe_of_teams():
    player_manager = PlayerManager()
    imported_players_df = pd.read_csv("tests/players_twelve.csv")
    import_players_from_df(imported_players_df, player_manager)
    df = player_manager.generate_teams()
    assert df.shape == (6, 2)
    assert list(df.columns) == ["Team A", "Team B"]
    assert list(df.index) == [
        "Setter",
        "Open Hitter",
        "Open Hitter",
        "Middle Blocker",
        "Middle Blocker",
        "Opposite Hitter",
    ]
    assert "Jei" in df["Team A"].values
    assert "Dennis" in df["Team B"].values
