import json
import datetime

class IntuitionEngine:
    """Digital Body Language Module - Analyzes market tension."""
    @staticmethod
    def analyze_tension(market_type):
        # Tension simulation - logic based on digital activity patterns
        tensions = {
            "DPE": {"level": "HIGH", "signal": "Digital Ghosting detected in competitors"},
            "COMMERCE": {"level": "MEDIUM", "signal": "Rapid Tempo of new inquiries"}
        }
        return tensions.get(market_type, {"level": "LOW", "signal": "Stable market"})

def generate_report():
    # 1. Gather data from academic/market signals
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
    
    # 2. Process through Intuition Module
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

    # 3. Construct final report structure
    final_report = {
        "last_update": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
        "deep_analysis": processed_analysis
    }

    # 4. Save to data.json
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(final_report, f, indent=4, ensure_ascii=False)
    
    print(f"--- Report generated successfully: {final_report['last_update']} ---")

if __name__ == "__main__":
    generate_report()