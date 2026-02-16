import os
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv
from fpdf import FPDF
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import time
import threading
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

# 1. KONFIGURACJA I SERWER
load_dotenv()
app = FastAPI(title="Scandi-Satellite Core")
LOG_FILE = "bot_memory.txt"

# 2. FUNKCJE POMOCNICZE
def check_if_task_completed():
    if not os.path.exists(LOG_FILE):
        return False
    with open(LOG_FILE, "r") as f:
        last_date = f.read().strip()
    return last_date == datetime.now().strftime('%Y-%m-%d')

def log_success():
    with open(LOG_FILE, "w") as f:
        f.write(datetime.now().strftime('%Y-%m-%d'))

def create_pdf_report(data_frame, output_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="Scandi-Satellite Strategic Report 2026", ln=True, align='C')
    pdf.set_font("Arial", size=12)
    pdf.ln(10)
    for index, row in data_frame.iterrows():
        content = f"Country: {row['Country']} | Feedback: {row['Positive_Feedback']} | Trend: {row['Trend_Forecast_2035']}"
        pdf.multi_cell(0, 10, txt=content)
        pdf.ln(2)
    pdf.output(output_path)

def send_email_with_attachment(file_path):
    sender_email = os.getenv('MY_EMAIL')
    receiver_email = os.getenv('MY_EMAIL')
    password = os.getenv('EMAIL_PASSWORD')
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = f"Scandi-Satellite: Strategic Report - {datetime.now().strftime('%Y-%m-%d')}"
    with open(file_path, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", f"attachment; filename= {os.path.basename(file_path)}")
        msg.attach(part)
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)
        server.send_message(msg)

def run_daily_mission():
    print(f"[{datetime.now()}] Mission Starting...")
    market_data = {
        'Country': ['Norway', 'Sweden', 'Denmark'],
        'Positive_Feedback': ['High Salaries', 'Nature Access', 'Work-Life Balance'],
        'Trend_Forecast_2035': ['Bullish', 'Stable', 'Strong Growth']
    }
    df = pd.DataFrame(market_data)
    timestamp = datetime.now().strftime('%Y%m%d')
    # Folder Pobrane użytkownika daw76
    download_dir = os.path.join(os.path.expanduser("~"), "Downloads")
    excel_path = os.path.join(download_dir, f"Scandi_Data_{timestamp}.xlsx")
    pdf_path = os.path.join(download_dir, f"Strategic_Report_{timestamp}.pdf")
    
    df.to_excel(excel_path, index=False)
    create_pdf_report(df, pdf_path)
    
    try:
        send_email_with_attachment(pdf_path)
        print(f"✅ Mission Success: Report sent.")
        log_success()
    except Exception as e:
        print(f"❌ Error: {e}")

# 3. PĘTLA BOTA (WĄTEK W TLE)
def background_scheduler():
    print("--- SCANDI-SATELLITE BOT: MONITORING ACTIVE ---")
    while True:
        now = datetime.now()
        # Sprawdzanie czy jest godzina 8:00 rano
        if now.hour == 8 and not check_if_task_completed():
            run_daily_mission()
        time.sleep(60) # Sprawdzaj co minutę

# Odpalenie bota w tle przy starcie serwera
threading.Thread(target=background_scheduler, daemon=True).start()

# 4. DASHBOARD NA SMARTFONA
@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <html>
        <head>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <style>
                body { font-family: 'Segoe UI', sans-serif; background: #0f172a; color: #f8fafc; text-align: center; padding-top: 50px; }
                .status-card { background: #1e293b; border-radius: 20px; padding: 30px; display: inline-block; border: 2px solid #38bdf8; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.5); }
                h1 { color: #38bdf8; margin-bottom: 5px; }
                .pulse { height: 15px; width: 15px; background-color: #22c55e; border-radius: 50%; display: inline-block; box-shadow: 0 0 0 0 rgba(34, 197, 94, 1); animation: pulse 2s infinite; }
                @keyframes pulse { 0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(34, 197, 94, 0.7); } 70% { transform: scale(1); box-shadow: 0 0 0 10px rgba(34, 197, 94, 0); } 100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(34, 197, 94, 0); } }
            </style>
        </head>
        <body>
            <div class="status-card">
                <h1>🛰️ SATELLITE CORE</h1>
                <p><span class="pulse"></span> SYSTEM STATUS: ACTIVE</p>
                <p>Morning Report: <b>08:00 AM</b></p>
                <p>Target: <b>Downloads Folder</b></p>
            </div>
        </body>
    </html>
    """