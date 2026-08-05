from langchain_community.vectorstores import FAISS

from embeddings import embedding_model
from text_splitter import chunks

vector_db = FAISS.from_documents(
    chunks,
    embedding_model
)