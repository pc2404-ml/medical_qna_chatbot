import streamlit as st
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_ollama import OllamaLLM  # Updated import
from config import OLLAMA_MODEL, PROMPT_TEMPLATE

@st.cache_resource
def load_llama():
    """Initialize Ollama model"""
    return OllamaLLM(model=OLLAMA_MODEL)

@st.cache_resource
def create_rag_chain(_vectorstore):
    """Create RAG chain with vectorstore"""
    prompt = PromptTemplate(
        input_variables=["context"],
        template=PROMPT_TEMPLATE
    )
    retriever = _vectorstore.as_retriever()
    llama = load_llama()
    return RetrievalQA.from_chain_type(
        llm=llama,
        retriever=retriever,
        chain_type_kwargs={"prompt": prompt}
    )