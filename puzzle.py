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

    def __str__(self):
        parts = []
        for row in self.rows:
            line = []
            for c in row:
                line.append(c)
            parts.append(' '.join(line))
        return '\n'.join(parts)

    def __repr__(self):
        return self.__str__()
