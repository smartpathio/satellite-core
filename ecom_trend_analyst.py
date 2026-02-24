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
            "verdict": status,
            "platform": platform,
            "advice": advice
        }