from langgraph.graph import StateGraph, START, END

from state import AgentState
from agents import (
    coordinator_agent,
    research_agent,
    writer_agent
)


# Create the graph
graph = StateGraph(AgentState)


# Add agents as nodes
graph.add_node("coordinator", coordinator_agent)
graph.add_node("research", research_agent)
graph.add_node("writer", writer_agent)


# Define workflow
graph.add_edge(START, "coordinator")
graph.add_edge("coordinator", "research")
graph.add_edge("research", "writer")
graph.add_edge("writer", END)


# Compile workflow
app = graph.compile()