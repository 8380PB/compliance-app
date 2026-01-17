def calculate_risk():
    return {
        "procedural_compliance": 18,
        "structural_consistency": 12,
        "counterparty_signals": 35,
        "payment_logic": 22,
        "document_integrity": 9
    }

def overall_score(scores):
    return round(sum(scores.values()) / len(scores))