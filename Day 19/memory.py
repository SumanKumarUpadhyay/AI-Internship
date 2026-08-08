def save_memory(state):

    messages = state["messages"]

    messages.append(
        {
            "role": "user",
            "content": state["question"]
        }
    )

    messages.append(
        {
            "role": "assistant",
            "content": state["answer"]
        }
    )

    return {
        "messages": messages
    }