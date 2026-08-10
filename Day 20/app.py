import os
import pandas as pd
import streamlit as st

from agent import run_agent


st.set_page_config(
    page_title="AI Data Analyzer",
    page_icon="📊"
)

st.title("📊 AI Data Analyzer")
st.caption("Upload a CSV and ask questions about your data.")


# Upload CSV
uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)


if uploaded_file:

    # Create data folder
    os.makedirs("data", exist_ok=True)

    # Save uploaded file
    file_path = os.path.join(
        "data",
        uploaded_file.name
    )

    with open(file_path, "wb") as file:
        file.write(uploaded_file.getbuffer())

    st.success("CSV uploaded successfully.")


    # Read CSV
    df = pd.read_csv(file_path)


    # Display first 5 rows
    st.subheader("📋 First 5 Rows")

    st.dataframe(
        df.head(),
        use_container_width=True
    )


    # Ask question
    question = st.chat_input(
        "Ask something about your CSV..."
    )


    if question:

        # Display user question
        with st.chat_message("user"):
            st.write(question)


        # Run AI Agent
        with st.spinner("Analyzing..."):

            answer = run_agent(
                question,
                file_path
            )


        # Display answer
        with st.chat_message("assistant"):
            st.write(answer)