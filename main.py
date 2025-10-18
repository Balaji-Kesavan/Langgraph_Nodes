# main.py
from typing import TypedDict, NotRequired
from langgraph.graph import StateGraph, END


# Step 1. Define the shared state structure
class State(TypedDict):
    user_input: str
    summary: NotRequired[str]
    final_output: NotRequired[str]


# Step 2. Define your first agent (ResearchAgent)
def research_agent(state: State):
    """Agent that does some basic research logic."""
    topic = state["user_input"]
    print(f"[ResearchAgent] Received topic: {topic}")

    # simulate research
    findings = f"AI agents in LangGraph communicate via shared state and edges."

    print(f"[ResearchAgent] Summary generated: {findings}")
    return {"summary": findings}


# Step 3. Define your second agent (WriterAgent)
def writer_agent(state: State):
    """Agent that uses summary to generate final output."""
    summary = state.get("summary", "")
    print(f"[WriterAgent] Received summary: {summary}")

    article = f"Here's a detailed explanation article: {summary}\n\nConclusion: Multi-agent systems can be easily built with LangGraph!"
    print(f"[WriterAgent] Final article ready.")
    return {"final_output": article}


# Step 4. Build the LangGraph
def build_graph():
    graph = StateGraph(State)

    # Add agents (nodes)
    graph.add_node("ResearchAgent", research_agent)
    graph.add_node("WriterAgent", writer_agent)

    # Define communication (edges)
    graph.set_entry_point("ResearchAgent")  # Set the starting point
    graph.add_edge("ResearchAgent", "WriterAgent")
    graph.add_edge("WriterAgent", END)

    # (Optional) conditional routing
    # graph.add_conditional_edges("ResearchAgent", lambda state: "WriterAgent" if "summary" in state else END)

    return graph.compile()


# Step 5. Run the workflow
if __name__ == "__main__":
    compiled_graph = build_graph()

    print("\n=== Starting LangGraph Agent Communication ===\n")

    result = compiled_graph.invoke({"user_input": "How do agents talk in LangGraph?"})

    print("\n=== Workflow Complete ===\n")
    print(result)
