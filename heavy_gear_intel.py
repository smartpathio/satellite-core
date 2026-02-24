class HeavyGearIntel:
    def __init__(self):
        self.market_rates = {
            "Kalmar/Reachstacker": {"min": 210, "unit": "DKK", "desc": "Port Logistics (DK/SE)"},
            "Excavator (M2)": {"min": 280, "unit": "NOK", "desc": "Road Construction E39"},
            "Heavy Transport/Lora": {"min": 250, "unit": "NOK", "desc": "Prefab Logistics"}
        }

    def analyze_offer(self, machine_type, offered_rate, currency, training_provided=False):
        if machine_type not in self.market_rates:
            return {"status": "UNKNOWN", "comment": "No data for this equipment."}

        target = self.market_rates[machine_type]
        is_underpaid = offered_rate < target["min"]
        
        advice = []
        if is_underpaid:
            advice.append(f"ALARM: Underpaid for {machine_type}. Minimum is {target['min']} {target['unit']}.")
        else:
            advice.append(f"RATE OK: Matches market standard for {target['desc']}.")

        if training_provided:
            advice.append("BONUS: Company offers training (Opplæring) - good for beginners.")
        
        return {
            "status": "LOW" if is_underpaid else "HIGH",
            "advice": advice,
            "region": target["desc"]
        }