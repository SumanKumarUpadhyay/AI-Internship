from langchain_core.prompts import PromptTemplate

support_prompt = PromptTemplate(
    input_variables=["context", "user_query"],
    template="""
You are an AI Support Assistant.

Answer the question using only the given context.

Context:
{context}

Question:
{user_query}

Answer:
"""
)