import os
import warnings

# Suppress warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # Suppress TensorFlow warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)  # Suppress LangChain warnings

import streamlit as st
from data_loader import load_medical_data
from vectorstore import create_vectorstore
from rag_chain import create_rag_chain

def show_examples():
    st.markdown("### 💡 Example Questions")
    st.markdown("""
    - What are the symptoms of diabetes?
    - How is high blood pressure treated?
    - What causes migraine headaches?
    - What are the side effects of aspirin?
    - How can I prevent heart disease?
    """)

st.title("🌿 Medical Data ChatBot")

# Initialize everything once and store in session state
if "rag_chain" not in st.session_state:
    with st.spinner("🔄 Initializing Medical ChatBot..."):
        documents = load_medical_data()
        vectorstore = create_vectorstore(documents)
        st.session_state.rag_chain = create_rag_chain(vectorstore)
        st.success("✅ ChatBot ready!")

query = st.text_input("Enter a disease name to extract info:")

# Show examples after input bar
show_examples()

if query:
    with st.spinner("Processing..."):
        # Use cached RAG chain from session state
        response = st.session_state.rag_chain.run(query)

        # Display results
        st.markdown("### Information")
        st.write(response)

st.markdown("---")