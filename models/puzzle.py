"""Domain model for the 8-puzzle problem."""

from models.grafo_base import Grafo
from models.nodo import Nodo
from models.heuristicas import get_heuristic

class PuzzleState:
    """Reresentacion inmutable del estado del 8-puzzle."""

    def __init__(self, tiles):
        if len(tiles) != 9:
            raise ValueError("Debe contener 9 valores")
        self.tiles = tuple(tiles) 

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, PuzzleState):
            return False
        return self.tiles == other.tiles

    def __hash__(self) -> int:
        return hash(self.tiles)

    def __repr__(self) -> str:
        return f"PuzzleState({self.tiles})"

    def index_of(self, value: int) -> int:
        """Devuelve la posicion de la ficha solicitada."""
        return self.tiles.index(value)

    def as_matrix(self):
        """Devuelve el tablero como una matriz 3x3 para propositos de visualizacion."""
        return [list(self.tiles[i : i + 3]) for i in range(0, 9, 3)]

    def neighbors(self):
        """Genera todos los estados alcanzables despues de un movimiento valido."""
        blank_index = self.index_of(0) # 0 representa la ficha en blanco
        row, col = divmod(blank_index, 3) # Obtiene fila y columna de la ficha en blanco
        swaps = []

        # agrega intercambios para cada posicion dada del espacio en blanco
        # si esta en el borde no se agrega  
        if row > 0:
            swaps.append(blank_index - 3)
        if row < 2:
            swaps.append(blank_index + 3)
        if col > 0:
            swaps.append(blank_index - 1)
        if col < 2:
            swaps.append(blank_index + 1)

        # genera nuevos estados al intercambiar el espacio en blanco con las fichas adyacentes
        for swap_index in swaps:
            new_tiles = list(self.tiles)
            new_tiles[blank_index], new_tiles[swap_index] = (
                new_tiles[swap_index],
                new_tiles[blank_index],
            )
            yield tuple(new_tiles)

    def pretty(self) -> str:
        """Devuelve una representacion multilinea del tablero."""
        lines = []
        for row in self.as_matrix():
            formatted_row = " ".join("_" if value == 0 else str(value) for value in row)
            lines.append(formatted_row)
        return "\n".join(lines)


class PuzzleGraph(Grafo):
    """Grafo especifico para el 8-puzzle."""

    def __init__(self, goal_state: PuzzleState, heuristic_name: str = "misplaced"):
        super().__init__()
        self.goal_state = goal_state
        self.heuristic = get_heuristic(heuristic_name)

    def expandir(self, nodo: Nodo):
        """Devuelve todos los nodos sucesores alcanzables desde el nodo proporcionado."""
        successors: list[Nodo] = []
        current_state: PuzzleState = nodo.estado

        for candidate in current_state.neighbors():
            state = PuzzleState(candidate)
            cost = nodo.costo + 1
            heuristic_value = self.heuristic(state.tiles, self.goal_state.tiles)
            child = Nodo(
                estado=state,
                padre=nodo,
                costo=cost,
                heuristica=heuristic_value,
            )
            successors.append(child)

        return successors
