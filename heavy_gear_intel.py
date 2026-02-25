class HeavyGearIntel:
    def __init__(self):
        self.market_rates = {
            "Kalmar/Reachstacker": {"min": 210, "unit": "DKK", "desc": "Logistyka Portowa (DK/SE)"},
            "Excavator (M2)": {"min": 280, "unit": "NOK", "desc": "Budowa dróg E39 (NO)"},
            "Heavy Transport/Lora": {"min": 250, "unit": "NOK", "desc": "Logistyka Prefabrykatów"}
        }

    def analyze_offer(self, machine_type, offered_rate, currency, training_provided=False):
        if machine_type not in self.market_rates:
            return {"status": "UNKNOWN", "comment": "Brak danych dla tego sprzętu."}

        target = self.market_rates[machine_type]
        is_underpaid = offered_rate < target["min"]
        
        advice = []
        if is_underpaid:
            advice.append(f"ALARM: Stawka poniżej rynkowej! Minimum to {target['min']} {target['unit']}.")
        else:
            advice.append(f"STAWKA OK: Zgodna ze standardem rynkowym dla {target['desc']}.")

        if training_provided:
            advice.append("BONUS: Firma oferuje szkolenie (Opplæring) – duży atut.")
        
        return {
            "status": "LOW" if is_underpaid else "HIGH",
            "advice": advice,
            "region": target["desc"],
            "offered": offered_rate,
            "currency": currency,
            "machine": machine_type
        }

def get_analysis():
    """Generuje merytoryczną sekcję sprzętu ciężkiego dla raportu"""
    intel = HeavyGearIntel()
    # Symulacja sprawdzenia oferty na koparkę
    res = intel.analyze_offer("Excavator (M2)", 260, "NOK", True)
    
    color = "#ef4444" if res['status'] == "LOW" else "#10b981"
    advices = "".join([f"<li>{a}</li>" for a in res['advice']])
    
    return f"""
    <div style="padding: 15px; border: 1px solid #333; border-radius: 10px; border-left: 5px solid {color};">
        <h3 style="color: {color}; margin-top:0;">Sprzęt Ciężki: {res['machine']}</h3>
        <p>Region: <strong>{res['region']}</strong></p>
        <p>Oferta: <strong>{res['offered']} {res['currency']}</strong></p>
        <ul style="margin-bottom:0;">{advices}</ul>
    </div>
    """