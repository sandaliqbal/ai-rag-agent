from rag_agent.doc_loader import load_documents
from rag_agent.doc_splitter import split_document
from rag_agent.vector_store import add_documents
from rag_agent.agent import agent


def main():
    print("Hello from ai-rag-agent!")
    file_path = "data_pipeline/nke-10k-2023.pdf"
    docs = load_documents(file_path)
    print(f"Loaded {len(docs)} documents.")
    all_splits = split_document(docs)
    add_documents(all_splits)
    query = (
        "How many distribution centers does Nike have in the US?",
        "When was Nike incorporated?",
    )

    for event in agent.stream(
        {"messages": [{"role": "user", "content": query}]},
        stream_mode="values",
    ):
        event["messages"][-1].pretty_print()


if __name__ == "__main__":
    main()
