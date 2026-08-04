from prompt import support_prompt
from llm import llm

# User Question
question = input("Ask your question: ")

# Create Prompt
final_prompt = support_prompt.format(
    user_query=question
)


print("\nAI Response\n")

# Send Prompt to LLM
response = llm.invoke(final_prompt)

print(response.content)