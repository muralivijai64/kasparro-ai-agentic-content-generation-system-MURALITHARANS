from logic_blocks.text_blocks import generate_questions

class QAGeneratorAgent:
    def run(self, model):
        return {
            "product_id": model["id"],
            "product_name": model["name"],
            "faq": generate_questions(model, n=15)
        }
