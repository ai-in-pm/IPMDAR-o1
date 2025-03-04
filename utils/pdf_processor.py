import PyPDF2
import nltk
import os
import json
from nltk.tokenize import sent_tokenize

# Download NLTK resources if not already downloaded
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

def extract_pdf_text(pdf_path):
    """Extract text from PDF file."""
    text = ""
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += page.extract_text() + "\n"
        return text
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
        return ""

def create_knowledge_base(text):
    """Create a structured knowledge base from the extracted text."""
    # Split text into sentences
    sentences = sent_tokenize(text)
    
    # Create initial knowledge structure
    knowledge_base = {
        "compliance_policy": [],
        "data_analytics": [],
        "project_management": [],
        "risk_forecasting": [],
        "systems_integration": [],
        "implementation": [],
        "general": []
    }
    
    # Keywords for each category to help with classification
    keywords = {
        "compliance_policy": [
            "compliance", "policy", "regulation", "guideline", "requirement", "standard", 
            "acquisition", "federal", "law", "statute", "mandate", "rule", "directive",
            "DFARS", "FAR", "CFR", "DCMA", "regulatory", "approval", "authorize"
        ],
        "data_analytics": [
            "analytics", "metrics", "measurement", "data", "report", "dashboard", 
            "analysis", "trend", "statistic", "calculation", "EVM", "earned value", 
            "performance", "indicator", "SPI", "CPI", "variance"
        ],
        "project_management": [
            "management", "project", "planning", "execution", "CDRL", "deliverable", 
            "milestone", "schedule", "timeline", "work breakdown", "WBS", "tailoring",
            "implementation", "contract", "SOW", "statement of work"
        ],
        "risk_forecasting": [
            "risk", "forecast", "prediction", "mitigation", "probability", "impact",
            "likelihood", "consequence", "uncertainty", "opportunity", "threat",
            "contingency", "reserve", "estimate", "projection", "future"
        ],
        "systems_integration": [
            "integration", "system", "technical", "interface", "interoperability",
            "architecture", "compatibility", "data format", "JSON", "schema", "XML",
            "standard", "protocol", "automation", "tool", "software"
        ],
        "implementation": [
            "implementation", "step", "procedure", "instruction", "guide", "manual",
            "how-to", "process", "workflow", "operation", "conduct", "perform",
            "execute", "action", "activity", "task"
        ]
    }
    
    # Classify sentences into categories based on keywords
    for sentence in sentences:
        sentence_lower = sentence.lower()
        categorized = False
        
        for category, category_keywords in keywords.items():
            for keyword in category_keywords:
                if keyword.lower() in sentence_lower:
                    knowledge_base[category].append(sentence.strip())
                    categorized = True
                    break
            if categorized:
                break
        
        # If not categorized, add to general
        if not categorized:
            knowledge_base["general"].append(sentence.strip())
    
    # Create embedding index for faster retrieval (placeholder for actual embedding implementation)
    # In a production system, you would use embeddings from models like OpenAI's or other embedding services
    knowledge_base["_index"] = "Placeholder for embeddings index"
    
    return knowledge_base
