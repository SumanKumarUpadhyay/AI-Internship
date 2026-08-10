from langchain_core.tools import tool
from tools import analyze_csv


@tool
def csv_analyzer():
    """
    Analyze the uploaded CSV file.
    """
    return "CSV Analyzer Tool"