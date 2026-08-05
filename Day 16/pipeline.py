from retriever import retriever
from prompt_template import support_prompt
from llm import llm


def run_rag(query):

    # Retrieve relevant document
    results = retriever.invoke(query)

    # Extract context
    context = results[0].page_content

    # Create prompt
    prompt = support_prompt.format(
        context=context,
        user_query=query
    )

    # Generate answer
    response = llm.invoke(prompt)

    return response.content