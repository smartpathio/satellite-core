import os
from pathlib import Path
from bs4 import BeautifulSoup  # Biblioteka do czytania i analizy HTML

class SatelliteBrain:
    def __init__(self):
        # Ścieżka do raportu w Twoim folderze Pobrane
        self.report_path = Path.home() / "Downloads" / "Satellite_Master_Report.html"

    def analyze_existing_report(self):
        """Analizuje treść raportu i zamienia dane na konkretne rozkazy."""
        if not self.report_path.exists():
            return ["❌ Brak raportu w Downloads. Odpal silnik, aby wygenerować dane."]

        try:
            with open(self.report_path, "r", encoding="utf-8") as f:
                soup = BeautifulSoup(f, "html.parser")
            
            # Pobieramy czysty tekst z pliku HTML, żeby bot mógł go analizować
            full_text = soup.get_text()
            briefing = []
            
            # --- LOGIKA DECYZYJNA ---
            
            # 1. Sprawdzanie Bezpieczeństwa
            if "NIEBEZPIECZNA" in full_text or "oryginału paszportu" in full_text:
                briefing.append("‼️ [KRYTYCZNE] Wykryto próbę przejęcia paszportu. Natychmiast zablokuj tę ofertę!")
                
            # 2. Sprawdzanie Okazji E-commerce
            if "HOT 🔥" in full_text:
                briefing.append("💰 [SKALUJ] Portable Blender ma wysoki SSR. Zwiększ budżet na reklamy o 20%.")
                
            # 3. Sprawdzanie Stawek (Heavy Gear)
            if "poniżej rynkowej" in full_text:
                briefing.append("🚜 [NEGOCJUJ] Stawka 260 NOK jest za niska. Żądaj wyrównania do standardu 280 NOK.")

            # 4. Sprawdzanie Kwaterunku
            if "PONIZEJ STANDARDU" in full_text:
                briefing.append("🏠 [ODRZUĆ] Kwatera nie spełnia norm (brak prywatnej kuchni). Szukaj innego lokum.")

            if not briefing:
                briefing.append("✅ [STATUS] Raport przeanalizowany. Brak krytycznych alertów.")

            return briefing

        except Exception as e:
            return [f"❌ Błąd analizy mózgu: {str(e)}"]

def get_analysis():
    """Funkcja wywoływana przez app_master_engine.py"""
    brain = SatelliteBrain()
    recommendations = brain.analyze_existing_report()
    
    # Tworzenie merytorycznego wyglądu dla sekcji Briefingu
    items = "".join([f"<li style='padding:12px; border-bottom:1px solid #222; border-left:4px solid #2563eb; margin-bottom:5px; background:#0a0a0a;'>{r}</li>" for r in recommendations])
    
    return f"""
    <div style="background: #000; border: 2px solid #2563eb; color: #fff; padding: 20px; border-radius: 15px; margin-bottom: 30px; box-shadow: 0 0 20px rgba(37, 99, 235, 0.2);">
        <h2 style="color: #2563eb; margin-top: 0; text-transform: uppercase; letter-spacing: 2px; font-size: 1.2em;">🛰️ SATELLITE BRAIN: BRIEFING OPERACYJNY</h2>
        <ul style="list-style-type: none; padding: 0; font-family: 'Segoe UI', sans-serif;">
            {items}
        </ul>
        <p style="font-size: 0.75em; color: #444; margin-top: 15px; text-align: right;">System analizy automatycznej v10.0</p>
    </div>
    """