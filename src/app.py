import pandas as pd
import streamlit as st

from src.form_logic import process_player_form
from src.player_manager import PlayerManager


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


def show_input_play_via_csv():
    global name, position, skill_level, msg
    uploaded_file = st.file_uploader("Upload CSV to Import Players", type=["csv"])
    if uploaded_file:
        imported_players_df = pd.read_csv(uploaded_file)

        st.subheader("📄 Preview Uploaded CSV")
        st.dataframe(imported_players_df.head(), use_container_width=True)

        expected_columns = {"Name", "Position", "Skill Level"}
        if not expected_columns.issubset(imported_players_df.columns):
            st.error(
                "❌ Invalid CSV format. Required columns: Name, Position, Skill Level"
            )
        else:
            if st.button("Import Players from CSV"):
                added_count = 0
                skipped_count = 0

                for index, row in imported_players_df.iterrows():
                    name = str(row.get("Name", "")).strip()
                    position = str(row.get("Position", "")).strip()
                    skill_level = str(row.get("Skill Level", "")).strip()

                    msg = process_player_form(
                        name, position, skill_level, st.session_state.player_manager
                    )
                    if msg.startswith("✅"):
                        added_count += 1
                    else:
                        skipped_count += 1

                st.success(
                    f"🎉 Imported {added_count} player(s). ❌ Skipped {skipped_count} invalid/duplicate entries."
                )


# Initialize session state
if "player_manager" not in st.session_state:
    st.session_state.player_manager = PlayerManager()

st.title("🏐 Volleyball Team Generator")


show_player_input_form()
show_input_play_via_csv()

# Show current player list
if st.session_state.player_manager.get_player_list():
    st.write("### Current Players")

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
