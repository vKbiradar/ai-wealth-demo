def risk_alignment(risk_label, equity_pct):
    ideal_ranges = {
        "Conservative": (0, 40),
        "Balanced": (40, 70),
        "Growth-Oriented": (70, 100)
    }

    low, high = ideal_ranges[risk_label]

    if equity_pct < low:
        return "Underexposed to equity"
    elif equity_pct > high:
        return "Overexposed to equity"
    else:
        return "Well aligned with risk profile"
