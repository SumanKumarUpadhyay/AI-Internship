# 🤖 AI Research Assistant Agent

A simple **AI Research Assistant Agent** built using **LangChain**, **Groq LLM**, **Wikipedia**, and **Streamlit**. The agent accepts a user's research question, plans the task, uses a search tool to gather information, and generates a clear AI-powered response.

---

# 🚀 Project Overview

This project demonstrates the basic concepts of an **AI Agent**.

Unlike a normal chatbot, the agent:

- Understands the user's query
- Plans how to solve it
- Selects an appropriate tool
- Collects information
- Generates a final answer using an LLM

This project was developed as part of **Day 18** of the **Linkific AI & ML Internship**.

---

# 🛠️ Technology Stack

- Python
- LangChain
- Groq API
- Llama 3.3 70B Versatile
- Wikipedia API
- Streamlit
- Python Dotenv

---

# 📂 Project Structure

```text
Day 18/
│
├── .env
├── requirements.txt
│
├── llm.py
├── prompts.py
├── tools.py
├── planner.py
├── agent.py
├── app.py
│
├── README.md
├── AI_Agent_Design_Document.md
├── Report.md
└── screenshots/
```

---

# 🎯 Features

- AI Research Assistant
- AI Agent Planning
- Tool Selection
- Wikipedia Search Tool
- Prompt Engineering
- Groq LLM Integration
- Chat-Based Interface
- Streamlit Frontend
- Modular Project Structure

---

# 📄 File Description

## llm.py

Loads the Groq Large Language Model.

---

## prompts.py

Creates the prompt template used by the AI Agent.

---

## tools.py

Implements the Wikipedia search tool to retrieve research information.

---

## planner.py

Decides which tool should be used to answer the user's question.

---

## agent.py

Connects the planner, search tool, prompt template, and LLM to execute the complete AI Agent workflow.

---

## app.py

Provides a simple Streamlit interface for interacting with the AI Research Assistant.

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/SumanKumarUpadhyay/AI-Internship.git
```

Move to the project folder

```bash
cd AI-Internship/Day\ 18
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variable

Create a `.env` file.

```env
GROQ_API_KEY=your_groq_api_key
```

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

---

# 🤖 AI Agent Workflow

```text
User Question
      │
      ▼
Planner
      │
      ▼
Select Tool
      │
      ▼
Wikipedia Search
      │
      ▼
Retrieve Information
      │
      ▼
Prompt Template
      │
      ▼
Groq LLM
      │
      ▼
Final AI Response
```

---

# 🧠 AI Agent Architecture

```text
                +----------------+
                |      User      |
                +-------+--------+
                        |
                        ▼
                +----------------+
                |    AI Agent    |
                +-------+--------+
                        |
                +-------+-------+
                |    Planner    |
                +-------+-------+
                        |
                        ▼
              Wikipedia Search Tool
                        |
                        ▼
                 Retrieved Information
                        |
                        ▼
                   Prompt Template
                        |
                        ▼
                    Groq LLM
                        |
                        ▼
                  Final Response
```

---

# 📌 Example

### User Question

```
What is Machine Learning?
```

### AI Response

```
Machine Learning is a branch of Artificial Intelligence that enables computers to learn from data and make predictions without being explicitly programmed.
```

---

# 📚 Concepts Covered

- AI Agents
- Planning
- Tool Usage
- Agent Workflow
- ReAct (Basic Concept)
- Prompt Engineering
- LLM Integration
- Streamlit UI

---

# 🎯 Learning Outcomes

Through this project, I learned how to:

- Understand AI Agent architecture.
- Build a simple AI Agent.
- Design an agent planning workflow.
- Integrate external tools with an LLM.
- Use LangChain Prompt Templates.
- Connect Groq LLM with Python.
- Develop an interactive AI application using Streamlit.
- Build modular AI applications with separate components.

---

# 🚀 Future Improvements

- Add multiple tools (Calculator, Weather, PDF Search).
- Integrate LangChain Agents.
- Add Conversation Memory.
- Support document-based research.
- Use LangGraph for advanced workflows.
- Implement Multi-Agent Systems.
- Add web search support.
- Deploy the application on Streamlit Cloud.

---

# 👨‍💻 Author

**Suman Kumar**

**B.Tech CSE (Artificial Intelligence)**

**AI/ML | Data Science | Generative AI | LangChain | FastAPI | RAG | AI Agents**

---

⭐ **This project was developed as part of the Linkific AI & ML Internship (Day 18).**
