# Day 20 — Tool Creation & Function Calling

## Linkific AI & ML Internship

Day 20 focuses on understanding how AI applications can use external tools and functions to perform specific tasks.

The practical implementation for today is an **AI Data Analyzer** that allows a user to upload a CSV file and ask questions about the dataset. The system uses an LLM to decide when CSV analysis is required and then executes the CSV Analyzer tool.

---

## 🎯 Learning Objectives

- Tool Creation
- Function Calling
- Tool Selection
- Tool Chaining
- Error Handling
- Understanding how LLMs interact with external functions

---

## 🛠️ Technologies Used

- Python
- LangChain
- Groq LLM
- Pandas
- Streamlit
- python-dotenv

---

# 📌 Today's Practical

## AI Data Analyzer

The application allows users to:

1. Upload a CSV file.
2. View the first five rows in a table.
3. Ask questions about the dataset.
4. Use the CSV Analyzer Tool to analyze the uploaded data.
5. Send the analysis result back to the LLM.
6. Receive a clear natural-language answer.

---

# 🔄 Application Workflow

```text
User
 ↓
Upload CSV
 ↓
Display First 5 Rows
 ↓
User Question
 ↓
LLM
 ↓
Tool Selection
 ↓
CSV Analyzer Tool
 ↓
Pandas Analysis
 ↓
Tool Result
 ↓
LLM
 ↓
Final Answer
