import os

# File paths
DATA_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "medical_data.csv")
#DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "medical_data.csv")

# Model settings
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
OLLAMA_MODEL = "llama3.2:latest"

# Text processing
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 100

# Prompt template
PROMPT_TEMPLATE = """
You are an expert medical assistant. From the medical text below, extract the following details clearly and present them in simple plain English (no JSON):

- Symptoms
- Treatment
- Impact on Pregnancy
- Mental Health Impact
- Age group affected

Use bullet points or short paragraphs for clarity. Do not include any formatting or code blocks. Dont write text like Here are the extracted details in simple plain English in response:

Text:
{context}
"""