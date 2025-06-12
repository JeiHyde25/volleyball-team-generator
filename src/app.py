import pandas as pd
import streamlit as st

from src.form_logic import process_player_form
from src.player_manager import PlayerManager
from src.csv_importer import import_players_from_df, validate_csv


def show_player_input_form():
    global name, position, skill_level, msg
    # Input Form
    with st.form(key="players_form"):
        name = st.text_input("Player Name")
        position = st.selectbox(
            "Playing Position",
            ["Select...", "Setter", "Open Hitter", "Middle Blocker", "Opposite Hitter"],
        )
        skill_level = st.selectbox(
            "Skill Level", ["Select...", "Developmental", "Intermediate", "Advanced"]
        )

        submitted = st.form_submit_button("Add Player")

        if submitted:
            msg = process_player_form(
                name, position, skill_level, st.session_state.player_manager
            )
            if msg.startswith("✅"):
                st.success(msg)
            else:
                st.error(msg)


def show_input_players_via_csv():
    global name, position, skill_level, msg

    with st.form(key="players_via_csv_form"):
        uploaded_file = st.file_uploader("Upload CSV to Import Players", type=["csv"])
        import_players_button_clicked = st.form_submit_button("Import Players from CSV")
    if uploaded_file:
        imported_players_df = pd.read_csv(uploaded_file)

        msg = validate_csv(imported_players_df)
        if "❌" in msg:
            st.error(msg)
        else:
            if import_players_button_clicked:
                added_count, skipped_count = import_players_from_df(
                    imported_players_df, st.session_state.player_manager
                )
                st.success(
                    f"🎉 Imported {added_count} player(s). ❌ Skipped {skipped_count} invalid/duplicate entries."
                )


def show_player_list():
    if st.session_state.player_manager.get_player_list():
        st.write(f"### Current Players ({app_player_manager.get_player_count()})")

        # Convert player objects to table-ready data
        table_data = [
            {
                "Name": player.name,
                "Position": player.position,
                "Skill Level": player.skill_level,
            }
            for player in st.session_state.player_manager.get_player_list()
        ]

        df = pd.DataFrame(table_data)

        st.dataframe(df, use_container_width=True, hide_index=True)


# Initialize session state
app_session_state = st.session_state
if "player_manager" not in app_session_state:
    app_session_state.player_manager = PlayerManager()

app_player_manager = app_session_state.player_manager

st.title("🏐 Volleyball Team Generator")
show_player_input_form()
show_input_players_via_csv()
show_player_list()

if st.button(label="Generate Teams", key="generate-teams"):
    if app_player_manager.get_player_count() < 12:
        st.error("❌ Cannot generate teams - player count is less than 12")
        errors = True
    else:
        try:
            teams = app_player_manager.generate_teams()
            st.success(f"🎉 Teams generated.")
        except ValueError as e:
            st.error(
                "❌ Cannot generate teams - invalid role distribution.\n\n"
                "Each team requires:\n"
                "• 1 Setter (total: 2)\n"
                "• 2 Open Hitters (total: 4)\n"
                "• 2 Middle Blockers (total: 4)\n"
                "• 1 Opposite Hitter (total: 2)\n\n"
                f"Your current selection:\n"
                f"• Setters: {app_player_manager.get_total_setter_count()}\n"
                f"• Open Hitters: {app_player_manager.get_total_open_hitter_count()}\n"
                f"• Middle Blockers: {app_player_manager.get_total_middle_blocker_count()}\n"
                f"• Opposite Hitters: {app_player_manager.get_total_opposite_hitter_count()}"
            )
