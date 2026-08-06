from langchain_community.vectorstores import FAISS
from embeddings import embedding_model


def create_vector_store(chunks):

    vector_db = FAISS.from_documents(
        chunks,
        embedding_model
    )

    return vector_db