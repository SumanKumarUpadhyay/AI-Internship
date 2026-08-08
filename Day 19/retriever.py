import wikipedia


def retrieve(state):

    question = state["question"]

    try:
        results = wikipedia.search(question)

        if not results:
            return {
                "context": ""
            }

        page = wikipedia.page(results[0], auto_suggest=False)

        context = page.content[:8000]

        return {
            "context": context
        }

    except Exception:
        return {
            "context": ""
        }