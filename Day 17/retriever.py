def create_retriever(vector_db):

    retriever = vector_db.as_retriever()

    return retriever