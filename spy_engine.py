import json, datetime, os, platform, feedparser, re

class IntuitionEngine:
    @staticmethod
    def analyze_tension(text):
        # Rozszerzona lista słów alarmowych
        alert_words = ['strike', 'crisis', 'increase', 'problem', 'failure', 'surge', 'delay', 'customs', 'rules', 'new laws']
        text_lower = text.lower()
        if any(word in text_lower for word in alert_words):
            return {"level": "HIGH", "signal": "Disruption Alert: Significant market shift detected."}
        return {"level": "LOW", "signal": "Stable flow: Standard market movement."}

def clean_html(raw_html):
    # Czyścimy opisy ze śmieci HTML, żeby kafelki były estetyczne
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext[:180] # Limit znaków dla estetyki

def generate_report():
    print("--- 🛰️  TURBO SCAN INITIALIZED... ---")
    
    # Rozszerzona lista solidnych źródeł
    feeds = [
        "https://ecommercenews.eu/feed/",
        "https://www.logisticsmanager.com/feed/",
        "https://www.shippingandfreightresource.com/feed/", # Mocny portal logistyczny
        "https://arcticstartup.com/feed/" # Najlepsze źródło o skandynawskich startupach
    ]

    processed_analysis = []
    
    for url in feeds:
        print(f"🔍 Deep Scanning: {url}")
        feed = feedparser.parse(url)
        
        # Bierzemy po 5 newsów dla "gęstszego" dashboardu
        for entry in feed.entries[:5]:
            tension = IntuitionEngine.analyze_tension(entry.title)
            summary = clean_html(entry.get('summary', 'No details.'))
            
            processed_analysis.append({
                "niche_or_area": entry.title,
                "market": "SATELLITE-SCAN",
                "confidence": 0.88 if tension['level'] == "HIGH" else 0.75,
                "decision": "YES" if tension['level'] == "HIGH" else "WATCH",
                "reason_short": summary + "...",
                "intuition_signal": tension['signal']
            })

    final_report = {
        "last_update": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
        "deep_analysis": processed_analysis
    }

    # Zapis
    with open('satellite_report.json', 'w', encoding='utf-8') as f:
        json.dump(final_report, f, indent=4, ensure_ascii=False)
    
    # Backup Windows
    if platform.system() == "Windows":
        path = os.path.join(os.environ['USERPROFILE'], 'Downloads', 'satellite_report.json')
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(final_report, f, indent=4, ensure_ascii=False)

    print(f"--- 🏁 Turbo Report Ready: {len(processed_analysis)} intelligence signals! ---")

if __name__ == "__main__":
    generate_report()