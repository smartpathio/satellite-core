# labor_scout.py

class LaborScout:
    def __init__(self):
        # Your specific thresholds and data points
        self.min_hourly_pln = 30.0
        self.currencies = {
            "NOK": 0.38, # Example rates - we will automate this later
            "SEK": 0.37,
            "DKK": 0.58
        }
        
    def analyze_opportunity(self, location, hourly_rate, currency, housing_cost_local):
        """
        Calculates if a job abroad is worth the relocation vs Poland base.
        """
        # Convert to PLN
        rate_in_pln = hourly_rate * self.currencies.get(currency, 1.0)
        monthly_gross_pln = rate_in_pln * 160 # Standard month
        housing_pln = housing_cost_local * self.currencies.get(currency, 1.0)
        
        net_after_housing = monthly_gross_pln - housing_pln
        
        status = "🟢 HIGH YIELD" if rate_in_pln > 100 else "🟡 STABLE" 
        if rate_in_pln < self.min_hourly_pln:
            status = "🔴 LOW YIELD"

        return {
            "location": location,
            "pln_hourly": round(rate_in_pln, 2),
            "net_after_housing_pln": round(net_after_housing, 2),
            "status": status
        }

# Quick Test for Denmark (280 DKK/h)
scout = LaborScout()
denmark = scout.analyze_opportunity("Denmark (CNC)", 280, "DKK", 7500)
print(f"Audit for Denmark: {denmark}")