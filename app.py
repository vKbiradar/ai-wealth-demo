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

st.info(
    "Analytics-only platform. No execution, no return guarantees."
)
