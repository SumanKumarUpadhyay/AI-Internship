# 📚 Basic RAG Chatbot using LangChain

A simple **Retrieval-Augmented Generation (RAG)** chatbot built using **LangChain**, **Groq LLM**, **HuggingFace Embeddings**, **FAISS**, and **Streamlit**. The chatbot retrieves relevant information from company documents and generates accurate AI-powered responses.

---

## 📌 Project Overview

This project demonstrates the complete **RAG (Retrieval-Augmented Generation)** pipeline.

The chatbot:

- Loads company documents
- Splits documents into chunks
- Converts text into embeddings
- Stores embeddings in FAISS
- Retrieves relevant document chunks
- Sends retrieved context to Groq LLM
- Generates accurate answers
- Displays responses through a Streamlit interface

---

## 🚀 Technology Stack

- Python
- LangChain
- Groq API
- Llama 3.3 70B Versatile
- HuggingFace Embeddings
- FAISS
- Streamlit
- Python-dotenv

---

## 📁 Project Structure

```
Day 16/
│
├── data/
│   └── company_info.txt
│
├── .env
├── requirements.txt
├── document_loader.py
├── text_splitter.py
├── embeddings.py
├── vector_store.py
├── retriever.py
├── prompt_template.py
├── llm.py
├── pipeline.py
├── app.py
├── README.md
└── screenshots/
```

---

## 📚 Learning Objectives

- Understand Retrieval-Augmented Generation (RAG)
- Load documents using LangChain
- Split documents into chunks
- Generate text embeddings
- Store vectors in FAISS
- Perform semantic search
- Retrieve relevant document context
- Connect retrieved context with Groq LLM
- Build a simple RAG chatbot

---

## ✨ Features

- Document Question Answering
- Semantic Search
- FAISS Vector Database
- HuggingFace Embeddings
- Groq LLM Integration
- Prompt Template
- Modular Project Structure
- Streamlit User Interface

---

## 📄 File Description

### `document_loader.py`

Loads the company document using LangChain TextLoader.

### `text_splitter.py`

Splits the document into smaller chunks.

### `embeddings.py`

Creates embeddings using HuggingFace Embedding Model.

### `vector_store.py`

Stores document embeddings in a FAISS vector database.

### `retriever.py`

Retrieves the most relevant document chunk.

### `prompt_template.py`

Creates the RAG prompt using retrieved context and user question.

### `llm.py`

Connects LangChain with Groq LLM.

### `pipeline.py`

Connects Retriever, Prompt Template and LLM into a single workflow.

### `app.py`

Provides a simple Streamlit interface for interacting with the chatbot.

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/SumanKumarUpadhyay/AI-Internship.git
```

Go to the project folder

```bash
cd AI-Internship
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Configure Environment Variable

Create a `.env` file

```env
GROQ_API_KEY=your_groq_api_key
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 🔄 RAG Workflow

```
Company Document
        │
        ▼
Document Loader
        │
        ▼
Text Splitter
        │
        ▼
Embeddings
        │
        ▼
FAISS Vector Store
        │
        ▼
Retriever
        │
        ▼
Prompt Template
        │
        ▼
Groq LLM
        │
        ▼
Generated Answer
```

---

## 💬 Sample Question

**Question**

```
What is the office timing?
```

**Answer**

```
The office timing is 9 AM to 6 PM.
```

---

## 📖 Concepts Covered

- Retrieval-Augmented Generation (RAG)
- LangChain
- Document Loader
- Text Splitting
- Embeddings
- HuggingFace Embeddings
- FAISS
- Vector Database
- Semantic Search
- Retriever
- Prompt Engineering
- Groq LLM
- Streamlit

---

## 🎯 Learning Outcomes

Through this project, I learned how to:

- Build a complete RAG pipeline
- Process documents using LangChain
- Generate embeddings from text
- Store embeddings in FAISS
- Retrieve relevant information using semantic search
- Combine retrieved context with an LLM
- Build a modular AI application
- Create a simple web interface using Streamlit

---

## 🚀 Future Improvements

- Support PDF documents
- Chat history
- Multiple document uploads
- Advanced RAG pipeline
- Hybrid Search
- ChromaDB Integration
- Source citation in responses
- ChatGPT-style UI

---

## 👨‍💻 Author

**Suman Kumar**

B.Tech CSE (Artificial Intelligence)

AI/ML | Machine Learning | Deep Learning | Generative AI | LangChain | RAG
