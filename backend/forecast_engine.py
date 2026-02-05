def forecast_cash_flow(cash_flow):
    return {
        "Q1": round(cash_flow * 0.85, 2),
        "Q2": round(cash_flow * 0.95, 2),
        "Q3": round(cash_flow * 1.05, 2),
        "Q4": round(cash_flow * 1.15, 2),
    }
