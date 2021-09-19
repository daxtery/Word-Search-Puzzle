from enum import Enum
from typing import Tuple


class Orientation(Enum):
    Horizontal = 1
    Vertical = 2
    Diagonal = 3
    AntiDiagonal = 4

    def get_vector(self) -> Tuple[int, int]:
        if self.name == self.Vertical.name:
            return 1, 0
        elif self.name == self.Horizontal.name:
            return 0, 1
        elif self.name == self.Diagonal.name:
            return 1, 1
        else:
            return -1, 1