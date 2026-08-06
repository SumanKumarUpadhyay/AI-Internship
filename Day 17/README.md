# 📚 RAG API using FastAPI, LangChain & Groq

A simple **Retrieval-Augmented Generation (RAG) API** built using **FastAPI**, **LangChain**, **Groq LLM**, **HuggingFace Embeddings**, and **FAISS**. The application allows users to upload a PDF document, ask questions, and receive AI-generated answers based on the uploaded document.

---

# 🚀 Project Overview

This project demonstrates the complete **RAG (Retrieval-Augmented Generation)** workflow.

The API performs the following steps:

- Upload PDF document
- Process document
- Split document into chunks
- Generate embeddings
- Store vectors in FAISS
- Retrieve relevant information
- Generate answers using Groq LLM
- Return JSON responses through FastAPI

---

# 🛠️ Technology Stack

- Python
- FastAPI
- LangChain
- Groq API
- Llama 3.3 70B Versatile
- HuggingFace Embeddings
- FAISS
- PyPDF
- Uvicorn

---

# 📂 Project Structure

```text
Day 17/
│
├── .env
├── requirements.txt
│
├── data/
│
├── llm.py
├── prompt_template.py
├── embeddings.py
├── document_loader.py
├── text_splitter.py
├── vector_store.py
├── retriever.py
├── pipeline.py
├── main.py
├── app.py
│
├── README.md
├── API_Testing_Report.md
└── screenshots/
```

---

# 🎯 Features

- Upload PDF using FastAPI
- Automatic document processing
- Text chunking
- HuggingFace Embeddings
- FAISS Vector Database
- Semantic Search
- Retrieval-Augmented Generation (RAG)
- Groq LLM Integration
- JSON API Responses
- Streamlit User Interface

---

# 📄 File Description

### `llm.py`

Loads the Groq Large Language Model.

---

### `prompt_template.py`

Creates reusable prompt templates using context and user questions.

---

### `embeddings.py`

Loads the HuggingFace embedding model.

---

### `document_loader.py`

Loads uploaded PDF documents using PyPDFLoader.

---

### `text_splitter.py`

Splits documents into smaller chunks.

---

### `vector_store.py`

Creates a FAISS vector database from document chunks.

---

### `retriever.py`

Creates a retriever for semantic search.

---

### `pipeline.py`

Connects all LangChain components and handles the complete RAG workflow.

---

### `main.py`

FastAPI backend providing PDF upload and question-answering endpoints.

---

### `app.py`

Simple Streamlit frontend for interacting with the RAG API.

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/SumanKumarUpadhyay/AI-Internship.git
```

Move into the project folder

```bash
cd AI-Internship
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Configure Environment Variable

Create a `.env` file.

```env
GROQ_API_KEY=your_groq_api_key
```

---

# ▶️ Run FastAPI

```bash
uvicorn main:app --reload
```

Open Swagger UI

```
http://127.0.0.1:8000/docs
```

---

# ▶️ Run Streamlit

```bash
streamlit run app.py
```

---

# 🔄 RAG Workflow

```text
Upload PDF
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
Generate Answer
```

---

# 📌 API Endpoints

## Upload PDF

**POST**

```
/upload
```

Uploads and processes a PDF document.

---

## Ask Question

**POST**

```
/chat
```

Example Request

```json
{
  "question": "What is the leave policy?"
}
```

Example Response

```json
{
  "answer": "Employees receive 20 paid leaves annually."
}
```

---

# 📖 Concepts Covered

- FastAPI
- File Upload
- PDF Processing
- LangChain
- Prompt Templates
- HuggingFace Embeddings
- FAISS
- Semantic Search
- Retriever
- Retrieval-Augmented Generation (RAG)
- Groq LLM
- API Development

---

# 🎯 Learning Outcomes

Through this project, I learned how to:

- Build REST APIs using FastAPI.
- Upload and process PDF documents.
- Implement document chunking.
- Generate embeddings using HuggingFace.
- Store vectors using FAISS.
- Retrieve relevant document context.
- Build a complete RAG pipeline.
- Integrate Groq LLM for question answering.
- Connect backend APIs with a Streamlit frontend.

---

# 🚀 Future Improvements

- Support multiple PDF uploads.
- Display source page numbers.
- Add chat history.
- Store FAISS index permanently.
- Support DOCX and TXT files.
- Add user authentication.
- Improve UI with streaming responses.
- Deploy on Render or Hugging Face Spaces.

---

# 👨‍💻 Author

**Suman Kumar**

B.Tech CSE (Artificial Intelligence)

AI/ML | Machine Learning | Deep Learning | Generative AI | LangChain | FastAPI | RAG
