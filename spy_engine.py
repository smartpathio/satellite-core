import json, datetime, os, platform, feedparser, re

class IntelAnalyst:
    @staticmethod
    def analyze_opportunity(title, summary):
        text = (title + " " + summary).lower()
        
        # --- FILTR WYWIADU: ODSIAWANIE ŚMIECI ---
        blacklist = ['lithuania', 'litwa', 'estonia', 'latvia', 'łotwa', 'finland', 'finlandia', 'ukraine', 'ukraina', 'stock market', 'shares rise']
        if any(word in text for word in blacklist):
            return None # Całkowite odrzucenie newsa

        # --- FILTRY MERYTORYCZNE ---
        ecom_trends = ['viral product', 'trending usa', 'tiktok shop', 'best seller', 'winning product', 'dropshipping trend', 'consumer demand']
        kdp_logic = ['brand-centric', 'qr code', 'd2c', 'low content', 'niche research', 'bsr breakout', 'amazon kdp']
        regions = ['poland', 'polska', 'scandinavia', 'norway', 'norwegia', 'denmark', 'dania']

        is_ecom_gold = any(word in text for word in ecom_trends)
        is_kdp_gem = any(word in text for word in kdp_logic)
        is_regional = any(region in text for region in regions)

        # --- GENEROWANIE RAPORTU ANALITYCZNEGO ---
        if is_ecom_gold:
            return {
                "level": "🔥 WYSTRZAŁ",
                "impact": "Wykryto trend viralowy w USA. Wysokie prawdopodobieństwo powtórki w PL/Scan.",
                "action": "Sprawdź dostępność u dostawców i przygotuj testowy landing page pod TikTok Ads."
            }
        if is_kdp_gem:
            return {
                "level": "💎 KDP GEM",
                "impact": "Nisza kompatybilna z Twoim modelem Brand-Centric/QR. Możliwość budowy bazy mailowej.",
                "action": "Zmapuj niszę pod kątem BSR i zaprojektuj unikalny dodatek cyfrowy pod kod QR."
            }
        if is_regional:
            return {
                "level": "⚠️ OPERACYJNE",
                "impact": "Zmiany na Twoim bezpośrednim podwórku biznesowym (PL/Norway).",
                "action": "Skoryguj plany logistyczne lub marketingowe pod te rynki."
            }
            
        return None # Jeśli to nie jest nic z powyższych, wyrzuć to (brak "bzdur")

def clean_data(raw_html):
    if not raw_html: return ""
    cleanr = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
    text = re.sub(cleanr, '', raw_html)
    text = re.sub(r'The post.*?appeared first on.*', '', text, flags=re.IGNORECASE)
    return text.strip()[:300]

def generate_report():
    print("--- 🛰️  SATELLITE-CORE: WYWIAD GOSPODARCZY URUCHOMIONY... ---")
    feeds = [
        "https://ecommercenews.eu/feed/",
        "https://www.logisticsmanager.com/feed/",
        "https://arcticstartup.com/feed/",
        "https://www.retaildive.com/feeds/news/",
        "https://techcrunch.com/feed/" # Dodatkowe źródło dla głębszych trendów
    ]

    processed = []
    for url in feeds:
        feed = feedparser.parse(url)
        for entry in feed.entries[:12]:
            summary = clean_data(entry.get('summary', ''))
            analysis = IntelAnalyst.analyze_opportunity(entry.title, summary)
            
            # Tylko jeśli analiza coś wykryła (brak śmieci)
            if analysis:
                processed.append({
                    "niche_or_area": entry.title.upper(),
                    "market": "USA-PL-INTEL",
                    "decision": analysis['level'],
                    "reason_short": f"KONTEKST: {summary}",
                    "intuition_signal": f"ANALIZA: {analysis['impact']} | REKOMENDACJA: {analysis['action']}",
                    "confidence": 0.99
                })

    # Sortowanie od najważniejszych
    processed.sort(key=lambda x: (x['decision'] == '🔥 WYSTRZAŁ', x['decision'] == '💎 KDP GEM'), reverse=True)

    report = {
        "last_update": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
        "deep_analysis": processed
    }

    # Zapis do folderu 'Pobrane' zgodnie z Twoim życzeniem
    downloads_path = os.path.join(os.path.expanduser("~"), "Downloads", "satellite_report.json")
    
    with open('satellite_report.json', 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=4, ensure_ascii=False)
    
    # Kopia do Pobranych (opcjonalnie, ale chciałeś mieć tam wyniki)
    try:
        with open(downloads_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=4, ensure_ascii=False)
    except:
        pass

    print(f"--- 🏁 RAPORT WYGENEROWANY. Znaleziono {len(processed)} istotnych sygnałów. ---")

if __name__ == "__main__":
    generate_report()