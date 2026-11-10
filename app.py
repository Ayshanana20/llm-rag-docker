import streamlit as st
import os
from ingest import process_and_store_pdf

st.title("📚 Local RAG Assistant with Dynamic PDF Upload")

# Sidebar for uploading new documents
st.sidebar.header("Upload Document")
uploaded_file = st.sidebar.file_uploader("Choose a PDF or TXT file", type=["pdf", "txt"])

if uploaded_file is not None:
    file_path = os.path.join(".", uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.sidebar.success(f"Uploaded {uploaded_file.name} successfully!")
    
    if st.sidebar.button("Process & Index Document"):
        with st.spinner("Processing and extracting document text..."):
            extracted_text = process_and_store_pdf(file_path)
            st.sidebar.success("Document processed successfully!")
            st.write("### Extracted Document Preview:")
            st.write(extracted_text[:1000] + "...") # Show preview of text

# Main Chat Interface
user_query = st.text_input("Ask a question about your documents:")
if user_query:
    st.write(f"Searching for answers regarding: *{user_query}*")