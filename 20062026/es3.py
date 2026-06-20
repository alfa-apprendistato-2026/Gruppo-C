"""Creare una pipeline che prende un'idea di prompt molto semplice scritta da un utente e la trasforma,
step dopo step, in un prompt di sistema perfetto, strutturato e pronto per la produzione.
Deve avere uno stato custom e avere almeno 2 o tre nodi.
"""
from langgraph.graph import StateGraph, START, END
from langgraph.graph import MessagesState
from langgraph.graph import State

llm = ChatOllama(
    model="llama3.2",
    base_url="http://localhost:11434",
    temperature=0
)

def call_model(state: State):
    response = llm.invoke(state["messages"])
    return {"messages" : [response]}

builder = StateGraph(State)
builder.add_node("agent", call_model)
builder.add_edge(START, "agent")

graph = builder.compile() 
