import pandas as pd
import streamlit as st

from src.form_logic import process_player_form
from src.player import Player

# Initialize session state
if "players" not in st.session_state:
    st.session_state.players = []

st.title("🏐 Volleyball Team Generator")

# Input Form
with st.form(key="players_form"):
    name = st.text_input("Player Name")
    position = st.selectbox(
        "Playing Position",
        ["Select...", "Setter", "Open Hitter", "Middle Blocker", "Opposite Hitter"],
    )
    skill_level = st.selectbox(
        "Skill Level", ["Select...", "Beginner", "Intermediate", "Advanced"]
    )
    submitted = st.form_submit_button("Add Player")

    if submitted:
        msg = process_player_form(name, position, skill_level, st.session_state.players)
        if msg.startswith("✅"):
            st.success(msg)
        else:
            st.error(msg)

# Show current player list
if st.session_state.players:
    st.write("### Current Players")

    # Convert player objects to table-ready data
    table_data = [
        {
            "Name": player.name,
            "Position": player.position,
            "Skill Level": player.skill_level,
        }
        for player in st.session_state.players
    ]

    df = pd.DataFrame(table_data)

    st.dataframe(df, use_container_width=True, hide_index=True)
