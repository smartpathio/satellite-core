import json
import os
from datetime import datetime

# Ścieżka do Twojego folderu Pobrane
DOWNLOADS_PATH = os.path.join(os.path.expanduser("~"), "Downloads", "satellite_report.json")
# Ścieżka do pliku w projekcie (dla dashboardu)
PROJECT_PATH = "data.json"

def build_final_report(raw_data):
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

    # 1. Zapis do projektu (żeby dashboard od razu to widział)
    with open(PROJECT_PATH, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    # 2. Kopia do folderu Pobrane (Twój wymóg)
    with open(DOWNLOADS_PATH, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    print(f"✅ Raport wygenerowany: {datetime.now().strftime('%H:%M:%S')}")
    print(f"📁 Kopia zapisana w Pobrane: {DOWNLOADS_PATH}")

# PRZYKŁAD UŻYCIA (Bot tu wrzuca to co znalazł):
test_data = {
    "decisions": [
        {
            "domain": "jobs",
            "niche_or_area": "Operator Kalmar - Drammen",
            "decision": "TEST",
            "reason_short": "Wysoki popyt w porcie, stawki 400+ NOK.",
            "risk_level": "low",
            "confidence": 0.95,
            "time_horizon": "short",
            "do_not": "Nie jedź bez certyfikatu UDT/T1-T4."
        }
    ]
}

if __name__ == "__main__":
    build_final_report(test_data)