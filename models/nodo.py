"""Nodo compatible con el grafo de busqueda generico."""


class Nodo:
    """Representa un nodo dentro del arbol o grafo de busqueda."""

    def __init__(self, estado, padre=None, costo: int = 0, heuristica: float = 0.0):
        self.estado = estado
        self.padre = padre
        self.costo = costo  # g(n)
        self.heuristica = heuristica  # h(n)
        self.hijos = []

    @property
    def costo_total(self) -> float:
        """Devuelve f(n) = g(n) + h(n)."""
        return self.costo + self.heuristica

    def __lt__(self, other: "Nodo") -> bool:
        """Permite comparar por costo total para usar colas de prioridad."""
        return self.costo_total < other.costo_total
    
    def __repr__(self) -> str:
        return (
            f"Nodo(estado={self.estado.tiles}, "
            f"costo={self.costo}, heuristica={self.heuristica}, "
            f"costo_total={self.costo_total})"
        )
