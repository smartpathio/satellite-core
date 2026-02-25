class SafetySentinel:
    def __init__(self):
        self.blacklisted_agencies = ["GlobalWork_Fake", "EuroJob_Scam"]
        self.mandatory_registries = ["RAZ (Denmark)", "StartBANK (Norway)", "KRAZ (Poland)"]

    def verify_agency(self, agency_name, has_bilingual_contract, asks_for_passport_original):
        score = 100
        warnings = []

        if asks_for_passport_original:
            score -= 100
            warnings.append("ALARM: Agencja wymaga oryginału paszportu! Ryzyko obozu pracy.")
        
        if not has_bilingual_contract:
            score -= 30
            warnings.append("RYZYKO: Brak umowy dwujęzycznej.")

        if agency_name in self.blacklisted_agencies:
            score = 0
            warnings.append("CZARNA LISTA: Agencja figuruje w bazach oszustw.")

        status = "BEZPIECZNA" if score > 70 else "NIEBEZPIECZNA"
        
        return {
            "status": status,
            "score": score,
            "warnings": warnings,
            "registries": self.mandatory_registries
        }

def get_analysis():
    """Generuje merytoryczny alert do raportu"""
    sentinel = SafetySentinel()
    # Symulacja sprawdzenia podejrzanej agencji
    res = sentinel.verify_agency("Unknown_Agency", True, True)
    
    color = "#ef4444" if res['status'] == "NIEBEZPIECZNA" else "#10b981"
    warn_list = "".join([f"<li style='color:#ef4444; font-weight:bold;'>⚠️ {w}</li>" for w in res['warnings']])
    regs = ", ".join(res['registries'])

    return f"""
    <div style="padding: 15px; background: rgba(239, 68, 68, 0.1); border: 2px solid {color}; border-radius: 10px;">
        <h3 style="color: {color}; margin-top:0;">STATUS: {res['status']} ({res['score']}/100)</h3>
        <ul style="list-style: none; padding: 0;">{warn_list}</ul>
        <hr style="border: 0; border-top: 1px solid #333;">
        <p style="font-size: 0.8em; color: #888;">Wymagane rejestry: {regs}</p>
    </div>
    """