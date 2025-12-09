import json
from agents.parser_agent import ParserAgent
from agents.qa_generator_agent import QAGeneratorAgent
from agents.template_engine_agent import TemplateEngineAgent
from agents.comparison_agent import ComparisonAgent
from agents.emitter_agent import EmitterAgent

def run_pipeline():
    with open("src/data/input_product.json") as f:
        raw = json.load(f)

    parser = ParserAgent()
    model = parser.run(raw)

    qa_agent = QAGeneratorAgent()
    faq_page = qa_agent.run(model)

    template_agent = TemplateEngineAgent()
    product_page = template_agent.run(model)

    comp_agent = ComparisonAgent()
    comparison_page = comp_agent.run(model)

    emitter = EmitterAgent()
    emitter.run({
        "faq": faq_page,
        "product_page": product_page,
        "comparison": comparison_page
    })

if __name__ == "__main__":
    run_pipeline()
