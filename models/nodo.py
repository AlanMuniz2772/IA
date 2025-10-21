class Nodo:
    """Representa un nodo en el grafo o árbol."""

    def __init__(self, estado, padre=None, costo=0, heuristica=0):
        self.estado = estado
        self.padre = padre
        self.costo = costo  # costo real g(n)
        self.heuristica = heuristica  # estimación h(n)
        self.hijos = []

    @property
    def costo_total(self):
        """Devuelve f(n) = g(n) + h(n)."""
        return self.costo + self.heuristica

    def __lt__(self, other):
        """Permite comparar nodos por su costo total (para usar en colas de prioridad)."""
        return self.costo_total < other.costo_total
