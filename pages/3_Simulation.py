import streamlit as st
import pandas as pd
from logic.simulation import project_values
from ui.theme import section

if not st.session_state.get("customer_logged_in"):
    st.warning("Customer access required. Please log in from the home page.")
    if st.button("Go to Login"):
        st.switch_page("app.py")
    st.stop()

section(
    "Scenario Simulation",
    "Showing possibilities, not predictions."
)

data = project_values()
df = pd.DataFrame(data)

st.line_chart(df)

st.caption(
    "Scenarios help investors prepare emotionally for volatility."
)
