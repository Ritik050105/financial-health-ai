def detect_risks(data: dict):
    risks = []

    if data["liabilities"] > data["assets"]:
        risks.append("Liabilities exceed assets")

    if data["cash_flow"] < 0:
        risks.append("Negative cash flow")

    if data["expenses"] > data["revenue"]:
        risks.append("Expenses exceed revenue")

    return risks
