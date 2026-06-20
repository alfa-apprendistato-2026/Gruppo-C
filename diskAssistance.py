"""Sostituisci
MemorySaver
con
SqliteSaver
e verifica la persistenza al riavvio.
1.
Crea
checkpoints.db
con
SqliteSaver
2.
Fai una domanda e ottieni risposta
3.
Chiudi il programma
4.
Riavvia lo script (senza cancellare il DB)
5.
Fai una domanda di follow-up nello stesso
thread_id
6.
Verifica che l'agente ricordi il contesto"""
import sqlite3
from langchain_ollama import ChatOllama
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.prebuilt import create_react_agent
import uuid



llm = ChatOllama(
    model="llama3.2",
    base_url="http://localhost:11434",
    temperature=0
)

conn = sqlite3.connect("checkpoints.db", check_same_thread=False)
memory_db = SqliteSaver(conn)

agent = create_react_agent(
    llm,
    tools=[],
    checkpointer=memory_db # ← abilita il checkpoint
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

    


