import numpy as np

def project_values(initial=100, years=10):
    return {
        "Pessimistic": [initial * (1.05 ** i) for i in range(years)],
        "Base": [initial * (1.10 ** i) for i in range(years)],
        "Optimistic": [initial * (1.14 ** i) for i in range(years)]
    }
