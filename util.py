from typing import List

from puzzle import Puzzle, Soup


def puzzle_from_file(path: str):
    with open(path, "r") as file:
        number_of_lines = int(file.readline())
        # skip the next lines because they have the words we are looking for
        # which we do not care about
        for i in range(number_of_lines):
            file.readline()

        lines: Soup = []

        while True:
            line = file.readline().strip()
            if line == "":
                break
            row: List[str] = []
            for character in line.split(" "):
                row.append(character)
            lines.append(row)

        return Puzzle(len(lines), len(lines[0]), lines)


def words_from_file(path: str) -> List[str]:
    with open(path, "r") as file:
        number_of_lines = int(file.readline())
        words = []
        for i in range(number_of_lines):
            words.append(file.readline().rstrip().upper())
        return words
