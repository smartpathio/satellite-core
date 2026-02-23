import json, datetime, os, feedparser, re

class IntelAnalyst:
    @staticmethod
    def analyze_opportunity(title, summary):
        text = (title + " " + summary).lower()
        
        # --- FILTR WYWIADU: ODSIAWANIE NUDY I ŚMIECI ---
        blacklist = ['lithuania', 'litwa', 'estonia', 'latvia', 'łotwa', 'finland', 'finlandia', 'ukraine', 'ukraina', 'stock market']
        if any(word in text for word in blacklist):
            return None

        # --- FILTRY MINEA-STYLE (USA / UK VIRALS) ---
        ecom_usa = ['winning product', 'viral', 'tiktok shop', 'best seller', 'usa', 'united kingdom', 'uk', 'ads', 'dropshipping', 'consumer trend']
        kdp_logic = ['brand-centric', 'qr code', 'kdp', 'niche', 'bsr', 'amazon kdp', 'low content']
        local_market = ['poland', 'polska', 'norway', 'norwegia', 'scandinavia']

        is_usa_viral = any(word in text for word in ecom_usa)
        is_kdp_gem = any(word in text for word in kdp_logic)
        is_local = any(word in text for word in local_market)

        # --- LOGIKA ANALITYCZNA (AGRESYWNA) ---
        if is_usa_viral:
            return {
                "level": "🔥 USA VIRAL",
                "impact": "DETEKCJA TRENDU W USA/UK. Potencjał na szybki arbitraż lub kopię na rynek PL.",
                "action": "ANALIZA MINEA: Sprawdź kreatywy na TikTok Ads Library. Szukaj dostawcy (agent/Alibaba)."
            }
        if is_kdp_gem:
            return {
                "level": "💎 KDP STRATEGY",
                "impact": "WYKRYTO NISZĘ POD MODEL BRAND-CENTRIC. Możliwość wdrożenia Twoich kodów QR.",
                "action": "Zbadaj BSR w tej niszy na Amazon US/UK. Przygotuj unikalny content cyfrowy."
            }
        if is_local:
            return {
                "level": "⚠️ LOCAL OPS",
                "impact": "Istotne zmiany logistyczne lub rynkowe w Polsce/Skandynawii.",
                "action": "Dostosuj łańcuch dostaw lub komunikację marketingową pod region."
            }
            
        return None

def generate_html_report(data):
    # Generowanie ładnego widoku na telefon
    html_template = f"""
    <!DOCTYPE html>
    <html lang="pl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>SATELLITE INTEL</title>
        <style>
            body {{ font-family: sans-serif; background: #0f172a; color: white; padding: 15px; }}
            .card {{ background: #1e293b; border-radius: 10px; padding: 15px; margin-bottom: 15px; border-left: 5px solid #3b82f6; }}
            .🔥 {{ border-left-color: #ef4444; }}
            .💎 {{ border-left-color: #10b981; }}
            .header {{ text-align: center; border-bottom: 2px solid #334155; padding-bottom: 10px; margin-bottom: 20px; }}
            .label {{ font-weight: bold; font-size: 0.8em; color: #94a3b8; }}
            .action {{ background: #0ea5e9; color: white; padding: 8px; border-radius: 5px; margin-top: 10px; font-size: 0.9em; }}
            h2 {{ font-size: 1.1em; color: #f8fafc; margin: 0 0 10px 0; }}
        </style>
    </head>
    <body>
        <div class="header">
            <h1>🛰️ SATELLITE INTEL</h1>
            <p>Aktualizacja: {data['last_update']}</p>
        </div>
    """
    for item in data['deep_analysis']:
        icon = "🔥" if "USA" in item['decision'] else ("💎" if "KDP" in item['decision'] else "⚠️")
        html_template += f"""
        <div class="card {icon}">
            <div class="label">{item['decision']} | {item['market']}</div>
            <h2>{item['niche_or_area']}</h2>
            <p style="font-size: 0.9em; color: #cbd5e1;">{item['reason_short']}</p>
            <p><strong>WNIOSEK:</strong> {item['intuition_signal'].split('|')[0]}</p>
            <div class="action">🚀 {item['intuition_signal'].split('|')[1]}</div>
        </div>
        """
    html_template += "</body></html>"
    return html_template

def generate_report():
    print("--- 🛰️  SATELLITE-CORE: WYWIAD AGRESYWNY USA/UK... ---")
    feeds = [
        "https://www.retaildive.com/feeds/news/",
        "https://techcrunch.com/feed/",
        "https://ecommercenews.eu/feed/",
        "https://arcticstartup.com/feed/"
    ]

    processed = []
    for url in feeds:
        feed = feedparser.parse(url)
        for entry in feed.entries[:15]:
            summary = re.sub('<.*?>', '', entry.get('summary', ''))[:250]
            analysis = IntelAnalyst.analyze_opportunity(entry.title, summary)
            
            if analysis:
                processed.append({
                    "niche_or_area": entry.title.upper(),
                    "market": "INTEL-REPORT",
                    "decision": analysis['level'],
                    "reason_short": summary,
                    "intuition_signal": f"{analysis['impact']} | {analysis['action']}"
                })

    processed.sort(key=lambda x: ("USA" in x['decision'], "KDP" in x['decision']), reverse=True)
    
    report_data = {{
        "last_update": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
        "deep_analysis": processed
    }}

    # Zapis JSON (dla systemu)
    with open('satellite_report.json', 'w', encoding='utf-8') as f:
        json.dump(report_data, f, indent=4, ensure_ascii=False)

    # Zapis HTML (Twój Dashboard na telefon)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(generate_html_report(report_data))

    print(f"--- 🏁 GOTOWE. Raport HTML wygenerowany. ---")

if __name__ == "__main__":
    generate_report()