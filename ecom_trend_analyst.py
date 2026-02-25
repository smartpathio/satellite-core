class EcomTrendAnalyst:
    def __init__(self):
        self.stop_scroll_benchmark = 3.5

    def analyze_viral_potential(self, product_name, current_ssr, platform="TikTok"):
        is_viral = current_ssr > self.stop_scroll_benchmark
        status = "HOT 🔥" if is_viral else "STABLE 📈"
        advice = []
        
        if is_viral:
            advice.append(f"High Stop-Scroll ({current_ssr}%). Market is engaging.")
            advice.append("ACTION: Aggressive scaling (20% budget increase daily).")
        else:
            advice.append("Average saturation. Focus on retargeting.")

        return {
            "product": product_name,
            "verdict": status,
            "platform": platform,
            "advice": advice,
            "ssr": current_ssr
        }

# TA FUNKCJA JEST KLUCZEM - Silnik będzie jej szukał
def get_analysis():
    analyst = EcomTrendAnalyst()
    # Przykładowa analiza (docelowo tu mogą być dane z pętli/bazy)
    data = analyst.analyze_viral_potential("Portable Blender", 4.2)
    
    advice_html = "".join([f"<li>{a}</li>" for a in data['advice']])
    
    html = f"""
    <div style="border: 1px solid #333; padding: 15px; border-radius: 8px;">
        <h3 style="color: #eab308;">Produkt: {data['product']}</h3>
        <p>Status: <strong>{data['verdict']}</strong> | Platforma: {data['platform']}</p>
        <p>Stop-Scroll Rate: <span style="color: #10b981;">{data['ssr']}%</span></p>
        <ul style="color: #cbd5e1;">
            {advice_html}
        </ul>
    </div>
    """
    return html