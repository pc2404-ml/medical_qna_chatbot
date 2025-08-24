import streamlit as st
from langchain_community.document_loaders import CSVLoader
from langchain.text_splitter import CharacterTextSplitter
from config import DATA_PATH, CHUNK_SIZE, CHUNK_OVERLAP

@st.cache_data
def load_medical_data():
    """Load and split medical data from CSV"""
    loader = CSVLoader(file_path=DATA_PATH)
    docs = loader.load()
    splitter = CharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
    return splitter.split_documents(docs)