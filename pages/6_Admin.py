import streamlit as st

from logic.customers import load_customers
from logic.portfolios import get_allocation, set_allocation
from ui.theme import section

section(
    "Admin Console",
    "Edit customer portfolio allocations."
)

if not st.session_state.get("admin_logged_in"):
    st.warning("Admin access required. Please log in from the Login page.")
    if st.button("Go to Login"):
        st.switch_page("pages/0_Login.py")
    st.stop()

customers = load_customers()
if not customers:
    st.info("No customer accounts found yet.")
    st.stop()

customer_usernames = [customer["username"] for customer in customers]
selected_customer = st.selectbox("Select customer", customer_usernames)

allocation = get_allocation(selected_customer)

st.markdown("<div class='card'>", unsafe_allow_html=True)

st.markdown("#### Portfolio allocation")

equity = st.slider("Equity (%)", 0, 100, allocation["equity"])
debt = st.slider("Debt (%)", 0, 100, allocation["debt"])
gold = st.slider("Gold (%)", 0, 100, allocation["gold"])

if equity + debt + gold != 100:
    st.warning("Allocations should total 100% before saving.")

if st.button("Save allocation"):
    if equity + debt + gold != 100:
        st.error("Please adjust the sliders so the allocation totals 100%.")
    else:
        set_allocation(selected_customer, {
            "equity": equity,
            "debt": debt,
            "gold": gold,
        })
        st.success(f"Saved allocation for {selected_customer}.")

st.markdown("</div>", unsafe_allow_html=True)
