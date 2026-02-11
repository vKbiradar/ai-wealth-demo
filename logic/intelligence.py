from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List


ASSETS = ("equity", "debt", "gold")


@dataclass
class IntelligenceReport:
    normalized_allocation: Dict[str, float]
    risk_score: float
    risk_level: str
    diversification_score: float
    expected_return: float
    expected_volatility: float
    recommendations: List[str]


RISK_PROFILES = {
    "Conservative": {
        "target": {"equity": 30.0, "debt": 55.0, "gold": 15.0},
        "return": 6.5,
        "volatility": 7.0,
    },
    "Balanced": {
        "target": {"equity": 55.0, "debt": 35.0, "gold": 10.0},
        "return": 9.0,
        "volatility": 11.0,
    },
    "Growth-Oriented": {
        "target": {"equity": 75.0, "debt": 20.0, "gold": 5.0},
        "return": 11.5,
        "volatility": 16.0,
    },
}


def _normalize(allocation: Dict[str, float]) -> Dict[str, float]:
    total = sum(max(allocation.get(asset, 0.0), 0.0) for asset in ASSETS)
    if total == 0:
        return {asset: 0.0 for asset in ASSETS}
    return {asset: round(max(allocation.get(asset, 0.0), 0.0) * 100 / total, 2) for asset in ASSETS}


def portfolio_risk_engine(allocation: Dict[str, float], profile: str) -> Dict[str, float | str]:
    normalized = _normalize(allocation)
    target = RISK_PROFILES[profile]["target"]

    mismatch = sum(abs(normalized[a] - target[a]) for a in ASSETS) / 2
    concentration = max(normalized.values())
    diversification_score = round(100 - min(concentration, 100), 2)
    risk_score = round(min(100.0, 0.6 * mismatch + 0.4 * concentration), 2)

    if risk_score < 35:
        risk_level = "Low"
    elif risk_score < 65:
        risk_level = "Medium"
    else:
        risk_level = "High"

    return {
        "risk_score": risk_score,
        "risk_level": risk_level,
        "diversification_score": diversification_score,
        "mismatch": round(mismatch, 2),
        "normalized": normalized,
    }


def optimize_portfolio(allocation: Dict[str, float], profile: str, market_view: str) -> Dict[str, float]:
    base_target = dict(RISK_PROFILES[profile]["target"])

    if market_view == "Risk-off":
        base_target["equity"] -= 8
        base_target["debt"] += 5
        base_target["gold"] += 3
    elif market_view == "Risk-on":
        base_target["equity"] += 8
        base_target["debt"] -= 5
        base_target["gold"] -= 3

    normalized_target = _normalize(base_target)

    current = _normalize(allocation)
    step = 0.4
    recommendation = {
        asset: round(current[asset] + step * (normalized_target[asset] - current[asset]), 2)
        for asset in ASSETS
    }
    return _normalize(recommendation)


def decision_support_ai(allocation: Dict[str, float], profile: str, market_view: str) -> IntelligenceReport:
    risk_view = portfolio_risk_engine(allocation, profile)
    optimized = optimize_portfolio(allocation, profile, market_view)

    base_return = RISK_PROFILES[profile]["return"]
    base_vol = RISK_PROFILES[profile]["volatility"]

    market_adjustment = {"Neutral": 0.0, "Risk-on": 1.1, "Risk-off": -1.2}[market_view]
    return_estimate = round(base_return + market_adjustment - (risk_view["mismatch"] * 0.03), 2)
    vol_estimate = round(base_vol + (risk_view["risk_score"] * 0.04), 2)

    recommendations = []
    if risk_view["risk_level"] == "High":
        recommendations.append("Trim concentration in the dominant asset bucket to reduce risk shocks.")
    if risk_view["mismatch"] > 12:
        recommendations.append("Current mix deviates from profile target. Rebalance in stages over 2-3 cycles.")
    if market_view == "Risk-off":
        recommendations.append("Increase defensive assets to preserve downside resilience.")
    elif market_view == "Risk-on":
        recommendations.append("Allow measured equity upside while maintaining profile guardrails.")
    recommendations.append(
        f"Suggested allocation: Equity {optimized['equity']}% / Debt {optimized['debt']}% / Gold {optimized['gold']}%."
    )

    return IntelligenceReport(
        normalized_allocation=risk_view["normalized"],
        risk_score=risk_view["risk_score"],
        risk_level=risk_view["risk_level"],
        diversification_score=risk_view["diversification_score"],
        expected_return=return_estimate,
        expected_volatility=vol_estimate,
        recommendations=recommendations,
    )
