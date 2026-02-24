# decision_matrix.py

class DecisionMatrix:
    def __init__(self):
        self.min_profit_threshold = 60.0  # Minimum PLN profit to consider
        self.high_competition_limit = 10  # Max number of competitors in PL
        self.fomo_growth_trigger = 1.5    # 150% growth needed for "WAIT" to "SELL"

    def evaluate_product(self, product_name, margin, growth_rate, competition_count):
        """
        Logic to decide: SELL, WAIT, or REJECT
        """
        # RULE 1: High Competition or Low Profit
        if competition_count > self.high_competition_limit or margin < self.min_profit_threshold:
            return "🔴 REJECT (Low margin or high competition)"

        # RULE 2: High Growth (Viral Potential)
        if growth_rate >= 1.8: # +180% as you mentioned
            if margin >= 80:
                return "🟢 SELL NOW (High margin + Viral trend)"
            else:
                return "🟡 WAIT (Wait for better margin/price)"

        # RULE 3: Waiting for the peak
        if 1.0 < growth_rate < 1.8:
            return "🟡 WAIT (Trend is growing, but not at peak yet)"

        return "⚪ HOLD (No clear signal)"

# TEST: Portable Blender
# margin=89, growth=1.8, competition=3
matrix = DecisionMatrix()
result = matrix.evaluate_product("Portable Blender", 89, 1.8, 3)
print(f"Decision for Blender: {result}")