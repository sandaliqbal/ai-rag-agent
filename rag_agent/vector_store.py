# vector_store.py

from typing import List
from langchain_core.documents import Document
from langchain_ollama import OllamaEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore


# --- Initialization ---------------------------------------------------------

# Use a singleton pattern so the vector store loads only once
_embeddings = OllamaEmbeddings(model="nomic-embed-text:latest")
_vector_store = InMemoryVectorStore(_embeddings)


# --- Public API -------------------------------------------------------------


def add_documents(documents: List[Document]):
    """Add documents to the global vector store."""
    return _vector_store.add_documents(documents=documents)


def similarity_search(query: str, k: int = 4):
    """Perform a similarity search on the global vector store."""
    return _vector_store.similarity_search(query, k=k)


def get_vector_store():
    """Expose the underlying vector store if needed elsewhere."""
    return _vector_store
