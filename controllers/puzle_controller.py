"""Controller responsible for solving the 8-puzzle with A*."""

from __future__ import annotations

from dataclasses import dataclass
from heapq import heappop, heappush
from typing import List, Sequence, Tuple

from models.nodo import Nodo
from models.puzzle import PuzzleGraph, PuzzleState

# Type alias for clarity
Board = Tuple[int, ...]


@dataclass
class PuzzleResult:
    """Value object containing the outcome of the search."""

    path: List[PuzzleState]
    explored_nodes: int
    generated_nodes: int
    depth: int


class PuzzleController:
    """Coordinate the A* search over the puzzle graph."""

    def __init__(self, heuristic: str = "manhattan") -> None:
        self.heuristic_name = heuristic

    def resolver(self, initial_state: Sequence[int], goal_state: Sequence[int]) -> PuzzleResult:
        """Run the A* search algorithm and return the resulting path."""
        initial = PuzzleState(self._normalize_state(initial_state))
        goal = PuzzleState(self._normalize_state(goal_state))

        # if not self._is_solvable(initial.tiles, goal.tiles):
        #     raise ValueError("The provided puzzle configuration is not solvable.")

        graph = PuzzleGraph(goal_state=goal, heuristic_name=self.heuristic_name)
        open_nodes: List[Nodo] = []
        closed_costs: dict[PuzzleState, int] = {}

        root = Nodo(
            estado=initial,
            padre=None,
            costo=0,
            heuristica=graph.heuristic(initial.tiles, goal.tiles),
        )
        heappush(open_nodes, root)

        explored = 0
        generated = 1

        while open_nodes:
            current = heappop(open_nodes)
            explored += 1

            self._print_state("Exploring", current.estado, current.costo, current.heuristica)

            if current.estado == goal:
                path = self._reconstruct_path(current)
                return PuzzleResult(
                    path=path,
                    explored_nodes=explored,
                    generated_nodes=generated,
                    depth=len(path) - 1,
                )

            if current.estado in closed_costs and closed_costs[current.estado] <= current.costo:
                continue

            closed_costs[current.estado] = current.costo

            for child in graph.expandir(current):
                generated += 1
                self._print_state("Generated", child.estado, child.costo, child.heuristica)

                previous_cost = closed_costs.get(child.estado)
                if previous_cost is not None and previous_cost <= child.costo:
                    continue

                heappush(open_nodes, child)

        raise RuntimeError("Failed to find a solution for the puzzle.")

    def _print_state(self, prefix: str, state: PuzzleState, cost: int, heuristic: float) -> None:
        """Print the state with the associated costs."""
        print(f"{prefix} state (g={cost}, h={heuristic}, f={cost + heuristic}):")
        print(state.pretty())
        print("-" * 20)

    @staticmethod
    def _normalize_state(state: Sequence[int]) -> Board:
        """Validate and convert a state sequence to the internal tuple form."""
        if len(state) != 9:
            raise ValueError("El puzzle debe contener 9 valores")
        normalized = tuple(int(value) for value in state)
        if sorted(normalized) != list(range(9)):
            raise ValueError("El puzzle debe contener los numeros del 0 al 8 sin repetidos")
        return normalized

    @staticmethod
    def _reconstruct_path(node: Nodo) -> List[PuzzleState]:
        """Build the sequence of states from the root to the given node."""
        path: List[PuzzleState] = []
        current = node
        while current is not None:
            path.append(current.estado)
            current = current.padre
        path.reverse()
        return path

    # @staticmethod
    # def _is_solvable(initial: Board, goal: Board) -> bool:
    #     """Return True if both configurations share the same parity of inversions."""
    #     return PuzzleController._count_inversions(initial) % 2 == PuzzleController._count_inversions(goal) % 2

    # @staticmethod
    # def _count_inversions(board: Board) -> int:
    #     """Count how many tile inversions exist in the flattened board."""
    #     values = [tile for tile in board if tile != 0]
    #     inversions = 0
    #     for index, value in enumerate(values[:-1]):
    #         for other in values[index + 1 :]:
    #             if value > other:
    #                 inversions += 1
    #     return inversions
