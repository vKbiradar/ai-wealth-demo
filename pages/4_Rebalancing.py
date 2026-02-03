import streamlit as st
from logic.rebalance import rebalance_needed
from ui.theme import section

section(
    "Rebalancing Discipline",
    "Rules over emotions."
)

current_equity = st.slider("Current Equity (%)", 0, 100, 75)
target_equity = 60

needed, drift = rebalance_needed(current_equity, target_equity)

if needed:
    st.warning(
        f"Equity drift of {drift}% detected. Rebalancing suggested."
    )
else:
    st.success("Portfolio within disciplined allocation range.")

st.caption(
    "No buy/sell instructions. Only discipline signals."
)
