class ComparisonAgent:
    def run(self, model):
        product_b = {
            "id": "radiant_bright_b",
            "name": "RadiantBright C Serum",
            "concentration": "8% Vitamin C",
            "ingredients": ["Vitamin C", "Glycerin"],
            "benefits": ["Brightening", "Hydration"],
            "price_inr": 799
        }

        shared = list(set(model["ingredients"]) & set(product_b["ingredients"]))
        unique_left = list(set(model["ingredients"]) - set(product_b["ingredients"]))
        unique_right = list(set(product_b["ingredients"]) - set(model["ingredients"]))

        return {
            "left_product": model,
            "right_product": product_b,
            "comparison": {
                "price_delta": product_b["price_inr"] - model["price_inr"],
                "shared_ingredients": shared,
                "unique_to_left": unique_left,
                "unique_to_right": unique_right,
                "benefit_overlap": list(set(model["benefits"]) & set(product_b["benefits"]))
            }
        }
