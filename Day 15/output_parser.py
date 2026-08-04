def parse_response(title, explanation, applications):

    print("\n========== AI Response ==========\n")

    print(f"Title : {title}\n")

    print(f"Explanation :\n{explanation}\n")

    print("Applications:")

    for app in applications:
        print(f"- {app}")


# Test

parse_response(
    title="Machine Learning",

    explanation="Machine Learning is a branch of Artificial Intelligence that enables systems to learn from data.",

    applications=[
        "Healthcare",
        "Finance",
        "Recommendation Systems"
    ]
)