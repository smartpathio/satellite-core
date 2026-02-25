class IPNCompliance:
    def __init__(self):
        self.p24_commission = 0.019
        self.max_product_value = 500.0

    def calculate_net_profit(self, buy_price_ali, sell_price_pl):
        if sell_price_pl > self.max_product_value: return 0.0
        raw_margin = sell_price_pl - buy_price_ali
        payment_fee = sell_price_pl * self.p24_commission
        return round(raw_margin - payment_fee, 2)

def get_analysis():
    calc = IPNCompliance()
    # Przykładowa kalkulacja dla Blendera z Twojego testu
    profit = calc.calculate_net_profit(40, 129)
    return f"""
    <div style="padding: 15px; border: 1px solid #333; border-radius: 10px; border-left: 5px solid #a855f7;">
        <h3 style="color: #a855f7; margin-top:0;">Protokół IPN: VAT Margin & Fees</h3>
        <p>Produkt Testowy: <strong>Portable Blender</strong></p>
        <p>Estymowany Zysk Netto: <strong style="color: #10b981;">{profit} PLN</strong></p>
        <p style="font-size: 0.8em; color: #888;">Uwzględniono prowizję P24 (1.9%). Limit bezpieczeństwa: {calc.max_product_value} PLN.</p>
    </div>
    """