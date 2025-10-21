"""Domain model for the 8-puzzle problem."""

from typing import Tuple, List

from models.grafo_base import Grafo
from models.nodo import Nodo
from models.heuristicas import get_heuristic

Board = Tuple[int, ...]


class PuzzleState:
    """Immutable representation of a 3x3 sliding puzzle configuration."""

    def __init__(self, tiles):
        if len(tiles) != 9:
            raise ValueError("Debe contener 9 valores")
        self.tiles: Board = tuple(tiles) 

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, PuzzleState):
            return False
        return self.tiles == other.tiles

    def __hash__(self) -> int:
        return hash(self.tiles)

    def __repr__(self) -> str:
        return f"PuzzleState({self.tiles})"

    def index_of(self, value: int) -> int:
        """Return the position of the requested tile."""
        return self.tiles.index(value)

    def as_matrix(self):
        """Return the board as a 3x3 matrix for display purposes."""
        return [list(self.tiles[i : i + 3]) for i in range(0, 9, 3)]

    def neighbors(self):
        """Generate all reachable states after one valid move."""
        blank_index = self.index_of(0) # 0 represents the blank tile
        row, col = divmod(blank_index, 3) # Get row and column of the blank tile
        swaps = []

        # adds swaps for each given position of the blank tile
        # if is on the border  it doesnt add up
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
        """Return a multi-line representation of the board."""
        lines = []
        for row in self.as_matrix():
            formatted_row = " ".join("_" if value == 0 else str(value) for value in row)
            lines.append(formatted_row)
        return "\n".join(lines)


class PuzzleGraph(Grafo):
    """Concrete graph implementation for the 8-puzzle search space."""

    def __init__(self, goal_state: PuzzleState, heuristic_name: str = "misplaced"):
        super().__init__()
        self.goal_state = goal_state
        self.heuristic = get_heuristic(heuristic_name)

    def expandir(self, nodo: Nodo):
        """Return all successor nodes reachable from the provided node."""
        successors: List[Nodo] = []
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
