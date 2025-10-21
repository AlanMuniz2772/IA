from abc import ABC, abstractmethod

class Grafo(ABC):
    """Clase abstracta que define la estructura general de un grafo."""

    def __init__(self):
        self.nodos = []

    def agregar_nodo(self, nodo):
        self.nodos.append(nodo)

    @abstractmethod
    def expandir(self, nodo):
        """Debe devolver los nodos sucesores."""
        pass
