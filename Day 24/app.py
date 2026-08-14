import streamlit as st

from workflow import app as workflow_app


st.set_page_config(
    page_title="Multi-Agent Research Assistant",
    page_icon="🤖"
)

st.title("🤖 Multi-Agent Research Assistant")

st.write(
    "Coordinator → Research Agent → Writer"
)

question = st.text_area(
    "Enter your question:",
    placeholder="Example: What are the applications of Generative AI?"
)


if st.button("Run Research"):

    if not question.strip():

        st.warning("Please enter a question.")

    else:

        initial_state = {
            "question": question,
            "research": "",
            "answer": "",
            "error": ""
        }

        with st.spinner("Agents are working..."):

            result = workflow_app.invoke(initial_state)

        # Check for errors
        if result.get("error"):

            st.error(result["error"])

        else:

            st.success("Workflow completed successfully!")

            st.subheader("📝 Final Answer")

            st.write(result["answer"])

            with st.expander("🔎 Research Agent Output"):

                st.write(result["research"])