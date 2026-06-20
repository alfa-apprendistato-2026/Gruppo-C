"""Implementa un reducer che gestisca un set di tag stringa in modo che venga mantenuta l'unione
univoca.

Requisiti:
Se due nodi aggiungono tag in parallelo, il risultato finale deve contenere l'unione senza duplicati.
La funzione deve accettare (esistente, nuovo) come richiesto da LangGraph.
"""

from typing import Annotated, TypedDict

def merge_tags(existing: set[str], update: set[str]) -> set[str]:
    "Unisce i set existing e update escludendo duplicati"
    return existing | update

class TaskState(TypedDict):
    description: str
    tags: Annotated[set[str], merge_tags]
