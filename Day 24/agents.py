from state import AgentState
from llm import llm
from logger import logger


def coordinator_agent(state: AgentState):

    logger.info("Coordinator started")

    question = state["question"]

    logger.info("Question received by Coordinator")

    return {
        "question": question,
        "error": ""
    }


def research_agent(state: AgentState):

    logger.info("Research Agent started")

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

        logger.info("Research Agent completed successfully")

        return {
            "research": response.content,
            "error": ""
        }

    except Exception as e:

        logger.error(f"Research Agent failed: {e}")

        return {
            "research": "",
            "error": f"Research failed: {str(e)}"
        }


def writer_agent(state: AgentState):

    logger.info("Writer Agent started")

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

        logger.info("Writer Agent completed successfully")

        return {
            "answer": response.content,
            "error": ""
        }

    except Exception as e:

        logger.error(f"Writer Agent failed: {e}")

        return {
            "answer": "",
            "error": f"Writer failed: {str(e)}"
        }