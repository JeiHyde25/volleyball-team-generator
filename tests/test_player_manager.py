from src.player import Player
from src.player_manager import PlayerManager


def test_add_unique_player_succeeds_when_adding_first_player():
    player_manager = PlayerManager()
    msg = player_manager.add_unique_player("Jei", "Setter", "Developmental")
    assert msg == "✅ Player added"
    assert player_manager.get_player_count() == 1
    assert Player("Jei", "Setter", "Developmental") in player_manager.get_player_list()


def test_add_unique_player_succeeds_when_adding_second_unique_player():
    player_manager = PlayerManager()
    player_manager.add_unique_player("Jei", "Setter", "Developmental")
    msg = player_manager.add_unique_player("Carl", "Setter", "Developmental")
    assert msg == "✅ Player added"
    assert player_manager.get_player_count() == 2
    assert Player("Carl", "Setter", "Developmental") in player_manager.get_player_list()


def test_add_unique_player_failes_when_adding_a_duplicate_player():
    player_manager = PlayerManager()
    player_manager.add_unique_player("Jei", "Setter", "Developmental")
    msg = player_manager.add_unique_player("Jei", "Setter", "Developmental")
    assert msg == "❌ Duplicate Player detected"
    assert player_manager.get_player_count() == 1


def test_has_valid_position_distribution_returns_true_if_player_positions_are_balanced():
    player_manager = PlayerManager()
    imported_players_df = pd.read_csv("players_twelve.csv")


    assert player_manager.has_valid_position_distribution()