import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load Environment Variables
load_dotenv()

# Create LLM
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0
)