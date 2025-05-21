from src.form_logic import process_player_form


def test_process_player_success():
    players = []
    msg = process_player_form("Harold", "Setter", "Beginner", players)
    assert msg == "✅ Player added"
    assert len(players) == 1


def test_process_player_empty_name():
    players = []
    msg = process_player_form("", "Setter", "Beginner", players)
    assert msg == "❌ Name cannot be empty"
    assert len(players) == 0
