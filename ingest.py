import os
from pypdf import PdfReader

def process_and_store_pdf(file_path: str):
    """Reads a PDF file, extracts text, and returns the extracted content."""
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted + "\n"
    
    print(f"Successfully extracted {len(text)} characters from {file_path}")
    return text