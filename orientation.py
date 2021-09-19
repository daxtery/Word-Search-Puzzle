from enum import Enum
from typing import Tuple


class Orientation(Enum):
    value: Tuple[int, int]

    Horizontal = (1, 0)
    Vertical = (0, 1)
    Diagonal = (1, 1)
    AntiDiagonal = (-1, 1)


def inverted_orientation_vector(orientation: Orientation):
    return -orientation.value[0], -orientation.value[1]
