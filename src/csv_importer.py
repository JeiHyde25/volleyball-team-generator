from pandas import DataFrame

from src.form_logic import process_player_form
from src.player_manager import PlayerManager


def import_players_from_df(
    imported_players_df: DataFrame, player_manager: PlayerManager = None
) -> (int, int):
    added_count, skipped_count = 0, 0

    player_manager.remove_all_players()
    for index, row in imported_players_df.iterrows():
        name = str(row.get("Name", "")).strip()
        position = str(row.get("Position", "")).strip()
        skill_level = str(row.get("Skill Level", "")).strip()

        msg = process_player_form(name, position, skill_level, player_manager)
        if msg.startswith("✅"):
            added_count += 1
        else:
            skipped_count += 1
    return added_count, skipped_count


def validate_csv(imported_players_df: DataFrame) -> str:
    expected_columns = {"Name", "Position", "Skill Level"}
    if not expected_columns.issubset(imported_players_df.columns):
        return "❌ Invalid CSV format. Required columns: Name, Position, Skill Level"
    return "✅ Valid CSV format."
