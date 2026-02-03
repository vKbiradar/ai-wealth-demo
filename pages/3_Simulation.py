import streamlit as st
import pandas as pd
from logic.simulation import project_values
from ui.theme import section

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
