import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="📚 RAG AI Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 RAG AI Assistant")
st.caption("Upload a PDF • Ask Questions • Get AI Answers")

# Upload PDF
st.sidebar.header("📂 Upload PDF")

uploaded_file = st.sidebar.file_uploader(
    "Choose a PDF",
    type=["pdf"]
)

if uploaded_file:

    files = {
        "file": (
            uploaded_file.name,
            uploaded_file.getvalue(),
            "application/pdf"
        )
    }

    response = requests.post(
        f"{API_URL}/upload",
        files=files
    )

    if response.status_code == 200:
        st.sidebar.success("✅ PDF Uploaded Successfully")
    else:
        st.sidebar.error("❌ Upload Failed")

# Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Chat
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat Input
question = st.chat_input("Ask anything about the uploaded PDF...")

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.write(question)

    response = requests.post(
        f"{API_URL}/chat",
        json={
            "question": question
        }
    )

    if response.status_code == 200:

        answer = response.json()["answer"]

    else:

        answer = "❌ Unable to generate response."

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    with st.chat_message("assistant"):
        st.write(answer)