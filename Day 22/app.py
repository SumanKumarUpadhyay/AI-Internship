import streamlit as st


st.set_page_config(
    page_title="Multi-Agent Research Assistant",
    page_icon="🤖"
)


st.title("🤖 Multi-Agent Research Assistant")

st.write(
    "Research → Analyze → Critic → Writer"
)

question = st.text_area(
    "Enter your research question:",
    placeholder="Example: What are the applications of Generative AI?"
)


if st.button("Run Research"):

    if not question.strip():
        st.warning("Please enter a question.")

    else:

        # Import workflow only when needed
        from workflow import app as workflow_app

        initial_state = {
            "question": question,
            "research": "",
            "analysis": "",
            "critique": "",
            "answer": ""
        }

        with st.spinner("AI Agents are working..."):

            result = workflow_app.invoke(initial_state)

        st.success("Research completed!")

        st.subheader("📝 Final Answer")

        st.write(result["answer"])

        with st.expander("🔎 Research Agent"):
            st.write(result["research"])

        with st.expander("📊 Analyzer"):
            st.write(result["analysis"])

        with st.expander("🧐 Critic"):
            st.write(result["critique"])