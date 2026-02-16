import os
import datetime
import pandas as pd
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="SATELLITE CORE - INTEGRATED")

# --- 1. SILNIK ANALITYCZNY (Tutaj zbieramy dane ze wszystkich ikon/raportów) ---

def get_integrated_data():
    # Tutaj bot docelowo będzie robił research przez parę godzin
    data = {
        "norway": [
            {"firma": "Silverhand", "rotacja": "6/2", "atut": "Mieszkanie/Diety", "link": "https://www.poloniusz.pl/"},
            {"firma": "Workshop AS", "rotacja": "3/3", "atut": "Loty opłacone", "link": "https://www.poloniusz.pl/"}
        ],
        "kdp_ecom": {
            "kdp": "Trend: Wellness Planner (High ROI)",
            "ecom": "Winner: Moss Smock (TikTok Trend USA)"
        },
        "logistyka": "Trasy PL-NO: Optymalizacja kosztów paliwa na promach (Świnoujście-Ystad)."
    }
    return data

def save_report_to_downloads(data):
    """Zapisuje raport jako plik TXT w folderze Pobrane"""
    try:
        downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
        filename = f"Raport_SATELLITE_{datetime.date.today()}.txt"
        full_path = os.path.join(downloads_path, filename)
        
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(f"RAPORT SATELLITE CORE - {datetime.date.today()}\n")
            f.write("="*30 + "\n")
            f.write(f"NORWEGIA: {len(data['norway'])} ofert\n")
            f.write(f"KDP/ECOM: {data['kdp_ecom']['kdp']}\n")
            f.write(f"LOGISTYKA: {data['logistyka']}\n")
        print(f"✅ Zapisano raport w: {full_path}")
    except Exception as e:
        print(f"❌ Błąd zapisu: {e}")

# --- 2. INTERFEJS UŻYTKOWNIKA (Nowoczesny Dashboard) ---

@app.get("/", response_class=HTMLResponse)
async def dashboard():
    now = datetime.datetime.now().strftime("%H:%M")
    d = get_integrated_data()
    
    html_content = f"""
    <!DOCTYPE html>
    <html lang="pl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>SATELLITE CORE</title>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap" rel="stylesheet">
        <style>
            :root {{ --neon: #00f2ff; --bg: #050505; --card: #121212; }}
            body {{ background: var(--bg); color: white; font-family: 'Inter', sans-serif; margin: 0; padding: 15px; }}
            .header {{ display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #333; padding-bottom: 10px; margin-bottom: 20px; }}
            .card {{ background: var(--card); border-radius: 12px; padding: 16px; margin-bottom: 15px; border-left: 4px solid var(--neon); }}
            .btn {{ display: block; width: 100%; padding: 12px; background: #222; border: 1px solid #444; color: white; text-align: center; text-decoration: none; border-radius: 8px; margin-top: 10px; font-size: 0.9em; }}
            .badge {{ background: #004d00; color: #00ff00; padding: 2px 8px; border-radius: 10px; font-size: 0.8em; }}
        </style>
    </head>
    <body>
        <div class="header">
            <div>🛰️ <b>SATELLITE</b> CORE</div>
            <div style="color:var(--neon)">{now}</div>
        </div>

        <div class="card">
            <h3>🇳🇴 NORWEGIA (ROTACJE)</h3>
            {"".join([f"<p><b>{j['firma']}</b> <span class='badge'>{j['rotacja']}</span><br><small>{j['atut']}</small><a href='{j['link']}' class='btn'>OTWÓRZ POLONIUSZA</a></p>" for j in d['norway']])}
        </div>

        <div class="card">
            <h3>📊 ANALITYKA (KDP & E-COM)</h3>
            <p>📚 {d['kdp_ecom']['kdp']}</p>
            <p>🇺🇸 {d['kdp_ecom']['ecom']}</p>
        </div>

        <div class="card" style="border-left-color: #ff00ff;">
            <h3>🚛 LOGISTYKA & TRASY</h3>
            <p><small>{d['logistyka']}</small></p>
            <a href="#" class="btn">KALKULATOR TRASY</a>
        </div>
        
        <p style="text-align:center; font-size:0.7em; color:#555;">SYSTEM GOTOWY | RAPORT ZAPISANY W POBRANE</p>
    </body>
    </html>
    """
    return html_content

@app.on_event("startup")
async def startup_event():
    # Przy każdym starcie bot automatycznie generuje i zapisuje raport
    data = get_integrated_data()
    save_report_to_downloads(data)