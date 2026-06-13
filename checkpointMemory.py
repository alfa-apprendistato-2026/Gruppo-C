"""Esercizio 1: Primo Checkpoint In-Memory
Obiettivo
Crea un agente ReAct con MemorySaver e verifica che ricordi il tuo nome.
1. Configura l'agente con checkpointer=MemorySaver()
2. Usa thread_id="test-1"
3. Turno 1: invia "Mi chiamo Alice"
4. Turno 2: invia "Qual è il mio nome?"
5. Verifica che la risposta contenga "Alice"
# BOZZA
from langgraph.checkpoint.memory import MemorySaver
# . completa tu"""

from langchain_ollama import ChatOllama
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent
import uuid


llm = ChatOllama(
    model="llama3.2",
    base_url="http://localhost:11434",
    temperature=0
)

memory = MemorySaver()

agent = create_react_agent(
    llm,
    tools=[],
    checkpointer=memory # ← abilita il checkpoint
)

id= str(uuid.uuid1())
print("id univoco: "+id)

config = {"configurable": {"thread_id": id}}


messages= ["Mi chiamo Alice", "Qual è il mio nome?"]


for i, message in enumerate(messages, 1):

    print(f"Turno {i}[Human]: "+str(message))

    response = agent.invoke(
        {"messages": [HumanMessage(content=message)]},
        config
    )

    print(f"Turno {i}[AI]: {response['messages'][-1].content}")

    


