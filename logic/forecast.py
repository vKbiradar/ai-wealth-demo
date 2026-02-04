import pandas as pd
import streamlit as st


STOOQ_BASE_URL = "https://stooq.com/q/d/l/?s={ticker}.us&i=d"
DEFAULT_TICKERS = ["AAPL", "MSFT", "NVDA", "AMZN", "GOOGL", "TSLA"]


@st.cache_data(show_spinner=False)
def fetch_price_history(ticker):
    url = STOOQ_BASE_URL.format(ticker=ticker.lower())
    try:
        data = pd.read_csv(url)
    except Exception:
        return pd.DataFrame()
    if data.empty:
        return pd.DataFrame()
    data["Date"] = pd.to_datetime(data["Date"], errors="coerce")
    return data.dropna(subset=["Date", "Close"]).sort_values("Date")


def compute_trailing_return(data, years):
    if data.empty:
        return None
    latest = data.iloc[-1]
    cutoff = latest["Date"] - pd.DateOffset(years=years)
    past = data[data["Date"] <= cutoff]
    if past.empty:
        return None
    past_close = past.iloc[-1]["Close"]
    if past_close == 0:
        return None
    return round(((latest["Close"] / past_close) - 1) * 100, 2)


def build_forecast_table(tickers):
    rows = []
    for ticker in tickers:
        data = fetch_price_history(ticker)
        if data.empty:
            continue
        one_year = compute_trailing_return(data, 1)
        two_year = compute_trailing_return(data, 2)
        rows.append(
            {
                "Ticker": ticker,
                "Latest Price": round(data.iloc[-1]["Close"], 2),
                "Signal": "Momentum" if one_year and one_year > 0 else "Neutral",
                "Expected Return (1Y)": one_year,
                "Expected Return (2Y)": two_year
            }
        )
    return pd.DataFrame(rows).sort_values("Expected Return (1Y)", ascending=False)


def pick_best_candidate(table, horizon_years):
    key = "Expected Return (1Y)" if horizon_years == 1 else "Expected Return (2Y)"
    usable = table.dropna(subset=[key])
    if usable.empty:
        return None
    best_row = usable.sort_values(key, ascending=False).iloc[0]
    return {
        "Ticker": best_row["Ticker"],
        "Signal": best_row["Signal"],
        "Expected Return (%)": best_row[key],
        "Latest Price": best_row["Latest Price"]
    }


def forecast_candidates():
    table = build_forecast_table(DEFAULT_TICKERS)
    return table.to_dict(orient="records")


def best_pick(candidates, horizon_years):
    if isinstance(candidates, list):
        table = pd.DataFrame(candidates)
    else:
        table = build_forecast_table(DEFAULT_TICKERS)
    return pick_best_candidate(table, horizon_years)
