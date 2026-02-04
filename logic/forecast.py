def forecast_candidates():
    return [
        {
            "Ticker": "NVDA",
            "Theme": "AI infrastructure",
            "Volatility": "High",
            "Expected Return (1Y)": 18.5,
            "Expected Return (2Y)": 32.0
        },
        {
            "Ticker": "MSFT",
            "Theme": "Cloud + AI",
            "Volatility": "Medium",
            "Expected Return (1Y)": 12.0,
            "Expected Return (2Y)": 24.0
        },
        {
            "Ticker": "ASML",
            "Theme": "Semiconductor equipment",
            "Volatility": "Medium",
            "Expected Return (1Y)": 10.5,
            "Expected Return (2Y)": 22.5
        },
        {
            "Ticker": "LLY",
            "Theme": "Healthcare innovation",
            "Volatility": "Low",
            "Expected Return (1Y)": 9.0,
            "Expected Return (2Y)": 18.0
        },
        {
            "Ticker": "NEE",
            "Theme": "Clean energy",
            "Volatility": "Medium",
            "Expected Return (1Y)": 8.5,
            "Expected Return (2Y)": 17.0
        }
    ]


def best_pick(candidates, horizon_years):
    key = "Expected Return (1Y)" if horizon_years == 1 else "Expected Return (2Y)"
    return max(candidates, key=lambda item: item[key])
