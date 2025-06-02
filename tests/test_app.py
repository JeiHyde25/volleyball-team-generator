from streamlit.testing.v1 import AppTest


def test_add_player_button_disabled_when_any_of_the_fields_are_empty():
    at = AppTest.from_file("src/app.py")
    at.run(timeout=3)
    form = at.form("players_form")

    assert not form.button("Add Player").is_enabled()
