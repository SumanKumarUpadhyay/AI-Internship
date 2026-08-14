from agents import coordinator_agent


def test_coordinator_agent():

    state = {
        "question": "What is Generative AI?",
        "research": "",
        "answer": "",
        "error": ""
    }

    result = coordinator_agent(state)

    assert result["question"] == "What is Generative AI?"
    assert result["error"] == ""