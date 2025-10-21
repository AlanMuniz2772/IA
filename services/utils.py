"""Generic utility helpers shared across the project."""

import random
from typing import Sequence, TypeVar

T = TypeVar("T")


def random_choice(options: Sequence[T]) -> T:
    """Return a random element from the provided sequence."""
    return random.choice(options)
