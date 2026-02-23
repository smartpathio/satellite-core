import json, datetime, os, platform, feedparser, re

class MarketHunter:
    @staticmethod
    def analyze_opportunity(title, summary):
        text = (title + " " + summary).lower()
        
        # 1. Filtry Arbitrażu (USA -> PL)
        ecom_trends = ['viral product', 'trending usa', 'tiktok shop', 'best seller', 'winning product', 'dropshipping trend']
        # 2. Filtry KDP (na podstawie Twoich raportów)
        kdp_logic = ['brand-centric', 'qr code', 'd2c', 'low content', 'niche research', 'bsr breakout']
        # 3. Twoje Regiony
        regions = ['poland', 'polska', 'scandinavia', 'norway', 'denmark']

        is_ecom_gold = any(word in text for word in ecom_trends)
        is_kdp_gem = any(word in text for word in kdp_logic)
        is_regional = any(region in text for region in regions)

        if is_ecom_gold:
            return {"level": "🔥 WYSTRZAŁ", "signal": "ARBITRAŻ ECOM: Trend z USA z potencjałem na rynek PL!"}
        if is_kdp_gem:
            return {"level": "💎 KDP GEM", "signal": "STRATEGIA KDP: Model Brand-Centric/QR wykryty w raportach."}
        if is_regional:
            return {"level": "TAK", "signal": "PRIORYTET REGIONALNY: Kluczowe dla Skandynawii/Polski."}
            
        return {"level": "OBSERWUJ", "signal": "Standardowy ruch rynkowy."}

def clean_data(raw_html):
    if not raw_html: return ""
    cleanr = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
    text = re.sub(cleanr, '', raw_html)
    text = re.sub(r'The post.*?appeared first on.*', '', text, flags=re.IGNORECASE)
    return text.strip()[:200]

def generate_report():
    print("--- 🛰️  SATELLITE-CORE: USA-PL ARBITRAGE START... ---")
    feeds = [
        "https://ecommercenews.eu/feed/",
        "https://www.logisticsmanager.com/feed/",
        "https://arcticstartup.com/feed/",
        "https://www.retaildive.com/feeds/news/" # Dodane źródło z USA dla trendów retail
    ]

    processed = []
    for url in feeds:
        feed = feedparser.parse(url)
        for entry in feed.entries[:8]:
            summary = clean_data(entry.get('summary', ''))
            opp = MarketHunter.analyze_opportunity(entry.title, summary)
            
            processed.append({
                "niche_or_area": entry.title,
                "market": "USA-PL-SCANNER",
                "decision": opp['level'],
                "reason_short": summary + "...",
                "intuition_signal": opp['signal'],
                "confidence": 0.98 if opp['level'] != "OBSERWUJ" else 0.70
            })

    # Sortowanie: Najpierw Gorące Trendy Ecom i KDP, potem Regiony
    processed.sort(key=lambda x: (x['decision'] == '🔥 WYSTRZAŁ', x['decision'] == '💎 KDP GEM', x['decision'] == 'TAK'), reverse=True)

    report = {
        "last_update": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
        "deep_analysis": processed
    }

    with open('satellite_report.json', 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=4, ensure_ascii=False)

    print(f"--- 🏁 Gotowe! Przeanalizowano {len(processed)} sygnałów pod kątem USA -> PL. ---")

if __name__ == "__main__":
    generate_report()