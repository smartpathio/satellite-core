import json
import datetime
import os
import platform

class IntuitionEngine:
    """Digital Body Language Module - Analyzes market tension."""
    @staticmethod
    def analyze_tension(market_type):
        tensions = {
            "DPE": {"level": "HIGH", "signal": "Digital Ghosting detected in competitors"},
            "COMMERCE": {"level": "MEDIUM", "signal": "Rapid Tempo of new inquiries"}
        }
        return tensions.get(market_type, {"level": "LOW", "signal": "Stable market"})

def save_report(data):
    # 1. Primary save for GitHub/Web
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    
    # 2. Secondary save for Local 'Downloads' folder
    if platform.system() == "Windows":
        downloads_path = os.path.join(os.environ['USERPROFILE'], 'Downloads', 'satellite_report.json')
        try:
            with open(downloads_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            print(f"--- Local copy saved to: {downloads_path} ---")
        except Exception as e:
            print(f"--- Could not save to Downloads: {e} ---")

def generate_report():
    raw_data = [
        {
            "area": "DPE Logistics - Last Mile",
            "market": "DPE",
            "reason": "Scandinavian universities report 15% gap in winter route optimization."
        },
        {
            "area": "Eco-Commerce Packaging",
            "market": "COMMERCE",
            "reason": "Sudden surge in negative sentiment regarding plastic in deliveries (Digital Body Language: High Frustration)."
        }
    ]

    processed_analysis = []
    
    for item in raw_data:
        tension = IntuitionEngine.analyze_tension(item['market'])
        processed_analysis.append({
            "niche_or_area": item['area'],
            "market": item['market'],
            "confidence": 0.85 if tension['level'] == "HIGH" else 0.70,
            "decision": "YES" if tension['level'] == "HIGH" else "WATCH",
            "reason_short": item['reason'],
            "intuition_signal": tension['signal']
        })

    final_report = {
        "last_update": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
        "deep_analysis": processed_analysis
    }

    save_report(final_report)
    print(f"--- Report generated successfully: {final_report['last_update']} ---")

if __name__ == "__main__":
    generate_report()