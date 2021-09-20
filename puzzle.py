from typing import List, Tuple

Row = int
Column = int

Cell = Tuple[Row, Column]
Soup = List[List[str]]


class Puzzle:
    def __init__(self, rows: int, columns: int, letters: Soup):
        self.letters = letters
        self.rows = rows
        self.columns = columns

    def __getitem__(self, key: Cell):
        return self.letters[key[0]][key[1]]

    def __setitem__(self, key: Cell, value: str):
        self.letters[key[0]][key[1]] = value

    def in_bounds(self, cell: Cell):
        row, column = cell
        return 0 <= row < self.rows and 0 <= column < self.columns

    def __copy__(self):
        return Puzzle(self.rows, self.columns, self.letters.copy())

    def __repr__(self):
        parts = []
        for row in self.letters:
            line = []
            for c in row:
                line.append(c)
            parts.append(" ".join(line))
        return "\n".join(parts)
