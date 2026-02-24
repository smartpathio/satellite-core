class AccommodationScout:
    def __init__(self):
        self.min_sq_meters = 25
        self.required_amenities = ["washing machine", "high-speed internet", "private kitchen"]

    def evaluate_housing(self, housing_type, size, amenities, price_pln):
        is_private = "shared" not in housing_type.lower()
        has_all_amenities = all(a in amenities for a in self.required_amenities)
        
        score = 0
        if is_private: score += 50
        if size >= self.min_sq_meters: score += 25
        if has_all_amenities: score += 25

        verdict = "SATELLITE STANDARD ✅" if score == 100 else "UNACCEPTABLE ❌"
        
        return {
            "verdict": verdict,
            "score": score,
            "missing": [a for a in self.required_amenities if a not in amenities] if not has_all_amenities else "None"
        }