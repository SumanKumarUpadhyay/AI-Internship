while True:
    user = input("\nYou: ").lower()

    if "hello" in user or "hi" in user:
        print("AI: Hello! How can I help you?")

    elif "your name" in user:
        print("AI: My name is Simple AI Assistant.")

    elif "python" in user:
        print("AI: Python is a popular programming language used in AI, ML, Web Development, and Data Science.")

    elif "ai" in user:
        print("AI: Artificial Intelligence enables machines to perform tasks that normally require human intelligence.")

    elif "ml" in user:
        print("AI: Machine Learning is a branch of AI where computers learn from data.")

    elif "bye" in user or "exit" in user:
        print("AI: Thank you! Have a nice day.")
        break

    else:
        print("AI: Sorry, I don't understand that. Please ask another question.")