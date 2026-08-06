# API Testing Report

## Project Name

**Basic RAG API using FastAPI and LangChain**

---

# Objective

The objective of API testing was to verify that the RAG API correctly handles PDF uploads, processes documents, retrieves relevant information, and generates accurate responses using the Groq LLM.

---

# Testing Environment

- Framework: FastAPI
- API Testing Tool: Swagger UI
- LLM: Groq (Llama 3.3 70B Versatile)
- Vector Database: FAISS
- Embedding Model: all-MiniLM-L6-v2
- Operating System: Windows 11

---

# API Endpoints Tested

## 1. Upload PDF

**Method**

```
POST
```

**Endpoint**

```
/upload
```

**Purpose**

Uploads a PDF document, processes it, creates embeddings, and stores vectors in the FAISS database.

---

## 2. Chat API

**Method**

```
POST
```

**Endpoint**

```
/chat
```

**Purpose**

Accepts a user question, retrieves relevant document chunks, and generates an AI response.

---

# Test Cases

| Test No. | Test Scenario | Expected Result | Status |
|----------|---------------|-----------------|--------|
| 1 | Upload a valid PDF | PDF uploaded successfully | ✅ Pass |
| 2 | Ask a valid question | Correct answer generated | ✅ Pass |
| 3 | Ask multiple questions | Answers generated successfully | ✅ Pass |
| 4 | Ask an unrelated question | AI indicates information is unavailable in the uploaded document | ✅ Pass |
| 5 | Ask a question before uploading a PDF | Displays "Please upload a PDF first." | ✅ Pass |
| 6 | Upload an empty PDF | System handles the file without crashing | ✅ Pass |
| 7 | Upload a large PDF | PDF processed successfully with increased processing time | ✅ Pass |
| 8 | Upload an unsupported file format | Upload rejected | ✅ Pass |
| 9 | Submit an empty question | Validation error or appropriate response returned | ✅ Pass |
| 10 | Upload another PDF and ask questions | New document processed successfully | ✅ Pass |

---

# Sample API Response

## Upload API

```json
{
    "message": "PDF uploaded successfully."
}
```

---

## Chat API

### Request

```json
{
    "question": "What is the leave policy?"
}
```

### Response

```json
{
    "answer": "Employees receive 20 paid leaves annually."
}
```

---

# Robustness Testing Summary

The application was tested using different document types, empty inputs, unsupported formats, and multiple user queries. The API remained stable and generated responses correctly for valid inputs. Invalid or unsupported inputs were handled appropriately without causing application failure.

---

# Observations

- PDF upload worked successfully.
- Document chunking completed correctly.
- Embeddings were generated successfully.
- FAISS stored document vectors correctly.
- Semantic retrieval returned relevant document chunks.
- Groq LLM generated context-aware responses.
- FastAPI endpoints responded correctly in JSON format.

---

# Improvement Suggestions

- Support multiple PDF uploads.
- Display source page numbers with responses.
- Save FAISS index for future reuse.
- Add user authentication.
- Support DOCX and TXT documents.
- Improve handling of empty PDF files.
- Enable streaming responses.
- Add chat history support.

---

# Conclusion

The Basic RAG API was successfully tested using FastAPI and Swagger UI. All major functionalities, including PDF upload, document processing, semantic retrieval, and AI response generation, worked correctly. The API demonstrated reliable performance for both valid and invalid test cases and provides a strong foundation for building scalable document-based AI applications.