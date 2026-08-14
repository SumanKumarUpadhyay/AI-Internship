from state import AgentState


def test_agent_state():

    state: AgentState = {
        "question": "What is Generative AI?",
        "research": "",
        "answer": "",
        "error": ""
    }

    assert state["question"] == "What is Generative AI?"
    assert state["research"] == ""
    assert state["answer"] == ""
    assert state["error"] == ""