from langgraph.graph import StateGraph, START, END

from state import AgentState
from agents import (
    research_agent,
    analyzer_agent,
    critic_agent,
    writer_agent
)


# Create graph
graph = StateGraph(AgentState)


# Add agents as nodes
graph.add_node("research", research_agent)
graph.add_node("analyzer", analyzer_agent)
graph.add_node("critic", critic_agent)
graph.add_node("writer", writer_agent)


# Connect the workflow
graph.add_edge(START, "research")
graph.add_edge("research", "analyzer")
graph.add_edge("analyzer", "critic")
graph.add_edge("critic", "writer")
graph.add_edge("writer", END)


# Compile graph
app = graph.compile()