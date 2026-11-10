def search_documents(query: str, text_corpus: str):
    """Searches the extracted text for the query terms and returns a snippet."""
    if not text_corpus:
        return "No document loaded yet. Please upload and process a PDF."
    
    # Basic keyword search implementation
    query_lower = query.lower()
    if query_lower in text_corpus.lower():
        # Find position and return surrounding context
        idx = text_corpus.lower().find(query_lower)
        start = max(0, idx - 100)
        end = min(len(text_corpus), idx + 400)
        return f"Found match in document:\n\n...{text_corpus[start:end]}..."
    
    return "No direct match found for your query in the current document."