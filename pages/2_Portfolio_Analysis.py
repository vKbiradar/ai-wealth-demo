import streamlit as st
import pandas as pd
import plotly.express as px
from logic.portfolio import risk_alignment
from ui.theme import section

section(
    "Portfolio Assessment",
    "Visualize diversification and risk mismatch."
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
    color_discrete_sequence=["#1D4ED8", "#64748B", "#CBD5E1"]
)

fig.update_layout(
    showlegend=True,
    margin=dict(t=10, b=10, l=10, r=10),
    font=dict(size=14)
)

st.plotly_chart(fig, use_container_width=True)


