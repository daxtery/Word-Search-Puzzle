from typing import List


class Puzzle:
    def __init__(self, rows: List[List[str]]):
        self.rows = rows

    def get(self, row: int, column: int) -> str:
        return self.rows[row][column]

    def set(self, character: str, row: int, column: int):
        self.rows[row][column] = character

    def in_bounds(self, row: int, column: int) -> bool:
        return 0 <= row < len(self.rows) and 0 <= column < len(self.rows[row])

    def __copy__(self):
        return Puzzle(self.rows.copy())

class PuzzleConstructor:
    @staticmethod
    def construct(path: str) -> Puzzle:
        with open(path, 'r') as file:
            number_of_lines = int(file.readline())
            # skip the next lines because they have the words we are looking for
            # which we do not care about
            for i in range(number_of_lines):
                file.readline()
            lines: List[str] = []
            while True:
                line = file.readline()
                if line == "":
                    break
                lines.append(line)
            return Puzzle(lines)
