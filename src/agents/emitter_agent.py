import json
import os

class EmitterAgent:
    def run(self, pages):
        os.makedirs("outputs", exist_ok=True)

        with open("outputs/faq.json", "w") as f:
            json.dump(pages["faq"], f, indent=2)

        with open("outputs/product_page.json", "w") as f:
            json.dump(pages["product_page"], f, indent=2)

        with open("outputs/comparison_page.json", "w") as f:
            json.dump(pages["comparison"], f, indent=2)

        print("Files generated in /outputs folder.")
