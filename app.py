import streamlit as st
from ui.theme import set_theme, section

set_theme()

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

section("Advisory Toolkit", "What advisors and investors can add today.")

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
