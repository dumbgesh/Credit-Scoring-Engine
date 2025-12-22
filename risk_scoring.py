def evaluate_borrower(borrower: dict) -> dict:
    score = 600
    reasons = []

    # Hard risk: past defaults
    if borrower["past_defaults"] == "many":
        score -= 300
        reasons.append("Multiple past defaults")
    elif borrower["past_defaults"] == "few":
        score -= 100
        reasons.append("Some past defaults")

    # Core risk: debt-to-income
    dti = borrower["debt_to_income_ratio"]
    if dti < 0.30:
        score += 150
        reasons.append("Low debt-to-income ratio")
    elif dti > 0.50:
        score -= 150
        reasons.append("High debt-to-income ratio")

    # Employment stability
    if borrower["employment_status"] == "stable":
        score += 100
    elif borrower["employment_status"] == "none":
        score -= 100
        reasons.append("No stable employment")

    # Income buffer
    if borrower["income_band"] == "high":
        score += 100
    elif borrower["income_band"] == "medium":
        score += 50

    # Credit history
    if borrower["credit_history_length"] == "long":
        score += 50
    elif borrower["credit_history_length"] == "short":
        score -= 50
        reasons.append("Short credit history")

    # Age (soft modifier)
    if borrower["age_band"] == "prime":
        score += 50
    elif borrower["age_band"] == "young":
        score -= 25

    # Clamp score
    score = max(300, min(score, 900))

    # Decision logic
    if score >= 750:
        risk_band = "low"
        decision = "approve"
    elif score >= 550:
        risk_band = "medium"
        decision = "review"
    else:
        risk_band = "high"
        decision = "decline"

    return {
        "credit_score": score,
        "risk_band": risk_band,
        "decision": decision,
        "key_drivers": reasons[:3]
    }