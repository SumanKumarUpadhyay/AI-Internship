from state import AgentState
from llm import llm


def coordinator_agent(state: AgentState):

    question = state["question"]

    # Coordinator simply prepares the task
    return {
        "question": question,
        "error": ""
    }


def research_agent(state: AgentState):

    question = state["question"]

    try:

        response = llm.invoke(
            f"""
You are a Research Agent.

Research the following question and provide
clear and useful information.

Question:
{question}

Give important points and simple examples.
"""
        )

        return {
            "research": response.content,
            "error": ""
        }

    except Exception as e:

        return {
            "research": "",
            "error": f"Research failed: {str(e)}"
        }


def writer_agent(state: AgentState):

    question = state["question"]
    research = state["research"]

    try:

        response = llm.invoke(
            f"""
You are a Writer Agent.

Create a clear final answer for the user's question
using the research provided below.

Question:
{question}

Research:
{research}

Write the answer in a simple and well-structured way.
Use headings and bullet points where useful.
"""
        )

        return {
            "answer": response.content,
            "error": ""
        }

    except Exception as e:

        return {
            "answer": "",
            "error": f"Writer failed: {str(e)}"
        }