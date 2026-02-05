def credit_rating(score):
    if score >= 80:
        return "A", "Excellent financial health"
    if score >= 65:
        return "B", "Moderate financial health with manageable risks"
    if score >= 50:
        return "C", "Weak financial position"
    return "D", "High financial risk"
