import streamlit as st
import pandas as pd
import plotly.express as px
from logic.portfolio import risk_alignment
from ui.theme import section

section(
    "Portfolio Assessment",
    "Visualize diversification and risk mismatch."
)

st.markdown("<div class='card'>", unsafe_allow_html=True)

profile = st.selectbox(
    "Investor Profile",
    ["Conservative", "Balanced", "Growth-Oriented"]
)

equity = st.slider("Equity (%)", 0, 100, 60)
debt = st.slider("Debt (%)", 0, 100, 30)
gold = st.slider("Gold (%)", 0, 100, 10)

df = pd.DataFrame({
    "Asset": ["Equity", "Debt", "Gold"],
    "Allocation": [equity, debt, gold]
})

fig = px.pie(
    df,
    names="Asset",
    values="Allocation",
    hole=0.5,
    color_discrete_sequence=["#00F0FF", "#1D8CF8", "#7FFBFF"]
)

fig.update_layout(
    showlegend=True,
    margin=dict(t=10, b=10, l=10, r=10),
    font=dict(size=14, color="#E2E8F0"),
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)"
)

st.plotly_chart(fig, use_container_width=True)

alignment = risk_alignment(profile, equity)
status_class = "status-ok" if alignment == "Well aligned with risk profile" else "status-warn"

st.markdown(
    f"""
    <div style='margin-top: 1rem;'>
        <span class='status-chip {status_class}'>Risk Alignment</span>
        <p class='muted' style='margin-top: 0.5rem;'>{alignment} for a {profile} investor.</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("</div>", unsafe_allow_html=True)
