"""Controlador encargado de resolver el 8-puzzle con A*."""

from dataclasses import dataclass
from heapq import heappop, heappush


from models.nodo import Nodo
from models.puzzle import PuzzleGraph, PuzzleState


@dataclass
class PuzzleResult:
    """Objeto de valor que resume el resultado de la busqueda."""

    process: list[str]
    path: list[PuzzleState]
    explored_nodes: int
    generated_nodes: int
    depth: int


class PuzzleController:
    """Coordina la busqueda A* sobre el grafo del rompecabezas."""

    def __init__(self, heuristic: str = "misplaced") -> None:
        self.heuristic_name = heuristic
    
    def resolver(self, initial_state: tuple[int], goal_state: tuple[int]) -> PuzzleResult:
        """Inicia la busqueda A* desde el estado inicial hasta el estado meta."""
        initial = PuzzleState(self._normalize_state(initial_state))
        goal = PuzzleState(self._normalize_state(goal_state))

        # if not self._is_solvable(initial.tiles, goal.tiles):
        #     raise ValueError("La configuracion proporcionada no es resoluble.")

        graph = PuzzleGraph(goal_state=goal, heuristic_name=self.heuristic_name)
        open_nodes: list[Nodo] = []
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

        process: list[str] = []

        return self._ejecutar_busqueda(
            goal,
            graph,
            open_nodes,
            closed_costs,
            process,
            explored,
            generated,
        )

    def _ejecutar_busqueda(
        self,
        goal: PuzzleState,
        graph: PuzzleGraph,
        open_nodes: list[Nodo],
        closed_costs: dict[PuzzleState, int],
        process: list[str],
        explored: int,
        generated: int,
    ) -> PuzzleResult:
        """Contiene el ciclo principal de la busqueda A*."""
        while open_nodes:
            current = heappop(open_nodes)
            explored += 1

            process.append(
                self._get_state(
                    "EXPLORANDO",
                    current.estado,
                    current.costo,
                    current.heuristica,
                )
            )

            if current.estado == goal:
                path = self._reconstruct_path(current)
                return PuzzleResult(
                    process=process,
                    path=path,
                    explored_nodes=explored,
                    generated_nodes=generated,
                    depth=len(path) - 1,
                )

            # Omite si ya se encontro una ruta mejor hacia este estado
            if (
                current.estado in closed_costs
                and closed_costs[current.estado] <= current.costo 
            ):
                continue

            closed_costs[current.estado] = current.costo

            for child in graph.expandir(current):
                generated += 1
                process.append(
                    self._get_state(
                        "Generando",
                        child.estado,
                        child.costo,
                        child.heuristica,
                    )
                )

                # Omite si ya se encontro una ruta mejor hacia este estado
                previous_cost = closed_costs.get(child.estado)
                if previous_cost is not None and previous_cost <= child.costo:
                    continue

                heappush(open_nodes, child)

        raise RuntimeError("Fallo al encontrar una solucion para el puzzle.")

    def _get_state(self, prefix: str, state: PuzzleState, cost: int, heuristic: float) -> None:
        """Compone el estado con los costos asociados."""
        if prefix == "EXPLORANDO":
            multiplier  = 60
        else:
            multiplier = 20
        return f"{prefix} estado (g={cost}, h={heuristic}, f={cost + heuristic}):\n{state.pretty()}\n{'-' * multiplier}"

    @staticmethod
    def _normalize_state(state: tuple[int]) -> tuple:
        """Valida y normaliza la representacion del estado del puzzle."""
        if len(state) != 9:
            raise ValueError("El puzzle debe contener 9 valores")
        normalized = tuple(int(value) for value in state)
        if sorted(normalized) != list(range(9)):
            raise ValueError("El puzzle debe contener los numeros del 0 al 8 sin repetidos")
        return normalized

    @staticmethod
    def _reconstruct_path(node: Nodo) -> list[PuzzleState]:
        """Reconstruye la secuencia de estados desde la raiz hasta el nodo final."""
        path: list[PuzzleState] = []
        current = node
        while current is not None:
            path.append(current.estado)
            current = current.padre
        path.reverse()
        return path
