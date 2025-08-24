import streamlit as st
#from langchain.embeddings import HuggingFaceEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings

from langchain.vectorstores import FAISS
from config import EMBEDDING_MODEL

@st.cache_resource
def create_vectorstore(_documents):
    """Create FAISS vectorstore from documents"""
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
    return FAISS.from_documents(_documents, embeddings)