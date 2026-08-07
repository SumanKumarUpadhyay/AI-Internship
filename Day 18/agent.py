from planner import choose_tool
from tools import search_wikipedia
from prompts import agent_prompt
from llm import llm


def run_agent(question):

    # Step 1: Planner
    tool = choose_tool(question)

    # Step 2: Tool
    if tool == "wikipedia":
        tool_result = search_wikipedia(question)

    else:
        tool_result = "No tool available."

    # Step 3: Create Prompt
    prompt = agent_prompt.format(
        question=question,
        tool_result=tool_result
    )

    # Step 4: Generate Answer
    response = llm.invoke(prompt)

    return response.content