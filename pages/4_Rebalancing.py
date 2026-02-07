import streamlit as st
from logic.rebalance import rebalance_needed
from ui.theme import section

if not st.session_state.get("customer_logged_in"):
    st.warning("Customer access required. Please log in from the home page.")
    if st.button("Go to Login"):
        st.switch_page("app.py")
    st.stop()

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
