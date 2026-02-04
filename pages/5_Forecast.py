import pandas as pd
import streamlit as st
from logic.forecast import build_forecast_table, pick_best_candidate
from ui.theme import section

section(
    "Forecast Lab",
    "Live data-driven outlook for 1–2 year horizons."
)

st.markdown("<div class='card'>", unsafe_allow_html=True)

horizon = st.selectbox(
    "Forecast Horizon",
    [1, 2],
    format_func=lambda value: f"{value} year"
)

tickers = st.multiselect(
    "Select Tickers",
    ["AAPL", "MSFT", "NVDA", "AMZN", "GOOGL", "TSLA"],
    default=["AAPL", "MSFT", "NVDA", "AMZN"]
)

table = build_forecast_table(tickers)

if table.empty:
    st.warning("No live data returned. Try again later or adjust tickers.")
else:
    st.dataframe(
        table,
        width="stretch",
        hide_index=True
    )

    best = pick_best_candidate(table, horizon)
    if best:
        st.markdown(
            f"""
            <div class="card" style="margin-top: 1rem;">
                <h4>Top Pick ({horizon}Y)</h4>
                <p class="muted">{best['Ticker']} · {best['Signal']}</p>
                <p><strong>Expected Return:</strong> {best['Expected Return (%)']}%</p>
                <p class="muted">Latest Price: ${best['Latest Price']}</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.info("Not enough history to score picks for this horizon.")

st.caption(
    "Signals are based on trailing price returns from a free live-data source."
)

st.markdown("</div>", unsafe_allow_html=True)
