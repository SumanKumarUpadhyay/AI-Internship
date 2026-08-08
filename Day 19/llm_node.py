from llm import llm
from prompts import rag_prompt


def generate_answer(state):

    question = state["question"]
    context = state["context"]

    prompt = rag_prompt.format(
        question=question,
        context=context
    )

    response = llm.invoke(prompt)

    return {
        "answer": response.content
    }