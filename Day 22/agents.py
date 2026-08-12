from llm import llm
from state import AgentState


def research_agent(state: AgentState):

    question = state["question"]

    response = llm.invoke(
        f"""
You are a Research Agent.

Research the following question and provide
important and useful information.

Question:
{question}

Give clear points and examples.
"""
    )

    return {
        "research": response.content
    }


def analyzer_agent(state: AgentState):

    research = state["research"]

    response = llm.invoke(
        f"""
You are an Analyzer Agent.

Analyze the following research.
Identify the important points, facts,
and useful findings.

Research:
{research}

Give a clear and structured analysis.
"""
    )

    return {
        "analysis": response.content
    }


def critic_agent(state: AgentState):

    analysis = state["analysis"]

    response = llm.invoke(
        f"""
You are a Critic Agent.

Review the following analysis.

Check:
- Missing important points
- Clarity
- Logical problems
- Possible improvements

Analysis:
{analysis}

Give short and useful feedback.
"""
    )

    return {
        "critique": response.content
    }


def writer_agent(state: AgentState):

    question = state["question"]
    research = state["research"]
    analysis = state["analysis"]
    critique = state["critique"]

    response = llm.invoke(
        f"""
You are a Writer Agent.

Create the final answer for the user's question.

Question:
{question}

Research:
{research}

Analysis:
{analysis}

Critic Feedback:
{critique}

Write a clear, well-structured answer.
Use headings and bullet points where useful.
"""
    )

    return {
        "answer": response.content
    }