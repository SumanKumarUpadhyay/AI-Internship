from llm import llm
from tools import analyze_csv


def run_agent(question, file_path):

    response = llm.invoke(
        f"""
You are an AI Data Analysis Assistant.

Decide whether the CSV Analyzer tool is required.

User Question:
{question}

If the question requires analyzing the uploaded CSV,
respond with exactly:
USE_CSV_TOOL

Otherwise, answer the question normally.
"""
    )

    if "USE_CSV_TOOL" in response.content:

        result = analyze_csv(file_path)

        final_response = llm.invoke(
            f"""
You are an AI Data Analysis Assistant.

User Question:
{question}

CSV Analysis Result:
{result}

Give a clear and concise answer based on the CSV analysis.
Use bullet points when useful.
"""
        )

        return final_response.content

    return response.content