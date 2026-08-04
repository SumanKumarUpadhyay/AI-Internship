from langchain_core.prompts import PromptTemplate

# Create Prompt Template
support_prompt = PromptTemplate(
    input_variables=["user_query"],
    template="""
You are a helpful AI Support Assistant.

Your job is to answer the user's question clearly and politely.

User Question:
{user_query}

Provide:
1. Simple Explanation
2. Suggested Solution
3. Important Notes
"""
)

# Test Prompt Template
if __name__ == "__main__":

    final_prompt = support_prompt.format(
        user_query="How do I reset my Gmail password?"
    )

    print(final_prompt)