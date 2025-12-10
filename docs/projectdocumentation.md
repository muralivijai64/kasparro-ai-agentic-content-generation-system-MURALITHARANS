# Project Documentation  
### Kasparro Applied AI Engineer Challenge  
### Submission by: **MURALITHARAN S**

---

## 1. Overview

This project implements a **Multi-Agent AI Content Generation System** designed for the Applied AI Engineer Challenge by Kasparro Technologies.  
The goal is to autonomously generate:

- Product Page Summary  
- FAQ (Frequently Asked Questions)  
- Comparison Page Output  

The project follows a **clean, scalable, and modular architecture**, enabling easy expansion and robust content generation.

---

## 2. System Architecture

The system uses **five independent agents**, each responsible for a single task. This ensures maintainability and clean separation of logic.

###  **1. Parser Agent**
- Reads product data from `input_product.json`
- Cleans currency symbols and formatting
- Structures raw JSON into a clean internal Python dictionary

###  **2. QA Generator Agent**
- Generates multiple Q&A pairs
- Uses reusable logic blocks from `text_blocks.py`
- Ensures all questions and answers follow a simple, consistent pattern

###  **3. Comparison Agent**
- Compares two products based on:
  - Price  
  - Brand  
  - Key features  
- Generates comparison insights
- Highlights the better option

### **4. Template Engine Agent**
- Applies templates to raw text blocks
- Ensures consistent formatting for final output

### **5. Emitter Agent**
- Saves final content into JSON files:
  - `product_page.json`
  - `faq.json`
  - `comparison_page.json`
- Creates `outputs/` folder if missing

---

## 3. Data Flow Pipeline

    Input JSON
    ↓
    Parser Agent
    ↓
    QA Generator Agent
    ↓
    Comparison Agent
    ↓
    Template Engine Agent
    ↓
    Emitter Agent
    ↓
    Final Output Files


This creates a **linear, modular pipeline** for generating clean, structured JSON outputs.

---

## 4. Project Folder Structure

    ├── docs/
    │ └── projectdocumentation.md
    ├── outputs/
    │ ├── faq.json
    │ ├── product_page.json
    │ └── comparison_page.json
    ├── src/
    │ ├── agents/
    │ ├── logic_blocks/
    │ ├── data/
    │ ├── templates/
    │ └── main.py
    ├── tests/
    ├── requirements.txt
    └── README.md


Each folder has a clear purpose:
- **agents/** → all agent logic  
- **logic_blocks/** → reusable text functions  
- **templates/** → format templates  
- **data/** → input datasets  
- **outputs/** → auto-generated JSON files  
- **docs/** → this documentation  

---

## 5. How to Run the System

### Step 1 — Create virtual environment  
    python -m venv venv
### Step 2 — Activate the environment
Windows:
    venv\Scripts\activate
### Step 3 — Install dependencies
    pip install -r requirements.txt
### Step 4 — Run the main pipeline
    python src/main.py
### Step 5 — Output files will be generated
Check /outputs/ folder for:
    product_page.json,
    faq.json,
    comparison_page.json

## 6. Key Design Choices
 ### Modular Agent Design
    Each task—parsing, generating, templating, saving—is handled by a separate agent.
 ### Clean Code Separation
    Logic is cleanly split into:
        Agents
        Templates
        Logic blocks
        Data
### Easy Extensibility
    To add new content types, simply create a new agent.
### Template-Driven Output
    Ensures consistent and reusable output formatting.

## 7. Output Descriptions
   ### product_page.json
      Contains:
        Product name
        Brand
        Price
        Features
        Summary
   ### faq.json
      List of Q&A pairs, each containing:
        question
        answer
   ### comparison_page.json
      Includes:
        Product A details
        Product B details
        Price comparison
        Feature comparison
        Winner summary

## 8. Testing
    A placeholder tests/ folder is included.
    Future unit tests may cover:
        Parsing accuracy
        FAQ generation logic
        Comparison logic
        Template formatting
        Output structure

### 9. Future Improvements
    Add LLM-based content generation
    Support HTML/Markdown output formats
    Build a CLI tool
    Add input error handling
    Auto-detect missing fields in JSON

### 10. Conclusion
   ### This project demonstrates:
        Problem-solving ability
        Modular architecture design
        Python engineering skills
        Autonomous system development
        Clean and maintainable coding practices
Prepared and submitted by:
**MURALITHARAN S**
For Kasparro Applied AI Engineer Challenge.   