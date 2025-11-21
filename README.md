
# AI RAG Agent

Lightweight Retrieval-Augmented Generation (RAG) helper and example agent for working with documents, vector stores, and retrieval pipelines.

This repository contains a small, opinionated implementation of components commonly used in RAG systems: document loading and splitting, a vector store wrapper, a retriever, and a simple agent orchestration layer.

## Quick Overview

- **Language:** Python
- **Structure:** core agent and helper modules under `rag_agent/`
- **Purpose:** provide reusable tooling to load documents, split them into chunks, create/restore a vector store, and run a retrieval-first agent loop.

## Quick Start

1. Create and activate a virtual environment (macOS / zsh):

```bash
uv sync
source .venv/bin/activate
```
This creates a virtual environment and installs dependencies.

2. Run the example entry point:

```bash
uv run main.py
```

Note: Configure any necessary environment variables or API keys required by your LLM or vector backend (for example `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, etc.) before running.

## Project Layout

- `main.py` — example runner / entry point for the demo agent.
- `pyproject.toml` — project metadata and dependencies.
- `rag_agent/` — core package with modules:
	- `agent.py` — orchestrates agent loop and tools to handle queries.
	- `doc_loader.py` — helpers to load documents from disk or sources.
	- `doc_splitter.py` — logic for chunking documents into retrievable pieces.
	- `retriever.py` — high-level retriever logic that queries the vector store.
	- `vector_store.py` — wrapper around a vector database or in-memory store.
	- `tools.py` — miscellaneous utilities used by the agent and pipeline.
- `data_pipeline` — sample pdf to ingest data.

## Usage Notes

- The repository is intentionally small so you can adapt the components to your preferred LLM provider and vector store (FAISS, Chroma, Pinecone, etc.).
- Ensure any provider API keys are set in your environment; the code reads keys/credentials from environment variables or a configuration you supply.
- If you plan to persist vectors, point `vector_store.py` to a persisted backend; otherwise the sample may use an in-memory store.

## Contributing

Contributions are welcome. Typical contributions include:

- Improving or adding document loaders.
- Adding support for additional vector backends.
- Enhancing the agent orchestration and tool integrations.

Please open issues or PRs against the `main` branch.

## Contact

If you have questions, ping @sandaliqbal or open an issue.

