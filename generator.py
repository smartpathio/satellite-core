import json
import os
from datetime import datetime

# Ścieżka do projektu (zawsze lokalna)
PROJECT_PATH = "data.json"

def build_final_report(raw_data):
    # Tworzenie struktury raportu
    report = {
        "meta": {
            "generated_at": datetime.now().isoformat(),
            "analysis_window_days": 30,
            "markets_covered": ["US", "PL", "NO", "SE"],
            "confidence_overall": 0.88
        },
        "deep_analysis": raw_data.get('decisions', []),
        "signals": raw_data.get('signals', []),
        "warnings": raw_data.get('warnings', []),
        "comparisons": raw_data.get('comparisons', []),
        "excluded": raw_data.get('excluded', [])
    }

    # 1. Zapis do projektu (Główny plik dla Dashboardu)
    try:
        with open(PROJECT_PATH, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        print(f"✅ Plik data.json zaktualizowany w projekcie.")
    except Exception as e:
        print(f"❌ Błąd zapisu data.json: {e}")

    # 2. Bezpieczny zapis do 'Pobrane' (Tylko jeśli folder istnieje - czyli na laptopie)
    try:
        # Próba znalezienia folderu Downloads użytkownika
        downloads_path = os.path.join(os.path.expanduser("~"), "Downloads", "satellite_report.json")
        
        # Sprawdzamy, czy folder Downloads istnieje (na serwerze GitHub go nie będzie)
        if os.path.exists(os.path.dirname(downloads_path)):
            with open(downloads_path, 'w', encoding='utf-8') as f:
                json.dump(report, f, indent=2, ensure_ascii=False)
            print(f"📁 Kopia zapisana lokalnie w Pobrane: {downloads_path}")
        else:
            # To się wyświetli w logach GitHuba - i to jest OK
            print("ℹ️ Tryb chmurowy: Pominięto zapis do folderu Pobrane.")
    except Exception:
        # Jeśli cokolwiek pójdzie nie tak z Pobranymi, nie zatrzymuj bota
        print("ℹ️ Nie udało się zapisać w Pobrane (brak uprawnień lub folderu).")

    print(f"🚀 Raport wygenerowany pomyślnie o {datetime.now().strftime('%H:%M:%S')}")

# --- TESTOWE URUCHOMIENIE ---
if __name__ == "__main__":
    # To są dane, które docelowo bot będzie tu wstrzykiwał
    test_data = {
        "decisions": [
            {
                "domain": "jobs",
                "niche_or_area": "System Satellite - Restart",
                "decision": "TEST",
                "reason_short": "Naprawa błędów ścieżek dostępu. System gotowy do synchronizacji.",
                "risk_level": "low",
                "confidence": 1.0,
                "time_horizon": "short",
                "do_not": "Nie używaj ścieżek bezwzględnych (C:/) w kodzie chmurowym."
            }
        ]
    }
    build_final_report(test_data)