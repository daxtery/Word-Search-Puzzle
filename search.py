from itertools import islice
import sys
from typing import DefaultDict, Dict, List, Tuple, Optional

from puzzle import Puzzle, Cell
from orientation import (
    Orientation,
    generate_cells_for_word,
)
from util import puzzle_from_file, words_from_file

from dataclasses import dataclass


@dataclass
class PuzzleWord:
    orientation: Orientation
    inverted: bool
    start: Cell
    end: Cell

    def __repr__(self):
        inverted = "Inverted " if self.inverted else ""
        return f"{self.start} --> {self.end} ({inverted}{self.orientation.name})"


class PuzzleWordsLookup:
    def __init__(self, words: List[str], puzzle: Puzzle):
        self.words = words
        self.puzzle = puzzle

    def resolve(self):
        words_in_puzzle = {word: self.look_for_word(word) for word in self.words}

        return words_in_puzzle

    def look_for_word(self, word: str):
        for row_index in range(self.puzzle.rows):
            for letter_index in range(self.puzzle.columns):
                cell = (row_index, letter_index)
                if self.puzzle[cell] == word[0]:
                    for orientation in Orientation:
                        for inverted in [True, False]:
                            found = self.try_look_for_word_with_orientation(
                                word, cell, orientation, inverted
                            )

                            if found is not None:
                                return PuzzleWord(
                                    orientation,
                                    inverted,
                                    (row_index, letter_index),
                                    found,
                                )

    def try_look_for_word_with_orientation(
        self,
        word: str,
        start: Tuple[int, int],
        orientation: Orientation,
        inverted: bool,
    ):
        # because of 1-letter "words", so position is not unbound
        position = start

        # skip the first letter because we already know it's in the puzzle
        for (index, position) in islice(
            generate_cells_for_word(start, orientation, inverted, word), 1
        ):
            if not self.puzzle.in_bounds(position):
                return None

            if self.puzzle[position] != word[index]:
                return None

        return position


class PuzzleWordsLookupWithCache(PuzzleWordsLookup):
    def __init__(self, words: List[str], puzzle: Puzzle):
        super().__init__(words, puzzle)
        self.first_letters_locations: Dict[str, List[Cell]] = DefaultDict(list)

    def resolve(self):
        for row_index in range(self.puzzle.rows):
            for letter_index in range(self.puzzle.columns):
                cell = (row_index, letter_index)
                self.first_letters_locations[puzzle[cell]].append(cell)

        words_in_puzzle = {word: self.look_for_word(word) for word in self.words}
        return words_in_puzzle

    def look_for_word(self, word: str):
        for cell in self.first_letters_locations[word[0]]:
            for orientation in Orientation:
                for inverted in [True, False]:
                    found = self.try_look_for_word_with_orientation(
                        word, cell, orientation, inverted
                    )

                    if found is not None:
                        return PuzzleWord(
                            orientation,
                            inverted,
                            cell,
                            found,
                        )


if __name__ == "__main__":
    sys.argv = ["", "search_tests/2cheias.txt"]
    puzzle = puzzle_from_file(sys.argv[1])
    words = words_from_file(sys.argv[1])
    words_list = "\n".join([word for word in words])
    print(words_list)
    print(puzzle)
    print(PuzzleWordsLookupWithCache(words, puzzle).resolve())
