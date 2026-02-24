# compliance_logic.py
# This module handles the IPN Protocol (VAT Margin & Fees)

class IPNCompliance:
    def __init__(self):
        self.p24_commission = 0.019  # Prowizja 1.9%
        self.max_product_value = 500.0 # Limit bezpieczenstwa

    def calculate_net_profit(self, buy_price_ali, sell_price_pl):
        """
        Calculates profit before marketing based on your input.
        Example: 40 PLN (Ali) -> 129 PLN (PL)
        """
        if sell_price_pl > self.max_product_value:
            return 0.0
        
        # Obliczenie marży brutto
        raw_margin = sell_price_pl - buy_price_ali
        
        # Odjęcie prowizji płatności (Przelewy24)
        payment_fee = sell_price_pl * self.p24_commission
        
        # Zysk netto (przed dochodowym)
        net_profit = raw_margin - payment_fee
        
        return round(net_profit, 2)

# TEST MODUŁU (Uruchomi się tylko gdy odpalisz ten konkretny plik)
if __name__ == "__main__":
    calc = IPNCompliance()
    result = calc.calculate_net_profit(40, 129)
    print(f"--- TEST ZYSKU ---")
    print(f"Produkt: Portable Blender")
    print(f"Zysk na reke: {result} PLN")