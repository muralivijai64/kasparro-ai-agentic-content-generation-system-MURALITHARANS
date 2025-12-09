from logic_blocks.text_blocks import generate_benefits_block, generate_usage_block

class TemplateEngineAgent:
    def run(self, model):
        return {
            "id": model["id"],
            "title": model["name"],
            "subtitle": model["concentration"],
            "price": {
                "amount": model["price_inr"],
                "currency": "INR",
                "display": f"₹{model['price_inr']}"
            },
            "skin_type": model["skin_type"],
            "ingredients": model["ingredients"],
            "benefits": generate_benefits_block(model),
            "how_to_use": generate_usage_block(model),
            "safety": {
                "side_effects": model["side_effects"]
            }
        }
