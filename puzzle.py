from typing import List


class Puzzle:
    def __init__(self, rows: List[str]):
        self.rows = rows

    def get(self, row: int, column: int) -> str:
        return self.rows[row][column]

    def in_bounds(self, row: int, column: int) -> bool:
        return 0 <= row < len(self.rows) and 0 <= column < len(self.rows[row])

