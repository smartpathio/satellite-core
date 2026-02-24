class SafetySentinel:
    def __init__(self):
        self.blacklisted_agencies = ["GlobalWork_Fake", "EuroJob_Scam"]
        self.mandatory_registries = ["RAZ (Denmark)", "StartBANK (Norway)", "KRAZ (Poland)"]

    def verify_agency(self, agency_name, has_bilingual_contract, asks_for_passport_original):
        score = 100
        warnings = []

        if asks_for_passport_original:
            score -= 100
            warnings.append("ALARM: Agency requires original passport! Labor camp risk.")
        
        if not has_bilingual_contract:
            score -= 30
            warnings.append("RISK: No bilingual contract provided.")

        if agency_name in self.blacklisted_agencies:
            score = 0
            warnings.append("BLACKLIST: Agency found in fraudulent databases.")

        status = "SAFE" if score > 70 else "DANGEROUS"
        
        return {
            "status": status,
            "score": score,
            "warnings": warnings,
            "registries": self.mandatory_registries
        }