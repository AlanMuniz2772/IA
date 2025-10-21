"""Funciones heuristicas para la busqueda del 8-puzzle."""

from typing import Tuple

Board = Tuple[int, ...]


def misplaced_tiles(current: Board, goal: Board) -> int:
    """Devuelve cuantas fichas no estan en su posicion objetivo."""
    return sum(
        1
        for index, value in enumerate(current)
        if value != goal[index]
    )


def get_heuristic(name: str):
    """Devuelve la funcion heuristica seleccionada por nombre."""
    heuristics = {
        "misplaced": misplaced_tiles,
    }

    try:
        return heuristics[name]
    except KeyError as error:
        raise ValueError(f"Heuristica desconocida: {name}") from error
