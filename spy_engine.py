import json
import datetime
import os
import platform
import feedparser

class IntuitionEngine:
    @staticmethod
    def analyze_tension(text):
        high_tension_words = ['delay', 'strike', 'crisis', 'increase', 'problem', 'failure', 'surge', 'trouble']
        text_lower = text.lower()
        if any(word in text_lower for word in high_tension_words):
            return {"level": "HIGH", "signal": "Disruption Alert: Volatility detected in this sector."}
        return {"level": "LOW", "signal": "Stable flow: Standard market movement."}

def save_report(data):
    # 1. Save for GitHub/Web
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print("✅ File data.json saved.")
    
    # 2. Local backup for Windows
    if platform.system() == "Windows":
        downloads_path = os.path.join(os.environ['USERPROFILE'], 'Downloads', 'satellite_report.json')
        try:
            with open(downloads_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            print(f"✅ Backup saved to Downloads: {downloads_path}")
        except Exception as e:
            print(f"❌ Backup failed: {e}")

def generate_report():
    print("--- 🛰️  Starting deep market scan... ---")
    
    feeds = [
        "https://ecommercenews.eu/feed/",
        "https://www.logisticsmanager.com/feed/",
        "https://www.scandinaviantraveler.com/en/feed"
    ]

    processed_analysis = []
    
    for url in feeds:
        print(f"🔍 Accessing: {url} ...")
        feed = feedparser.parse(url)
        
        if not feed.entries:
            print(f"⚠️ No entries found for {url}")
            continue

        print(f"📈 Found {len(feed.entries)} news. Processing top 3...")
        for entry in feed.entries[:3]:
            tension = IntuitionEngine.analyze_tension(entry.title)
            
            # Pobieramy opis (summary), jeśli istnieje
            summary = entry.get('summary', 'No description available')
            
            processed_analysis.append({
                "niche_or_area": entry.title,
                "market": "AUTO-SCAN",
                "confidence": 0.85 if tension['level'] == "HIGH" else 0.70,
                "decision": "YES" if tension['level'] == "HIGH" else "WATCH",
                "reason_short": summary[:150] + "...",
                "intuition_signal": tension['signal']
            })

    if not processed_analysis:
        print("❌ CRITICAL: No data collected from any feed!")
        return

    final_report = {
        "last_update": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
        "deep_analysis": processed_analysis
    }

    save_report(final_report)
    print(f"--- 🏁 Report Ready: {len(processed_analysis)} signals gathered ---")

# TO JEST KLUCZOWE - bez tego skrypt się nie odpali!
if __name__ == "__main__":
    generate_report()