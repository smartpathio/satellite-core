import json, datetime, os, platform, feedparser, re

class IntuitionEngine:
    @staticmethod
    def analyze_tension(title, summary):
        # Kraje skandynawskie i Polska - Twoje priorytety
        target_regions = ['norway', 'denmark', 'sweden', 'finland', 'lithuania', 'poland', 'norwegia', 'dania', 'szwecja', 'finlandia', 'litwa', 'polska']
        # Słowa kluczowe alertów
        alert_words = ['customs', 'rules', 'fee', 'tax', 'strike', 'delay', 'cło', 'podatek', 'strajk', 'opóźnienie']
        
        text_to_scan = (title + " " + summary).lower()
        is_regional = any(region in text_to_scan for region in target_regions)
        is_alert = any(word in text_to_scan for word in alert_words)

        if is_regional:
            return {"level": "TAK", "signal": "PRIORYTET REGIONALNY: Ważne dla rynków Skandynawii/Polski."}
        if is_alert:
            return {"level": "TAK", "signal": "ALERT RYNKOWY: Wykryto zmiany w przepisach lub utrudnienia."}
        
        return {"level": "OBSERWUJ", "signal": "Standardowy ruch na rynku globalnym."}

def clean_html(raw_html):
    if not raw_html: return ""
    # 1. Usuwanie tagów HTML
    cleanr = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
    cleantext = re.sub(cleanr, '', raw_html)
    # 2. Usuwanie śmieci typu "The post ... appeared first on..."
    cleantext = re.sub(r'The post.*?appeared first on.*', '', cleantext, flags=re.IGNORECASE)
    return cleantext.strip()[:180]

def generate_report():
    print("--- 🛰️  TURBO SCANNER (PL) START... ---")
    feeds = [
        "https://ecommercenews.eu/feed/",
        "https://www.logisticsmanager.com/feed/",
        "https://www.shippingandfreightresource.com/feed/",
        "https://arcticstartup.com/feed/"
    ]

    processed_analysis = []
    
    for url in feeds:
        feed = feedparser.parse(url)
        for entry in feed.entries[:6]: # Pobieramy nieco więcej dla lepszej selekcji
            summary = clean_html(entry.get('summary', ''))
            analysis = IntuitionEngine.analyze_tension(entry.title, summary)
            
            processed_analysis.append({
                "niche_or_area": entry.title,
                "market": "SATELLITE-SCAN",
                "confidence": 0.95 if analysis['level'] == "TAK" else 0.75,
                "decision": analysis['level'],
                "reason_short": summary + "...",
                "intuition_signal": analysis['signal']
            })

    # SORTOWANIE: Wszystkie TAK (Polska, Skandynawia, Alerty) na samą górę!
    processed_analysis.sort(key=lambda x: x['decision'] == 'TAK', reverse=True)

    final_report = {
        "last_update": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
        "deep_analysis": processed_analysis
    }

    # Zapis do głównego folderu
    with open('satellite_report.json', 'w', encoding='utf-8') as f:
        json.dump(final_report, f, indent=4, ensure_ascii=False)
    
    # Kopia do Pobranych
    if platform.system() == "Windows":
        path = os.path.join(os.environ['USERPROFILE'], 'Downloads', 'satellite_report.json')
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(final_report, f, indent=4, ensure_ascii=False)

    print(f"--- 🏁 Gotowe! Wygenerowano {len(processed_analysis)} sygnałów. ---")

if __name__ == "__main__":
    generate_report()