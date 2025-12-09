def generate_benefits_block(model):
    blocks = []
    for b in model["benefits"]:
        blocks.append({"title": b, "description": f"{b} effect from {model['name']}"})
    return blocks

def generate_usage_block(model):
    return {
        "instructions": model.get("usage"),
        "frequency": "Daily (morning)",
        "tips": ["Apply before sunscreen"]
    }

def generate_questions(model, n=15):
    questions = []
    categories = ["Informational", "Safety", "Usage", "Purchase", "Comparison", "Ingredients"]
    q_templates = [
        ("Informational", f"What is {model['name']} and who is it for?"),
        ("Usage", f"How do I use {model['name']}?"),
        ("Safety", f"Are there any side effects of {model['name']}?"),
        ("Purchase", f"What is the price of {model['name']}?"),
        ("Ingredients", f"What are the key ingredients in {model['name']}?"),
        ("Comparison", f"How does {model['name']} compare to Product B?")
    ]
    i = 0
    while len(questions) < n:
        cat, q = q_templates[i % len(q_templates)]
        a = ""
        if cat == "Informational":
            a = f"{model['name']} is a serum with {model['concentration']} suitable for {', '.join(model['skin_type'])} skin."
        elif cat == "Usage":
            a = model["usage"]
        elif cat == "Safety":
            a = model["side_effects"]
        elif cat == "Purchase":
            a = f"Price: ₹{model['price_inr']}"
        elif cat == "Ingredients":
            a = ", ".join(model["ingredients"])
        elif cat == "Comparison":
            a = "See comparison page."
        questions.append({"q": q, "a": a, "category": cat})
        i += 1
    return questions
