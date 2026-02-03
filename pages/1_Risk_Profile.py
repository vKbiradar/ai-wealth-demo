import streamlit as st
from logic.risk import calculate_risk_score, risk_label
from ui.theme import section

section(
    "Risk Profiling",
    "Behavioural assessment before portfolio construction."
)

with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    horizon = st.selectbox(
        "Investment Horizon",
        ["Less than 3 years", "3–7 years", "7+ years"]
    )

    drawdown = st.selectbox(
        "Maximum acceptable drawdown",
        ["5%", "10%", "20%+"]
    )

    if st.button("Generate Risk Profile"):
        score = calculate_risk_score(horizon, drawdown)
        label = risk_label(score)

        st.success(f"Risk Score: {score}/100")
        st.markdown(f"**Investor Profile:** {label}")

    st.markdown("</div>", unsafe_allow_html=True)

