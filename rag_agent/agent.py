from langchain.agents import create_agent
from langchain_ollama import ChatOllama
from rag_agent.tools import retrieve_context

llm = ChatOllama(
    model="gpt-oss:20b",
    temperature=0,
    # other params...
)
tools = [retrieve_context]
# If desired, specify custom instructions
prompt = (
    "You have access to a tool that retrieves context from a pdf file. "
    "Use the tool to help answer user queries."
)
agent = create_agent(llm, tools, system_prompt=prompt)
