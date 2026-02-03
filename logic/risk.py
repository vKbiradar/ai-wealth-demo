def calculate_risk_score(horizon, drawdown):
    score = 0

    horizon_map = {
        "Less than 3 years": 15,
        "3–7 years": 35,
        "7+ years": 55
    }

    drawdown_map = {
        "5%": 15,
        "10%": 30,
        "20%+": 45
    }

    score += horizon_map[horizon]
    score += drawdown_map[drawdown]

    return min(score, 100)


def risk_label(score):
    if score < 40:
        return "Conservative"
    elif score < 70:
        return "Balanced"
    else:
        return "Growth-Oriented"
