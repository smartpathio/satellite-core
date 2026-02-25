import os
from pathlib import Path
from datetime import datetime
import importlib
import re

# PEŁNA LISTA TWOICH BOTÓW + NOWY ANALITYK NA GÓRZE
BOT_MODULES = [
    'ecom_trend_analyst', 
    'heavy_gear_intel', 
    'safety_sentinel', 
    'compliance_logic', 
    'accommodation_scout'
]

def get_downloads_path():
    """Lokalizuje folder Pobrane na Twoim laptopie (daw76)."""
    return Path.home() / "Downloads" / "Satellite_Master_Report.html"

def generate_executive_summary(data_dict):
    """BOT ANALITYCZNY: Wyciąga wnioski z surowych danych wszystkich botów."""
    insights = []
    combined_text = "".join(data_dict.values())

    if "DANGEROUS" in combined_text or "ALARM" in combined_text:
        insights.append("<li style='color:#ef4444;'>🚨 KRYTYCZNE: Wykryto zagrożenie bezpieczeństwa lub próbę oszustwa!</li>")
    
    if "HOT 🔥" in combined_text:
        insights.append("<li style='color:#10b981;'>📈 E-COM: Masz produkt o wysokim potencjale. Skaluj budżet.</li>")
    
    if "LOW" in combined_text or "poniżej rynkowej" in combined_text:
        insights.append("<li style='color:#eab308;'>🚜 STAWKI: Wykryto ofertę poniżej minimum rynkowego.</li>")
    
    if "PONIZEJ STANDARDU" in combined_text:
        insights.append("<li style='color:#f87171;'>🏠 KWATERY: Obecne lokum nie spełnia norm Satellite.</li>")

    if not insights:
        insights.append("<li>✅ Brak krytycznych uwag. System stabilny.</li>")

    return "".join(insights)

def collect_bot_data():
    reports = {}
    for module_name in BOT_MODULES:
        try:
            module = importlib.import_module(module_name)
            importlib.reload(module)
            if hasattr(module, 'get_analysis'):
                reports[module_name] = module.get_analysis()
            else:
                reports[module_name] = f"<p>⚠️ Moduł {module_name} bez danych.</p>"
        except Exception as e:
            reports[module_name] = f"<p style='color:red;'>❌ Błąd {module_name}: {str(e)}</p>"
    return reports

def generate_final_dashboard():
    print("🚀 SATELLITE CORE v10.0: Generowanie inteligentnego raportu...")
    
    data = collect_bot_data()
    summary = generate_executive_summary(data)
    now = datetime.now().strftime("%d.%m.%Y | %H:%M:%S")
    dest = get_downloads_path()

    html = f"""
    <!DOCTYPE html>
    <html lang="pl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>SATELLITE COMMAND CENTER v10.0</title>
        <style>
            :root {{ --bg: #050505; --card: #111; --accent: #2563eb; --danger: #ef4444; --text: #e2e8f0; --gold: #eab308; }}
            body {{ font-family: 'Segoe UI', system-ui, sans-serif; background: var(--bg); color: var(--text); padding: 15px; margin: 0; }}
            .container {{ max-width: 900px; margin: auto; }}
            .header {{ border-bottom: 2px solid var(--accent); padding: 20px 0; margin-bottom: 30px; text-align: center; }}
            .summary-box {{ background: linear-gradient(45deg, #1e1b4b, #0f172a); border: 2px solid var(--accent); border-radius: 15px; padding: 20px; margin-bottom: 30px; }}
            .card {{ background: var(--card); border-radius: 12px; padding: 20px; margin-bottom: 20px; border-left: 6px solid var(--accent); border: 1px solid #222; }}
            .card-danger {{ border-left: 6px solid var(--danger); }}
            h1 {{ margin: 0; color: var(--accent); letter-spacing: 2px; text-transform: uppercase; }}
            h2 {{ color: var(--accent); font-size: 0.9rem; text-transform: uppercase; margin: 0 0 15px 0; border-bottom: 1px solid #222; }}
            ul {{ padding-left: 20px; }}
            .footer {{ text-align: center; font-size: 0.8rem; color: #444; margin-top: 50px; padding: 20px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>🛰️ SATELLITE COMMAND</h1>
                <p>STATUS: <strong style="color:var(--accent)">INTEL ANALYST ACTIVE</strong> | {now}</p>
            </div>

            <div class="summary-box">
                <h2 style="color: #818cf8;">🧠 STRATEGIC OVERVIEW (WNIOSKI)</h2>
                <ul style="font-size: 1.1em; font-weight: bold;">{summary}</ul>
            </div>

            <div class="card"><h2>📈 E-COMMERCE</h2>{data.get('ecom_trend_analyst')}</div>
            <div class="card"><h2>🚜 HEAVY GEAR</h2>{data.get('heavy_gear_intel')}</div>
            <div class="card card-danger"><h2>🛡️ SAFETY ALERTS</h2>{data.get('safety_sentinel')}</div>
            <div class="card"><h2>🏠 ACCOMMODATION</h2>{data.get('accommodation_scout')}</div>
            <div class="card"><h2>⚖️ COMPLIANCE</h2>{data.get('compliance_logic')}</div>

            <div class="footer">SATELLITE CORE v10.0 | daw76 | Authorized Only</div>
        </div>
    </body>
    </html>
    """
    with open(dest, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✅ RAPORT ZAPISANY: {dest}")

if __name__ == "__main__":
    generate_final_dashboard()