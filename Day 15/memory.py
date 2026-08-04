# Chat History
chat_history = []

# Function to save conversation
def save_message(user, assistant):

    chat_history.append({
        "user": user,
        "assistant": assistant
    })


# Function to display chat history
def show_history():

    print("\nConversation History\n")

    for chat in chat_history:

        print(f"User      : {chat['user']}")
        print(f"Assistant : {chat['assistant']}")
        print("-" * 40)


# Test

save_message(
    "What is AI?",
    "AI stands for Artificial Intelligence."
)

save_message(
    "What is Machine Learning?",
    "Machine Learning is a subset of AI."
)

show_history()