import streamlit as st

from logic.customers import authenticate_customer, register_customer
from ui.theme import set_theme

set_theme()

st.markdown(
    """
    <div class="card">
        <h1>Customer Login</h1>
        <p class="muted">Securely access your AI Wealth experience.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("<br/>", unsafe_allow_html=True)

login_tab, register_tab = st.tabs(["Login", "Create Account"])

with login_tab:
    st.markdown("#### Sign in")
    with st.form("customer_login"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Login")

    if submitted:
        if authenticate_customer(username.strip(), password):
            st.session_state["customer_logged_in"] = True
            st.session_state["customer_username"] = username.strip()
            st.success("Welcome back! You're now signed in.")
        else:
            st.error("We couldn't sign you in. Check your username and password.")

    if st.session_state.get("customer_logged_in"):
        st.markdown("<br/>", unsafe_allow_html=True)
        if st.button("Continue to AI Wealth home"):
            st.switch_page("app.py")

with register_tab:
    st.markdown("#### Create your account")
    with st.form("customer_register"):
        new_username = st.text_input("Choose a username")
        new_password = st.text_input("Choose a password", type="password")
        confirm_password = st.text_input("Confirm password", type="password")
        register = st.form_submit_button("Create Account")

    if register:
        new_username = new_username.strip()
        if not new_username or not new_password:
            st.error("Please provide both a username and password.")
        elif new_password != confirm_password:
            st.error("Passwords do not match. Please try again.")
        elif not register_customer(new_username, new_password):
            st.error("That username is taken. Please choose another.")
        else:
            st.success("Account created! You can now log in with your credentials.")
