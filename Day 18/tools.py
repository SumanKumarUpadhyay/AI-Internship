import wikipedia

def search_wikipedia(query):
    try:
        # Search first
        results = wikipedia.search(query)

        if not results:
            return "No information found."

        # Get summary of the first matching topic
        summary = wikipedia.summary(results[0], sentences=3)

        return summary

    except Exception:
        return "No information found."