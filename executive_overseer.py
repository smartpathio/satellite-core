import os
from pathlib import Path
import re

class ExecutiveOverseer:
    def __init__(self):
        self.report_path = Path.home() / "Downloads" / "Satellite_Master_Report.html"

    def extract_strategic_insights(self):
        if not self.report_path.exists():
            return "❌ Błąd: Nie znaleziono raportu do analizy."

        with open(self.report_path, "r", encoding="utf-8") as f:
            content = f.read()

        insights = []

        # 1. Szukanie Alertów Bezpieczeństwa
        if "DANGEROUS" in content or "ALARM" in content:
            insights.append("🔴 KRYTYCZNE: Masz aktywne zagrożenie bezpieczeństwa! Sprawdź sekcję Safety Sentinel.")

        # 2. Szukanie Okazji E-com
        if "HOT 🔥" in content:
            product_match = re.search(r"Produkt: (.*?) - HOT 🔥", content)
            prod_name = product_match.group(1) if product_match else "E-com"
            insights.append(f"🟢 OKAZJA: {prod_name} ma wysoki potencjał viralowy. Rozważ zwiększenie budżetu.")

        # 3. Szukanie problemów ze stawkami
        if "LOW" in content or "poniżej rynkowej" in content:
            insights.append("🟡 NEGOCJACJE: Wykryto zaniżoną stawkę za sprzęt. Przygotuj kontrofertę.")

        # 4. Problemy z kwaterunkiem
        if "PONIZEJ STANDARDU" in content:
            insights.append("🏠 MIESZKANIE: Obecna oferta zakwaterowania nie spełnia norm Satellite (braki w wyposażeniu).")

        return insights

def get_executive_summary():
    overseer = ExecutiveOverseer()
    actions = overseer.extract_strategic_insights()
    
    if isinstance(actions, str): return actions

    action_items = "".join([f"<li style='margin-bottom:10px;'>{a}</li>" for a in actions])
    
    return f"""
    <div style="background: linear-gradient(45deg, #1e1b4b, #312e81); padding: 20px; border-radius: 15px; border: 2px solid #4f46e5; margin-bottom: 30px;">
        <h2 style="color: #818cf8; margin-top: 0;">🧠 SATELLITE COMMAND: WNIOSKI I REKOMENDACJE</h2>
        <ul style="color: #e2e8f0; font-weight: bold; font-size: 1.1em; list-style-type: '🚀 ';">
            {action_items}
        </ul>
    </div>
    """