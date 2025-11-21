from langchain_community.document_loaders import PyPDFLoader


def load_documents(file_path: str):
    """Load documents from a PDF file."""
    loader = PyPDFLoader(file_path)

    docs = loader.load()
    print(f"{len(docs)} documents loaded from {file_path}")
    return docs
