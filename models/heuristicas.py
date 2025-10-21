"""Heuristic functions for the 8-puzzle search problem."""

from __future__ import annotations

from math import sqrt
from typing import Callable, Dict, Tuple

Board = Tuple[int, ...]


def manhattan_distance(current: Board, goal: Board) -> int:
    """Return the Manhattan distance between the current and goal positions."""
    distance = 0
    positions = {value: index for index, value in enumerate(goal)}

    for index, value in enumerate(current):
        if value == 0:
            continue
        goal_index = positions[value]
        current_row, current_col = divmod(index, 3)
        goal_row, goal_col = divmod(goal_index, 3)
        distance += abs(current_row - goal_row) + abs(current_col - goal_col)

    return distance


def misplaced_tiles(current: Board, goal: Board) -> int:
    """Return the number of tiles that are not in their goal position."""
    return sum(
        1
        for index, value in enumerate(current)
        if value != 0 and value != goal[index]
    )


def euclidean_distance(current: Board, goal: Board) -> float:
    """Return the Euclidean distance between the current and goal positions."""
    distance = 0.0
    positions = {value: index for index, value in enumerate(goal)}

    for index, value in enumerate(current):
        if value == 0:
            continue
        goal_index = positions[value]
        current_row, current_col = divmod(index, 3)
        goal_row, goal_col = divmod(goal_index, 3)
        distance += sqrt(
            (current_row - goal_row) ** 2 + (current_col - goal_col) ** 2
        )

    return distance


def get_heuristic(name: str) -> Callable[[Board, Board], float]:
    """Return the selected heuristic function by name."""
    heuristics: Dict[str, Callable[[Board, Board], float]] = {
        "manhattan": manhattan_distance,
        "misplaced": misplaced_tiles,
        "euclidean": euclidean_distance,
    }

    try:
        return heuristics[name]
    except KeyError as error:
        available = ", ".join(sorted(heuristics))
        raise ValueError(f"Unknown heuristic '{name}'. Available: {available}") from error
