import streamlit as st
import pandas as pd
#from logic.forecast import forecast_candidates, best_pick
from ui.theme import set_theme, section

set_theme()

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
else:
    st.markdown(
        """
        <div class="card">
            <h4>Customer access</h4>
            <p class="muted">Log in to save your preferences and access personalized insights.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if st.button("Go to login"):
        st.switch_page("pages/0_Login.py")

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
