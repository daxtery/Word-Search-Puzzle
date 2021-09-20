from enum import Enum
from itertools import islice
from typing import Tuple


class Orientation(Enum):
    value: Tuple[int, int]

    Horizontal = (1, 0)
    Vertical = (0, 1)
    Diagonal = (1, 1)
    AntiDiagonal = (-1, 1)


def inverted_orientation_vector(orientation: Orientation):
    return -orientation.value[0], -orientation.value[1]


def generate_cells_in_direction(
    start: Tuple[int, int], orientation: Orientation, inverted: bool
):
    x, y = start
    dx, dy = (
        orientation.value if not inverted else inverted_orientation_vector(orientation)
    )
    while True:
        yield x, y
        x += dx
        y += dy


def generate_cells_for_word(
    start: Tuple[int, int], orientation: Orientation, inverted: bool, word: str
):
    return enumerate(
        islice(
            generate_cells_in_direction(start, orientation, inverted),
            1,
            len(word),
        ),
        1,
    )
