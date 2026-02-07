import streamlit as st
import pandas as pd
#from logic.forecast import forecast_candidates, best_pick
from logic.admin import authenticate_admin
from logic.customers import authenticate_customer, register_customer
from ui.theme import set_theme, section

set_theme()

if not st.session_state.get("customer_logged_in") and not st.session_state.get("admin_logged_in"):
    st.markdown(
        """
        <div class="card">
            <h1>AI Wealth Login</h1>
            <p class="muted">Sign in to access customer or admin experiences.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<br/>", unsafe_allow_html=True)

    login_tab, register_tab, admin_tab = st.tabs(["Customer Login", "Create Account", "Admin Login"])

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
                st.rerun()

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

    with admin_tab:
        st.markdown("#### Admin access")
        with st.form("admin_login"):
            admin_username = st.text_input("Admin username")
            admin_password = st.text_input("Admin password", type="password")
            admin_submit = st.form_submit_button("Login as Admin")

        if admin_submit:
            if authenticate_admin(admin_username, admin_password):
                st.session_state["admin_logged_in"] = True
                st.success("Admin authenticated. You can now manage portfolios.")
            else:
                st.error("Admin credentials not recognized.")

        if st.session_state.get("admin_logged_in"):
            st.markdown("<br/>", unsafe_allow_html=True)
            if st.button("Go to Admin Console"):
                st.switch_page("pages/6_Admin.py")

    st.stop()

if st.session_state.get("customer_logged_in"):
    st.markdown(
        f"""
        <div class="card">
            <h4>Welcome, {st.session_state.get('customer_username', 'Customer')}!</h4>
            <p class="muted">You are signed in and ready to explore AI Wealth.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

if st.session_state.get("admin_logged_in"):
    st.markdown(
        """
        <div class="card">
            <h4>Admin session active</h4>
            <p class="muted">Manage customer portfolio allocations.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if st.button("Open Admin Console"):
        st.switch_page("pages/6_Admin.py")

st.markdown("<br/>", unsafe_allow_html=True)

st.markdown("""
<div class="card">
<h1>AI Wealth</h1>
<p class="muted">
Institutional-grade portfolio intelligence for disciplined investing.
</p>
</div>
""", unsafe_allow_html=True)

st.markdown("<br/>", unsafe_allow_html=True)

section("Our Process", "Built for long-term investors, not traders.")

cols = st.columns(4)
steps = [
    ("Risk Profiling", "Understand behaviour & tolerance"),
    ("Portfolio Assessment", "Visualise diversification"),
    ("Scenario Simulation", "Prepare for uncertainty"),
    ("Rebalancing Discipline", "Rules over emotions")
]

for col, (title, desc) in zip(cols, steps):
    with col:
        st.markdown(f"""
        <div class="card">
            <h4>{title}</h4>
            <p class="muted">{desc}</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br/>", unsafe_allow_html=True)

section("Platform Highlights", "Decision support across the investment lifecycle.")

highlights = st.columns(3)
highlight_data = [
    ("Institutional Lens", "Factor-based views and risk lenses in plain language."),
    ("Transparency", "Explainable signals with evidence for every recommendation."),
    ("Actionable Insights", "Clear next steps without trading or product bias.")
]

for col, (title, desc) in zip(highlights, highlight_data):
    with col:
        st.markdown(f"""
        <div class="card">
            <h4>{title}</h4>
            <p class="muted">{desc}</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br/>", unsafe_allow_html=True)

section("Live Market Feeds", "Jump into real-time dashboards.")

feed_cols = st.columns(3)
feed_links = [
    ("Stocks Live Data", "https://www.tradingview.com/markets/stocks-usa/"),
    ("Commodities Live Data", "https://www.tradingview.com/markets/commodities/"),
    ("Bitcoin Live Data", "https://www.tradingview.com/symbols/BTCUSD/")
]

for col, (label, link) in zip(feed_cols, feed_links):
    with col:
        st.markdown(f"""
        <div class="card">
            <a class="live-button" href="{link}" target="_blank" rel="noopener noreferrer">
                {label}
            </a>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br/>", unsafe_allow_html=True)

section("Forecast Lab", "Launch the data-science driven return outlook.")

forecast_cols = st.columns([2, 1])
with forecast_cols[0]:
    st.markdown(
        """
        <div class="card">
            <h4>Data Science Return Outlook</h4>
            <p class="muted">Explore live signals and horizon-based rankings for 1–2 years.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
with forecast_cols[1]:
    if st.button("Open Forecast Lab"):
        st.switch_page("pages/5_Forecast.py")

st.markdown("<br/>", unsafe_allow_html=True)

section("Advisory Toolkit", "Modules to expand the platform.")

toolkit = st.columns(4)
toolkit_items = [
    ("Goal Mapping", "Connect portfolios to milestones and timelines."),
    ("Stress Tests", "Visualise drawdowns against historical regimes."),
    ("Tax Awareness", "Highlight turnover and taxable events risk."),
    ("Behavioral Nudges", "Prompts to reinforce disciplined decisions.")
]

for col, (title, desc) in zip(toolkit, toolkit_items):
    with col:
        st.markdown(f"""
        <div class="card">
            <h4>{title}</h4>
            <p class="muted">{desc}</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br/>", unsafe_allow_html=True)

section("Trusted Metrics", "Designed to keep decisions grounded.")

metrics = st.columns(3)
metric_data = [
    ("Risk Alignment", "Score how closely a portfolio matches intent."),
    ("Diversification", "Measure concentration across assets and factors."),
    ("Discipline Index", "Track rebalancing consistency over time.")
]

for col, (title, desc) in zip(metrics, metric_data):
    with col:
        st.markdown(f"""
        <div class="card">
            <h4>{title}</h4>
            <p class="muted">{desc}</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br/>", unsafe_allow_html=True)

section("Client & Advisor Experiences", "Tailored journeys for different users.")

personas = st.columns(3)
persona_data = [
    ("Advisors", "Model portfolio oversight, client readiness reports, compliance logs."),
    ("Individuals", "Goal-based dashboards with risk-aware action nudges."),
    ("Institutions", "Committee-ready scorecards and policy guardrails.")
]

for col, (title, desc) in zip(personas, persona_data):
    with col:
        st.markdown(f"""
        <div class="card">
            <h4>{title}</h4>
            <p class="muted">{desc}</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br/>", unsafe_allow_html=True)

section("Integrations & Governance", "Keep data, reporting, and compliance connected.")

integrations = st.columns(4)
integration_data = [
    ("Data Feeds", "Custodian and broker imports, CSV or API."),
    ("CRM Sync", "Surface risk signals inside client workflows."),
    ("Audit Trail", "Decision logs for investment committees."),
    ("Report Packs", "Board-ready PDFs with consistent narratives.")
]

for col, (title, desc) in zip(integrations, integration_data):
    with col:
        st.markdown(f"""
        <div class="card">
            <h4>{title}</h4>
            <p class="muted">{desc}</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br/>", unsafe_allow_html=True)

section("Get Started", "Bring your current allocation and goals to begin.")

cta_cols = st.columns([2, 1])
with cta_cols[0]:
    st.markdown("""
    <div class="card">
        <h4>Ready to evaluate your portfolio?</h4>
        <p class="muted">Upload a holdings summary and receive a risk-aligned report.</p>
    </div>
    """, unsafe_allow_html=True)
with cta_cols[1]:
    st.button("Request a demo")

st.info(
    "Analytics-only platform. No execution, no return guarantees."
)
