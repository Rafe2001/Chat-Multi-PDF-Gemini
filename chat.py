import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
from interface import user_input
from processing import get_pdf_text, get_text_chunks, get_vector_store


load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def main():
    st.set_page_config("Chat PDF")
    st.header("Chat with PDF using Gemini💁")
    
    user_query = st.chat_input("Ask a question from the PDF files")
    
    if user_query:
        user_input(user_query)
        
        
    with st.sidebar:
        st.title("Menu:")
        pdf_docs = st.file_uploader("Upload your PDF files and click on submit & process button", accept_multiple_files=True)
        if st.button("Submit & Process"):
            with st.spinner("Processing...."):
                raw_text = get_pdf_text(pdf_docs)
                text_chunk = get_text_chunks(raw_text) 
                get_vector_store(text_chunk)
                st.success("Done")
                
                
if __name__ == "__main__":
    main()      
        