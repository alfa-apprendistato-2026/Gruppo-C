"""Completa il seguente schema TypedDict per un agente di supporto clienti."""

from typing import TypedDict, Annotated
from langgraph.graph.message import add_messages
class SupportState(TypedDict):
    messages: Annotated[list[str], add_messages]
    ticket_id: int
    resolved: False # bool con valore di default . o no?
    notes: list[str] # lista di stringhe che si accumulano