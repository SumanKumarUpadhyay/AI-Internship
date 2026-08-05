import streamlit as st

from pipeline import run_rag

st.set_page_config(page_title="Basic RAG Chatbot")

st.title("📚 Basic RAG Chatbot")

question = st.text_input("Ask your Question")

if st.button("Get Answer"):

    if question:

        answer = run_rag(question)

        st.subheader("Answer")

        st.write(answer)

    else:

        st.warning("Please enter a question.")