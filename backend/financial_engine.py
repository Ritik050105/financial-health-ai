def financial_health_score(data: dict) -> float:
    liquidity = data["assets"] / max(data["liabilities"], 1)
    profitability = (data["revenue"] - data["expenses"]) / max(data["revenue"], 1)
    cash_ratio = data["cash_flow"] / max(data["expenses"], 1)

    score = (liquidity * 30) + (profitability * 40) + (cash_ratio * 30)
    return round(min(score, 100), 2)
