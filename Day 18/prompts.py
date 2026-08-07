from langchain_core.prompts import PromptTemplate

agent_prompt = PromptTemplate(
    input_variables=["question", "tool_result"],
    template="""
You are an AI Research Assistant.

Use the tool result to answer the user's question.

Question:
{question}

Tool Result:
{tool_result}

Provide a clear and simple answer.
"""
)