import streamlit as st

from prompt import support_prompt
from llm import llm

st.set_page_config(
    page_title="AI Support Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Support Assistant")

# Session State
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Previous Messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat Input
user_query = st.chat_input("Type your question...")

if user_query:

    # Show User Message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_query
        }
    )

    with st.chat_message("user"):
        st.markdown(user_query)

    # Create Prompt
    prompt = support_prompt.format(
        user_query=user_query
    )

    # Generate Response
    with st.spinner("Thinking..."):

        response = llm.invoke(prompt)

        answer = response.content

    # Store Assistant Message
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    # Show Assistant Message
    with st.chat_message("assistant"):
        st.markdown(answer)