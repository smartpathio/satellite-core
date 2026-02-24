import os
import sys
import io
from datetime import datetime

# Importing your army of bots (ensure these files are in the same folder)
from compliance_logic import IPNCompliance
from safety_sentinel import SafetySentinel
from accommodation_scout import AccommodationScout
from heavy_gear_intel import HeavyGearIntel
from ecom_trend_analyst import EcomTrendAnalyst

# Fixing encoding for environments to handle emojis and special characters
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

class MasterEngine:
    def __init__(self):
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        
        # SMART PATH LOGIC:
        # Detects if running on GitHub Actions server or local machine
        if os.environ.get('GITHUB_ACTIONS'):
            # Path for GitHub environment
            self.output_path = "Satellite_Master_Report.html"
        else:
            # Path for your local laptop (Downloads folder)
            self.output_path = os.path.join(os.path.expanduser("~"), "Downloads", "Satellite_Master_Report.html")
        
        # Bot Initialization
        self.finance = IPNCompliance()
        self.safety = SafetySentinel()
        self.housing = AccommodationScout()
        self.gear = HeavyGearIntel()
        self.ecom = EcomTrendAnalyst()

    def generate_html_report(self, results):
        """
        Generates the final responsive HTML report with PL/EN toggles.
        """
        html_content = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>SATELLITE INTELLIGENCE v7.0</title>
            <style>
                :root {{ --bg: #050505; --card: #111111; --accent: #2563eb; --text: #e2e8f0; --safe: #10b981; --danger: #ef4444; --purple: #a855f7; --gold: #eab308; }}
                body {{ font-family: 'Inter', -apple-system, sans-serif; background: var(--bg); color: var(--text); margin: 0; padding: 15px; }}
                .container {{ max-width: 900px; margin: auto; }}
                .card {{ background: var(--card); border: 1px solid #262626; border-radius: 12px; padding: 25px; margin-bottom: 25px; border-left: 5px solid var(--accent); transition: transform 0.2s; }}
                .header-row {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; }}
                .bot-tag {{ font-size: 0.7rem; font-weight: 800; background: #1e293b; padding: 4px 10px; border-radius: 4px; color: var(--accent); text-transform: uppercase; }}
                .lang-btn {{ background: #1f2937; border: none; color: #94a3b8; padding: 6px 15px; border-radius: 5px; cursor: pointer; font-weight: bold; font-size: 11px; }}
                .lang-btn.active {{ background: var(--accent); color: white; }}
                .hidden {{ display: none !important; }}
                .rx-box {{ background: rgba(16, 185, 129, 0.05); border: 1px solid var(--safe); border-radius: 8px; padding: 15px; margin-top: 15px; }}
                .alert-box {{ background: rgba(239, 68, 68, 0.1); border: 1px solid var(--danger); border-radius: 8px; padding: 15px; margin-top: 15px; }}
                .grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }}
                .box {{ background: #0a0a0a; padding: 15px; border-radius: 8px; border: 1px solid #1f2937; }}
                h2 {{ margin: 0; font-size: 1.5rem; }}
                ul {{ padding-left: 20px; }}
                @media (max-width: 600px) {{ .grid {{ grid-template-columns: 1fr; }} }}
            </style>
            <script>
                function toggleLang(cardId, lang) {{
                    const card = document.getElementById(cardId);
                    card.querySelectorAll('.lang-pl, .lang-en').forEach(el => el.classList.add('hidden'));
                    card.querySelectorAll('.lang-' + lang).forEach(el => el.classList.remove('hidden'));
                    card.querySelectorAll('.lang-btn').forEach(btn => btn.classList.remove('active'));
                    card.querySelector('.btn-' + lang).classList.add('active');
                }}
            </script>
        </head>
        <body>
            <div class="container">
                <header style="padding: 20px 0; border-bottom: 1px solid #262626; margin-bottom: 30px;">
                    <h1 style="margin:0; font-size: 2.2rem; letter-spacing: -1px;">🛰️ SATELLITE <span style="color:var(--accent)">CORE</span></h1>
                    <p style="color:#64748b;">Daily Operational Intelligence | {self.timestamp}</p>
                </header>

                <div class="card" id="ecom-card" style="border-left-color: var(--purple);">
                    <div class="header-row">
                        <span class="bot-tag">Bot: E-Com Trend Analyst</span>
                        <div style="display:flex; gap:5px;">
                            <button class="lang-btn btn-pl active" onclick="toggleLang('ecom-card','pl')">PL</button>
                            <button class="lang-btn btn-en" onclick="toggleLang('ecom-card','en')">EN</button>
                        </div>
                    </div>
                    <div class="lang-pl">
                        <h2>E-Commerce: {results['ecom']['product_name']}</h2>
                        <div class="grid">
                            <div class="box"><h3>Status rynkowy</h3><p>{results['ecom']['verdict']}</p></div>
                            <div class="box"><h3>Zysk Netto</h3><p>{results['ecom']['profit']} PLN</p></div>
                        </div>
                        <div class="rx-box">
                            <h4>📋 ZALECENIA OPERACYJNE:</h4>
                            <ul>{"".join([f"<li>{a}</li>" for a in results['ecom']['advice_pl']])}</ul>
                        </div>
                    </div>
                    <div class="lang-en hidden">
                        <h2>E-Commerce: {results['ecom']['product_name']}</h2>
                        <div class="grid">
                            <div class="box"><h3>Market Status</h3><p>{results['ecom']['verdict']}</p></div>
                            <div class="box"><h3>Net Profit</h3><p>{results['ecom']['profit']} PLN</p></div>
                        </div>
                        <div class="rx-box">
                            <h4>📋 OPERATIONAL ADVICE:</h4>
                            <ul>{"".join([f"<li>{a}</li>" for a in results['ecom']['advice_en']])}</ul>
                        </div>
                    </div>
                </div>

                <div class="card" id="safety-card" style="border-left-color: var(--danger);">
                    <div class="header-row">
                        <span class="bot-tag">Bot: Safety Sentinel</span>
                        <div style="display:flex; gap:5px;">
                            <button class="lang-btn btn-pl active" onclick="toggleLang('safety-card','pl')">PL</button>
                            <button class="lang-btn btn-en" onclick="toggleLang('safety-card','en')">EN</button>
                        </div>
                    </div>
                    <div class="lang-pl">
                        <h2>Weryfikacja Bezpieczeństwa Agencji</h2>
                        <div class="alert-box">
                            <h4>🛡️ STATUS: {results['safety']['status']} (Wynik: {results['safety']['score']}/100)</h4>
                            <ul>{"".join([f"<li>{w}</li>" for w in results['safety']['warnings_pl']])}</ul>
                        </div>
                    </div>
                    <div class="lang-en hidden">
                        <h2>Agency Safety Verification</h2>
                        <div class="alert-box">
                            <h4>🛡️ STATUS: {results['safety']['status']} (Score: {results['safety']['score']}/100)</h4>
                            <ul>{"".join([f"<li>{w}</li>" for w in results['safety']['warnings_en']])}</ul>
                        </div>
                    </div>
                </div>
            </div>
        </body>
        </html>
        """
        with open(self.output_path, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"✅ FINAL REPORT GENERATED: {self.output_path}")

    def run_daily_check(self):
        """
        Main operation loop collecting data from sub-bots.
        """
        # 1. E-Commerce Analysis
        ecom_data = self.ecom.analyze_viral_potential("Portable Blender", 4.8)
        ecom_data['advice_pl'] = ["Skaluj reklamy na TikTok", "Zwiększ zapasy o 20%"]
        ecom_data['advice_en'] = ["Scale ads on TikTok", "Increase inventory by 20%"]
        ecom_data['profit'] = self.finance.calculate_net_profit(40, 129)
        ecom_data['product_name'] = "Portable Blender"

        # 2. Safety Verification
        safety_data = self.safety.verify_agency("NordicWork_Test", True, True)
        safety_data['warnings_pl'] = ["ALARM: Próba zatrzymania paszportu!", "Ryzyko obozu pracy."]
        safety_data['warnings_en'] = ["ALARM: Passport retention attempt!", "Labor camp risk."]

        # 3. Logistics & Gear
        housing_data = self.housing.evaluate_housing("Private Studio", 28, ["washing machine", "high-speed internet", "private kitchen"], 3500)
        gear_data = self.gear.analyze_offer("Kalmar/Reachstacker", 190, "DKK", True)
        gear_data['machine'] = "Kalmar/Reachstacker"
        gear_data['advice_pl'] = ["Stawka za niska, ale oferują przyuczenie."]
        gear_data['advice_en'] = ["Rate too low, but they offer training."]

        # Aggregating all results
        master_results = {
            "ecom": ecom_data,
            "safety": safety_data,
            "housing": housing_data,
            "gear": gear_data
        }

        # 4. Generate report
        self.generate_html_report(master_results)

if __name__ == "__main__":
    engine = MasterEngine()
    engine.run_daily_check()