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

        verdict = "SATELLITE STANDARD ✅" if score == 100 else "PONIZEJ STANDARDU ❌"
        
        return {
            "verdict": verdict,
            "score": score,
            "type": housing_type,
            "size": size,
            "missing": [a for a in self.required_amenities if a not in amenities] if not has_all_amenities else [],
            "price": price_pln
        }

def get_analysis():
    """Generuje merytoryczną sekcję kwaterunku dla raportu"""
    scout = AccommodationScout()
    # Symulacja sprawdzenia mieszkania (przykładowe dane)
    res = scout.evaluate_housing("Private Studio", 22, ["washing machine", "high-speed internet"], 3500)
    
    color = "#10b981" if res['score'] == 100 else "#ef4444"
    missing_info = f"<p style='color:#ef4444;'><strong>Braki:</strong> {', '.join(res['missing'])}</p>" if res['missing'] else "<p style='color:#10b981;'>Pełne wyposażenie.</p>"

    return f"""
    <div style="padding: 15px; border: 1px solid #333; border-radius: 10px; border-left: 5px solid {color};">
        <h3 style="color: {color}; margin-top:0;">Kwaterunek: {res['verdict']} ({res['score']}/100)</h3>
        <p>Typ: <strong>{res['type']}</strong> | Powierzchnia: <strong>{res['size']} m²</strong></p>
        <p>Koszt: <strong>{res['price']} PLN</strong></p>
        {missing_info}
    </div>
    """