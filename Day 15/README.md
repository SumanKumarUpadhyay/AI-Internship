# 🤖 AI Support Assistant using LangChain

A simple AI Support Assistant built using **LangChain**, **Groq LLM**, and **Streamlit**. This project demonstrates Prompt Templates, LLM integration, Conversation Memory, and Output Parsing.

---

## 📌 Project Overview

This project was developed as part of **Day 15 Internship Tasks** to understand the fundamentals of LangChain and build a simple AI-powered chatbot.

The assistant can:

- Accept user questions
- Process prompts using Prompt Templates
- Generate responses using Groq LLM
- Maintain basic conversation history
- Display responses through a Streamlit chatbot interface

---

## 🛠️ Tech Stack

- Python
- LangChain
- Groq API
- Llama 3.3 70B Versatile
- Streamlit
- python-dotenv

---

## 📁 Project Structure

```
Day 15/
│
├── .env
├── requirements.txt
├── prompt_template.py
├── llm.py
├── memory.py
├── output_parser.py
├── app.py
├── streamlit_app.py
├── workflow.md
├── langchain_notes.md
├── README.md
└── screenshots/
```

---

## 📚 Learning Objectives

- Understand LangChain Architecture
- Create Prompt Templates
- Connect LangChain with Groq LLM
- Learn Conversation Memory
- Structure responses using Output Parser
- Build a simple AI Support Assistant
- Create a chatbot using Streamlit

---

## ✨ Features

- AI-powered chatbot
- Prompt Template support
- Groq LLM integration
- Basic conversation memory
- Structured AI responses
- Streamlit web interface

---

## 📄 File Description

### `.env`

Stores the Groq API Key securely.

### `requirements.txt`

Contains all required Python libraries.

### `prompt_template.py`

Defines reusable Prompt Templates.

### `llm.py`

Connects LangChain with Groq LLM.

### `memory.py`

Stores conversation history using Python list.

### `output_parser.py`

Formats AI responses.

### `app.py`

Main terminal application.

### `streamlit_app.py`

Interactive chatbot interface using Streamlit.

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

## 🔑 Configure API Key

Create a `.env` file

```env
GROQ_API_KEY=your_groq_api_key
```

---

## ▶️ Run Terminal Application

```bash
python app.py
```

---

## ▶️ Run Streamlit Application

```bash
streamlit run streamlit_app.py
```

---

## 🔄 Project Workflow

```
User Question
      │
      ▼
Prompt Template
      │
      ▼
Groq LLM
      │
      ▼
Generate AI Response
      │
      ▼
Conversation Memory
      │
      ▼
Output Parser
      │
      ▼
Display Response
```

---

## 📸 Sample Output

**User**

```
What is Machine Learning?
```

**Assistant**

```
Machine Learning is a subset of Artificial Intelligence that enables systems to learn patterns from data and make predictions without being explicitly programmed.
```

---

## 📖 Concepts Covered

- LangChain Fundamentals
- Prompt Engineering
- Prompt Templates
- Groq LLM
- Environment Variables
- Conversation Memory
- Output Parsing
- Streamlit Chatbot
- Modular Python Programming

---

## 🎯 Learning Outcome

Through this project, I learned how to:

- Build AI applications using LangChain
- Create reusable Prompt Templates
- Connect Groq LLM with Python
- Secure API keys using `.env`
- Maintain conversation history
- Structure AI responses
- Develop a chatbot using Streamlit
- Organize projects using a modular architecture

---

## 🚀 Future Improvements

- ChatGPT-like UI
- Sidebar with New Chat option
- Real LangChain Memory
- JSON Output Parser
- Streaming Responses
- Chat History Export
- Multi-session Support

---

## 👨‍💻 Author

**Suman Kumar**

B.Tech CSE (Artificial Intelligence)

AI/ML | Deep Learning | Generative AI | LangChain
