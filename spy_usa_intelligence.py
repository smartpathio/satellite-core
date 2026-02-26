# spy_usa_intelligence.py

def get_analysis(product_name):
    return f"""
    <div class="report-page">
        <h2>⚡ USA LIVE PULSE: Rankingi Dzisiejsze</h2>
        <div class="merytoryka-box">
            <div class="highlight-info" style="border-left-color: #00ff00; background: #000; color: #00ff00; font-family: 'Courier New';">
                >>> SYSTEM STATUS: PRZECHWYTYWANIE TRENDU... SUCCESS.
            </div>
            
            <h3>1. Ranking Reklam (Today's Top Ads USA)</h3>
            <p>Kliknij poniżej, aby wejść w przefiltrowany ranking reklam, które DZISIAJ generują największy obrót w USA:</p>
            <div style="display: flex; gap: 10px; margin-top: 20px;">
                <a href="https://ads.tiktok.com/business/creativecenter/inspiration/topads?region=US&period=7" class="video-link" style="background: #ff0050;">🚀 TIKTOK TOP ADS (7d USA)</a>
                <a href="https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&q={product_name}" class="video-link" style="background: #0668E1;">🔥 FACEBOOK ADS USA</a>
            </div>

            <h3>2. Amazon Movers (Amazon.com)</h3>
            <p>To jest Twój towar do importu. Sprawdź, jak Amerykanie go pakują i opisują:</p>
            <a href="https://www.amazon.com/gp/movers-and-shakers/" class="video-link" style="background: #ff9900; color: black;">📦 AMAZON BEST SELLERS LIVE</a>
        </div>
    </div>
    """