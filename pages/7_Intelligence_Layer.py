import streamlit as st
import pandas as pd
import plotly.express as px

from logic.intelligence import decision_support_ai
from ui.theme import section

if not st.session_state.get("customer_logged_in"):
    st.warning("Customer access required. Please log in from the home page.")
    if st.button("Go to Login"):
        st.switch_page("app.py")
    st.stop()

section(
    "Intelligence Layer",
    "Decision-support AI with portfolio optimizer and integrated risk engine."
)

left, right = st.columns([1.1, 1])

with left:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("#### Input portfolio")

    profile = st.selectbox(
        "Investor Profile",
        ["Conservative", "Balanced", "Growth-Oriented"],
        index=1,
    )
    market_view = st.selectbox("Market Regime", ["Neutral", "Risk-on", "Risk-off"])

    equity = st.slider("Equity (%)", 0, 100, 55)
    debt = st.slider("Debt (%)", 0, 100, 35)
    gold = st.slider("Gold (%)", 0, 100, 10)

    if st.button("Run Decision-Support AI"):
        st.session_state["intelligence_report"] = decision_support_ai(
            {"equity": equity, "debt": debt, "gold": gold},
            profile,
            market_view,
        )

    st.markdown("</div>", unsafe_allow_html=True)

report = st.session_state.get("intelligence_report")

with right:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("#### Platform coverage")
    st.markdown("✔ Intelligence layer on top of existing platforms")
    st.markdown("✔ Decision-support AI")
    st.markdown("✔ Portfolio optimizer + risk engine")
    st.markdown("</div>", unsafe_allow_html=True)

if report:
    metrics = st.columns(4)
    metrics[0].metric("Risk Score", f"{report.risk_score}/100")
    metrics[1].metric("Risk Level", report.risk_level)
    metrics[2].metric("Diversification", f"{report.diversification_score}/100")
    metrics[3].metric("Expected Return", f"{report.expected_return}%")

    allocation_df = pd.DataFrame(
        {
            "Asset": ["Equity", "Debt", "Gold"],
            "Allocation": [
                report.normalized_allocation["equity"],
                report.normalized_allocation["debt"],
                report.normalized_allocation["gold"],
            ],
        }
    )

    fig = px.bar(
        allocation_df,
        x="Asset",
        y="Allocation",
        color="Asset",
        color_discrete_sequence=["#00F0FF", "#1D8CF8", "#7FFBFF"],
        title="Current allocation (normalized)",
    )
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#E2E8F0"),
        showlegend=False,
    )
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("#### AI recommendations")
    for rec in report.recommendations:
        st.markdown(f"- {rec}")

    st.caption(
        f"Model output for educational decision support only. Estimated volatility: {report.expected_volatility}%"
    )
else:
    st.info("Run the intelligence engine to generate your portfolio decision-support report.")
