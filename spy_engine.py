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
    html_template = f"""
    <!DOCTYPE html>
    <html lang="pl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
        <title>SATELLITE INTEL</title>
        
        <link rel="icon" type="image/png" href="icon.png">
        <link rel="apple-touch-icon" href="icon.png">
        <meta name="mobile-web-app-capable" content="yes">
        <meta name="apple-mobile-web-app-capable" content="yes">
        <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
        <meta name="apple-mobile-web-app-title" content="Satellite">

        <style>
            body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background: #0f172a; color: white; padding: 15px; margin: 0; }}
            .card {{ background: #1e293b; border-radius: 12px; padding: 16px; margin-bottom: 16px; border-left: 6px solid #3b82f6; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.2); }}
            .🔥 {{ border-left-color: #ef4444; }}
            .💎 {{ border-left-color: #10b981; }}
            .header {{ text-align: center; padding: 25px 0; border-bottom: 2px solid #334155; margin-bottom: 25px; }}
            .label {{ font-weight: 800; font-size: 0.7em; color: #94a3b8; text-transform: uppercase; letter-spacing: 1.5px; }}
            .action {{ background: #0ea5e9; color: white; padding: 12px; border-radius: 8px; margin-top: 15px; font-size: 0.85em; font-weight: bold; border: 1px solid #38bdf8; }}
            h2 {{ font-size: 1.2em; color: #f8fafc; margin: 10px 0; line-height: 1.3; font-weight: 700; }}
            p {{ margin: 6px 0; line-height: 1.5; color: #e2e8f0; }}
            .footer {{ text-align: center; font-size: 0.7em; color: #475569; margin-top: 30px; padding-bottom: 20px; }}
        </style>
    </head>
    <body>
        <div class="header">
            <h1 style="margin:0; font-size: 1.8em; letter-spacing: -1px;">🛰️ SATELLITE INTEL</h1>
            <p style="color: #94a3b8; font-size: 0.9em; margin-top: 5px;">Raport Operacyjny: {data['last_update']}</p>
        </div>
    """
    for item in data['deep_analysis']:
        icon_class = "🔥" if "USA" in item['decision'] else ("💎" if "KDP" in item['decision'] else "⚠️")
        html_template += f"""
        <div class="card {icon_class}">
            <div class="label">{item['decision']} | {item['market']}</div>
            <h2>{item['niche_or_area']}</h2>
            <p style="font-size: 0.85em; color: #94a3b8; font-style: italic; border-bottom: 1px solid #334155; padding-bottom: 8px; margin-bottom: 10px;">{item['reason_short']}...</p>
            <p><strong>🎯 ANALIZA:</strong> {item['intuition_signal'].split('|')[0]}</p>
            <div class="action">💡 REKOMENDACJA: {item['intuition_signal'].split('|')[1]}</div>
        </div>
        """
    if not data['deep_analysis']:
        html_template += "<p style='text-align:center; color: #64748b;'>Brak sygnałów wysokiego priorytetu w tej sesji.</p>"
    
    html_template += """
        <div class="footer">SYSTEM SATELLITE-CORE v2.1 | USA-UK-PL-NOR</div>
    </body></html>
    """
    return html_template

def generate_report():
    print("--- 🛰️ SATELLITE-CORE: URUCHAMIANIE WYWIADU AGRESYWNEGO... ---")
    feeds = [
        "https://www.retaildive.com/feeds/news/",
        "https://techcrunch.com/feed/",
        "https://ecommercenews.eu/feed/",
        "https://arcticstartup.com/feed/",
        "https://www.theverge.com/rss/index.xml"
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
                    "market": "INTEL-OPERATIONS",
                    "decision": analysis['level'],
                    "reason_short": summary,
                    "intuition_signal": f"{analysis['impact']} | {analysis['action']}"
                })

    processed.sort(key=lambda x: ("USA" in x['decision'], "KDP" in x['decision']), reverse=True)
    
    report_data = {
        "last_update": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
        "deep_analysis": processed
    }

    with open('satellite_report.json', 'w', encoding='utf-8') as f:
        json.dump(report_data, f, indent=4, ensure_ascii=False)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(generate_html_report(report_data))

    print(f"--- 🏁 GOTOWE. Raport HTML z ikoną wygenerowany poprawnie. ---")

if __name__ == "__main__":
    generate_report()