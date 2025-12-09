class ParserAgent:
    def run(self, raw):
        # Clean price (handles ₹, â‚¹, etc.)
        price_str = str(raw.get("Price"))
        price_clean = (
            price_str.replace("₹", "")
                     .replace("â‚¹", "")
                     .replace("Rs.", "")
                     .replace("rs.", "")
                     .replace("INR", "")
                     .strip()
        )

        model = {
            "id": "glowboost_vitc_10",
            "name": raw.get("Product Name"),
            "concentration": raw.get("Concentration"),
            "skin_type": [s.strip() for s in raw.get("Skin Type", "").split(",")],
            "ingredients": [i.strip() for i in raw.get("Key Ingredients", "").split(",")],
            "benefits": [b.strip() for b in raw.get("Benefits", "").split(",")],
            "usage": raw.get("How to Use"),
            "side_effects": raw.get("Side Effects"),
            "price_inr": int(price_clean)
        }
        return model
