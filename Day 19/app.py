import streamlit as st

from graph import graph


st.set_page_config(
    page_title="LangGraph AI Assistant",
    page_icon="🤖"
)

st.title("🤖 LangGraph AI Assistant")
st.caption("RAG workflow using LangGraph, LLM and Memory")


# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []


# Display previous messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])


# User input
question = st.chat_input("Ask your question...")


if question:

    # Display user question
    with st.chat_message("user"):
        st.write(question)

    # Initial State
    initial_state = {
        "question": question,
        "context": "",
        "answer": "",
        "messages": st.session_state.messages.copy()
    }

    # Run LangGraph
    with st.spinner("Thinking..."):

        result = graph.invoke(initial_state)

    answer = result["answer"]

    # Display answer
    with st.chat_message("assistant"):
        st.write(answer)

    # Save UI history
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )