def rebalance_needed(current, target, threshold=5):
    drift = current - target
    return abs(drift) > threshold, drift
