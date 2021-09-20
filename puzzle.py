from typing import List, Tuple

Row = int
Column = int

Cell = Tuple[Row, Column]


class Puzzle:
    def __init__(self, rows: List[List[str]]):
        self.rows = rows

    def __getitem__(self, key: Cell):
        return self.rows[key[0]][key[1]]

    def __setitem__(self, key: Cell, value: str):
        self.rows[key[0]][key[1]] = value

    def in_bounds(self, cell: Cell):
        row, column = cell
        return 0 <= row < len(self.rows) and 0 <= column < len(self.rows[row])

    def __copy__(self):
        return Puzzle(self.rows.copy())

    def __repr__(self):
        parts = []
        for row in self.rows:
            line = []
            for c in row:
                line.append(c)
            parts.append(" ".join(line))
        return "\n".join(parts)
