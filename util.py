from enum import Enum
from typing import List, Tuple

from puzzle import Puzzle


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


class PuzzleConstructorFromFile:
    @staticmethod
    def construct(path: str) -> Puzzle:
        with open(path, 'r') as file:
            number_of_lines = int(file.readline())
            # skip the next lines because they have the words we are looking for
            # which we do not care about
            for i in range(number_of_lines):
                file.readline()
            lines: List[List[str]] = []
            while True:
                line = file.readline().strip()
                if line == "":
                    break
                row: List[str] = []
                for character in line.split(" "):
                    row.append(character)
                lines.append(row)
            return Puzzle(lines)


def read_words_looking_for_from_file(path: str) -> List[str]:
    with open(path, 'r') as file:
        number_of_lines = int(file.readline())
        words = []
        for i in range(number_of_lines):
            words.append(file.readline().rstrip().upper())
        return words
