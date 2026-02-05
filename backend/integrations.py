def mock_bank_products(credit_rating):
    return {
        "A": ["HDFC Working Capital Loan", "ICICI OD Facility"],
        "B": ["NBFC Credit Line", "Invoice Discounting"],
        "C": ["Microfinance Loan"],
        "D": []
    }.get(credit_rating, [])


def mock_gst_status():
    return {
        "gst_status": "Filed",
        "last_return": "GSTR-3B",
        "compliance_score": 92
    }
