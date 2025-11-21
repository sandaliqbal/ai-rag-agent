from typing import List
from langchain_core.documents import Document
from langchain_core.runnables import chain
from rag_agent.vector_store import similarity_search


@chain
def retriever(query: str) -> List[Document]:
    return similarity_search(query, k=1)
