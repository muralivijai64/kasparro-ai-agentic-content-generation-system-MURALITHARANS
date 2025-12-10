# Kasparro Multi-Agent Content Generation System  
### Applied AI Engineer Challenge  
### Submission by: **Muralitharan S**

This repository contains my solution for the **Kasparro Applied AI Engineer Challenge**, where I built a **multi-agent autonomous content generation system**.  
The system processes product information and generates:

- Product Page Summary  
- Frequently Asked Questions (FAQ)  
- Product Comparison Summary  

It is designed with clean modular architecture following the single-responsibility principle.

---

## 🚀 Features

- **Multi-Agent Architecture**
- **Reusable Logic Blocks**
- **Template-Based Output Generation**
- **Well-Structured JSON Outputs**
- **Clean, Extensible Codebase**

---

## Project Structure

    ├── docs/
    │ └── projectdocumentation.md
    ├── outputs/
    │ ├── faq.json
    │ ├── product_page.json
    │ └── comparison_page.json
    ├── src/
    │ ├── agents/
    │ │ ├── parser_agent.py
    │ │ ├── qa_generator_agent.py
    │ │ ├── comparison_agent.py
    │ │ ├── template_engine_agent.py
    │ │ └── emitter_agent.py
    │ ├── logic_blocks/
    │ │ └── text_blocks.py
    │ ├── data/
    │ │ └── input_product.json
    │ ├── templates/
    │ └── main.py
    ├── tests/
    ├── requirements.txt
    └── README.md


---

## How to Run the Project

### 1. Create Virtual Environment

    python -m venv venv

### 2. Activate the Virtual Environment

    Windows:
        venv\Scripts\activate

### 3. Install Dependencies
    pip install -r requirements.txt

### 4. Run the Main Pipeline
    python src/main.py

### 5. Generated Output Files
    Outputs will be automatically created in the /outputs folder:

        product_page.json

        faq.json

        comparison_page.json

## Agents Overview
            Agent	                              Responsibility
            
        Parser Agent	            Reads input JSON and extracts structured product data

        QA Generator Agent	        Generates FAQ-style question–answer pairs

        Comparison Agent	        Compares two products using pricing & features

        Template Engine Agent	    Applies templates for structured final output

        Emitter Agent	            Saves output content as JSON files

## Key Design Principles

Single Responsibility Principle: Each agent handles exactly one task.

Clean Separation of Logic: Parsing, generation, templating, and output writing are isolated.

Easily Extensible: New agents or output formats can be added without modifying existing ones.

Consistent JSON Structure: Ensures downstream usability.

## Submission Information

This project is submitted as part of the Kasparro Applied AI Engineer Challenge.

Developer:
MURALITHARAN S

For detailed documentation, refer to:
docs/projectdocumentation.md
