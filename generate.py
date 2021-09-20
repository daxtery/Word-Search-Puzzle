import random
import string
import sys
from typing import DefaultDict, List, Optional, Dict, Tuple

from puzzle import Puzzle, Soup
from orientation import (
    Orientation,
    generate_cells_for_word,
)

from dataclasses import dataclass


@dataclass
class PuzzleGeneratorConfig:
    rows: int
    columns: int
    words: List[str]
    orientations: List[Orientation]


def puzzle_generator_config_from_file(path: str):
    with open(path, "r") as file:
        line = file.readline()
        parts = line.split(" ")
        rows = int(parts[0])
        columns = int(parts[1])
        words = []
        while True:
            line = file.readline()
            if line == "":
                break
            words.append(line.strip().upper())
        return PuzzleGeneratorConfig(rows, columns, words, [o for o in Orientation])


class PuzzleConstructorFromConfig:
    def __init__(self, config: PuzzleGeneratorConfig, seed: int = 42):
        self.config = config
        random.seed(seed)

    def try_construct(self):

        letters = [[" "] * self.config.columns for _ in range(self.config.rows)]

        # We were unable to fit all the words there
        if not self._construct_from_config_helper(letters, 0):
            return None

        for i in range(self.config.rows):
            for j in range(self.config.columns):
                if letters[i][j] == " ":
                    letters[i][j] = random.choice(string.ascii_uppercase)

        return Puzzle(config.rows, config.columns, letters)

    def _in_bounds(self, row: int, collumn: int) -> bool:
        return 0 <= row < self.config.rows and 0 <= collumn < self.config.columns

    def _construct_from_config_helper(self, letters: Soup, index: int):
        # base case; we've added all the words we wanted to, yay!
        if index == len(config.words):
            return True

        word = config.words[index]
        possible_for_this_word = self._possible_points_with_orientation(word, letters)

        while len(possible_for_this_word) > 0:

            random_start_position = random.choice(list(possible_for_this_word.keys()))
            orientations_and_inverted = possible_for_this_word.pop(
                random_start_position
            )

            for orientation, inverted in orientations_and_inverted:

                previous_letters = [" "] * len(word)

                for (i, (row, column)) in generate_cells_for_word(
                    random_start_position, orientation, inverted, word
                ):
                    previous_letters[i] = letters[row][column]
                    letters[row][column] = word[i]

                if self._construct_from_config_helper(letters, index + 1):
                    return True

                for (i, (row, column)) in generate_cells_for_word(
                    random_start_position, orientation, inverted, word
                ):
                    letters[row][column] = previous_letters[i]

        return False

    def _possible_points_with_orientation(self, word: str, letters: Soup):
        start_points: Dict[
            Tuple[int, int], List[Tuple[Orientation, bool]]
        ] = DefaultDict(list)

        for row_index in range(self.config.rows):
            for letter_index in range(self.config.columns):

                cell = (row_index, letter_index)

                for orientation in random.sample(
                    self.config.orientations, len(self.config.orientations)
                ):
                    inverted_list = random.sample([True, False], 2)
                    for inverted in inverted_list:
                        if self._possible_with_location_and_orientation(
                            word,
                            letters,
                            cell,
                            orientation,
                            inverted,
                        ):
                            start_points[cell].append((orientation, inverted))

        return start_points

    def _possible_with_location_and_orientation(
        self,
        word: str,
        letters: Soup,
        location: Tuple[int, int],
        orientation: Orientation,
        inverted: bool,
    ) -> bool:

        for (index, (row, column)) in generate_cells_for_word(
            location, orientation, inverted, word
        ):
            if not self._in_bounds(row, column):
                return False

            if (letter := letters[row][column]) != " " and letter != word[index]:
                return False

        return True


if __name__ == "__main__":
    config = puzzle_generator_config_from_file(sys.argv[1])
    puzzle = PuzzleConstructorFromConfig(config).try_construct()
    assert puzzle, (
        f"Failed to create a puzzle with "
        f"{config.rows} * {config.columns}, words: {config.words}, orientations: {config.orientations}"
    )
    words_list = "\n".join([word for word in config.words])
    print(words_list)
    print(puzzle)
