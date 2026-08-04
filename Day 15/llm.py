import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load .env file
load_dotenv()

# Read API Key
groq_api_key = os.getenv("GROQ_API_KEY")

# Create LLM
llm = ChatGroq(
    api_key=groq_api_key,
    model="llama-3.3-70b-versatile",
    temperature=0.2
)

# Test LLM
if __name__ == "__main__":

    response = llm.invoke("What is Artificial Intelligence?")

    print(response.content)