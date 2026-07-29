import os
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
PERSIST_DIRECTORY = "./chroma_db"

def retrieve_context(query: str, k: int = 4) -> str:
    if not os.path.exists(PERSIST_DIRECTORY):
        return "No context available in vector store."
        
    vectorstore = Chroma(
        persist_directory=PERSIST_DIRECTORY, 
        embedding_function=embeddings
    )
    docs = vectorstore.similarity_search(query, k=k)
    return "\n\n".join([doc.page_content for doc in docs])