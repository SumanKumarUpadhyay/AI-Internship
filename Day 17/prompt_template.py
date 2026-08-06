from langchain_core.prompts import PromptTemplate

support_prompt = PromptTemplate(
    input_variables=["context", "question"],
    template="""
You are an AI Support Assistant.

Answer the user's question only using the given context.
Answer provided in bulleted points format.first some short paragraph then 2 to 3 to the point bulleted points.

Context:
{context}

Question:
{question}

Answer:
"""
)