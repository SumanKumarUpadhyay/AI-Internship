from langgraph.graph import StateGraph, START, END

from state import AgentState
from retriever import retrieve
from llm_node import generate_answer
from memory import save_memory


# Error Node
def handle_error(state):

    return {
        "answer": "Sorry, I could not find relevant information."
    }


# Check whether context exists
def check_context(state):

    if state["context"]:
        return "generate"

    return "error"


# Create Graph
graph_builder = StateGraph(AgentState)


# Add Nodes
graph_builder.add_node("retrieve", retrieve)
graph_builder.add_node("generate", generate_answer)
graph_builder.add_node("memory", save_memory)
graph_builder.add_node("error", handle_error)


# Starting point
graph_builder.add_edge(START, "retrieve")


# Conditional Routing
graph_builder.add_conditional_edges(
    "retrieve",
    check_context,
    {
        "generate": "generate",
        "error": "error"
    }
)


# Normal Edges
graph_builder.add_edge("generate", "memory")
graph_builder.add_edge("memory", END)
graph_builder.add_edge("error", END)


# Compile Graph
graph = graph_builder.compile()