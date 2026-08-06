from document_loader import load_document
from text_splitter import split_document
from vector_store import create_vector_store
from retriever import create_retriever
from prompt_template import support_prompt
from llm import llm

# Global Retriever
retriever = None


def process_pdf(file_path):
    global retriever

    # Load PDF
    documents = load_document(file_path)

    # Split into Chunks
    chunks = split_document(documents)

    # Create Vector Database
    vector_db = create_vector_store(chunks)

    # Create Retriever
    retriever = create_retriever(vector_db)


def ask_question(question):

    if retriever is None:
        return "Please upload a PDF first."

    results = retriever.invoke(question)

    context = "\n".join(
    [doc.page_content for doc in results]
    )

    metadata = [
    doc.metadata for doc in results
    ]

    # Create Prompt
    prompt = support_prompt.format(
        context=context,
        question=question
    )

    # Generate Answer
    response = llm.invoke(prompt)

    return response.content