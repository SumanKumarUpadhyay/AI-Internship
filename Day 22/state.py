from typing import TypedDict


class AgentState(TypedDict):

    question: str
    research: str
    analysis: str
    critique: str
    answer: str