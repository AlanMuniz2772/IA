"""Node representation compatible with the generic search graph."""


class Nodo:
    """Represent a node within the search tree or graph."""

    def __init__(self, estado, padre=None, costo: int = 0, heuristica: float = 0.0):
        self.estado = estado
        self.padre = padre
        self.costo = costo  # g(n)
        self.heuristica = heuristica  # h(n)
        self.hijos = []

    @property
    def costo_total(self) -> float:
        """Return f(n) = g(n) + h(n)."""
        return self.costo + self.heuristica

    def __lt__(self, other: "Nodo") -> bool:
        """Allow comparison by total cost to work with priority queues."""
        return self.costo_total < other.costo_total
