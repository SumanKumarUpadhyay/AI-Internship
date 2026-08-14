from typing import TypedDict

class AgentState(TypedDict):
    question: str
    research : str
    answer : str
    error : str

    