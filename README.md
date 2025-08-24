# 🏥 Medical Q&A Chatbot

This project is a **RAG (Retrieval-Augmented Generation) based chatbot** for answering medical questions using **AI and vector search technology**. It combines document retrieval with large language models to provide accurate medical information.

## 🚀 Features

- **RAG-based responses**: Combines retrieval and generation for accurate answers
- **Vector search**: Fast similarity search through medical documents  
- **Streamlit web interface**: Easy-to-use chat interface
- **Docker support**: Easy deployment and scaling
- **Medical document processing**: Handles various medical data formats

## 🧠 Tech Stack

- **Python 3.8+**
- **LangChain** - RAG framework
- **Streamlit** - Web interface
- **Vector Database** - Document embeddings storage
- **OpenAI/HuggingFace APIs** - Language models
- **Docker** - Containerization

## 💻 How to Run

### 🔧 Prerequisites
- Python 3.8+
- Docker 

### 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/pc2404-ml/medical_qna_chatbot
   cd medical_qna_chatbot
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

### 🐳 Docker Setup 

```bash
# Build and run with Docker Compose
docker-compose up --build

# Access the application at http://localhost:8501
```

### ▶️ Run the Application

```bash
# Start the medical chatbot
streamlit run src/app.py

# Open your browser to http://localhost:8501
```

## 📁 Project Structure

```
medical_qna_chatbot/
├── src/                    # Source code
│   ├── app.py             # Main Streamlit application
│   ├── config.py          # Configuration settings
│   ├── data_loader.py     # Data loading utilities
│   ├── rag_chain.py       # RAG implementation
│   └── vectorstore.py     # Vector database operations
├── data/                  # Medical data files
├── requirements.txt       # Python dependencies
├── docker-compose.yml     # Docker configuration
└── Dockerfile            # Docker image definition
```

## ⚙️ Configuration

Edit the configuration in `src/config.py` or use environment variables:

- `OPENAI_API_KEY`: Your OpenAI API key
- `HUGGINGFACE_API_KEY`: Your HuggingFace API key (if using)
- `DATA_PATH`: Path to your medical data files

## 💬 Usage

1. Start the application by running `streamlit run src/app.py`
2. Open your browser to `http://localhost:8501`
3. Ask medical questions in the chat interface
4. Get AI-powered responses based on medical documents

### 💡 Example Questions
- What are the symptoms of diabetes?
- How is high blood pressure treated?
- What causes migraine headaches?
- What are the side effects of aspirin?
- How can I prevent heart disease?

## 🛠️ Development

### Adding New Data
1. Place medical documents in the `data/` folder
2. Run the data loader to process and index the documents
3. Restart the application

### Running Tests
```bash
python -m pytest tests/
```

## ⚠️ Disclaimer

This chatbot is for **educational and informational purposes only**. It should not be used as a substitute for professional medical advice, diagnosis, or treatment. Always consult with qualified healthcare professionals for medical concerns.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Submit a pull request


## 📫 Contact

For queries or suggestions, reach out on [LinkedIn](https://www.linkedin.com/in/poojachoudhary7408/).

---

**Built with ❤️ using Python, LangChain, Streamlit, and OpenAI**