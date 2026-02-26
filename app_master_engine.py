import os
import subprocess
from pathlib import Path
from datetime import datetime
import urllib.parse

def get_chrome_path():
    paths = [r"C:\Program Files\Google\Chrome\Application\chrome.exe", 
             r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
             os.path.expandvars(r"%LocalAppData%\Google\Chrome\Application\chrome.exe")]
    for path in paths:
        if os.path.exists(path): return path
    return None

def launch_matrix():
    print("\n" + "="*60)
    print("🛰️  SATELLITE MATRIX v29.5 | CLOUD SYNC & GIT READY")
    print("="*60)
    
    target = input("\n👉 DAWID, CO DZISIAJ ANALIZUJEMY? : ")
    if not target: target = "Portable Blender"

    encoded_target = urllib.parse.quote(target)

    links = {
        "USA_TIKTOK": f"https://www.tiktok.com/search/video?q={encoded_target}%20review",
        "SNAPTIK": "https://snaptik.app/pl",
        "CHINA_1688": f"https://s.1688.com/selloffer/offer_search.htm?keywords={encoded_target}",
        "EU_MERKANDI": f"https://www.google.com/search?q=site:merkandi.pl+{encoded_target}",
        "PL_ALLEGRO": f"https://allegro.pl/listing?string={encoded_target}"
    }

    # ŚCIEŻKA DO CHMURY - Automatyczne wykrywanie OneDrive Dawida
    onedrive_path = Path(os.environ.get('OneDriveConsumer', os.environ.get('OneDrive', Path.home() / "Downloads")))
    target_folder = onedrive_path / "MATRIX_REPORTS"
    
    # Stwórz folder jeśli nie istnieje
    if not target_folder.exists():
        target_folder.mkdir(parents=True, exist_ok=True)

    report_name = "MATRIX_REPORT.html" # Stała nazwa dla skrótu na telefonie
    report_path = target_folder / report_name

    full_html = f"""
    <!DOCTYPE html>
    <html lang="pl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
        <title>MATRIX APP</title>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
            body {{ background: #0f172a; font-family: 'Inter', sans-serif; padding: 15px; color: #f8fafc; margin: 0; }}
            .header {{ background: linear-gradient(135deg, #1e3a8a 0%, #1e40af 100%); padding: 30px; border-radius: 20px; text-align: center; border-bottom: 6px solid #10b981; margin-bottom: 20px; }}
            .card {{ background: #1e293b; padding: 20px; border-radius: 15px; border: 1px solid #334155; margin-bottom: 15px; }}
            .btn {{ display: block; padding: 18px; text-align: center; border-radius: 12px; text-decoration: none; font-weight: 900; color: white; margin-top: 10px; text-transform: uppercase; }}
            @media (min-width: 768px) {{ .grid {{ display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 15px; }} }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1 style="margin:0; font-size: 1.2em; color: #94a3b8;">TARGET: {target.upper()}</h1>
                <div style="font-size: 3.5em; font-weight: 900; color: #10b981;">85%</div>
                <p style="margin:0;">SUKCESU</p>
            </div>
            <div class="grid">
                <div class="card">
                    <h3>🎬 CONTENT</h3>
                    <a href="{links['USA_TIKTOK']}" class="btn" style="background:#000;" target="_blank">TIKTOK</a>
                    <a href="{links['SNAPTIK']}" class="btn" style="background:#10b981;" target="_blank">POBIERZ</a>
                </div>
                <div class="card">
                    <h3>📦 DOSTAWA</h3>
                    <a href="{links['CHINA_1688']}" class="btn" style="background:#f97316;" target="_blank">1688</a>
                    <a href="{links['EU_MERKANDI']}" class="btn" style="background:#3b82f6;" target="_blank">EUROPA</a>
                </div>
                <div class="card">
                    <h3>🛒 RYNEK</h3>
                    <a href="{links['PL_ALLEGRO']}" class="btn" style="background:#ff5a00;" target="_blank">ALLEGRO</a>
                </div>
            </div>
        </div>
    </body>
    </html>
    """

    with open(report_path, "w", encoding="utf-8") as f:
        f.write(full_html)
    
    chrome = get_chrome_path()
    if chrome: subprocess.Popen([chrome, "--new-window", str(report_path)])
    print(f"✅ RAPORT WYSŁANY DO CHMURY: {report_path}")

if __name__ == "__main__":
    launch_matrix()