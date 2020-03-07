from typing import List, Tuple, Optional
from enum import Enum

from puzzle import Puzzle


def words_looking_for(path: str) -> List[str]:
    with open(path, 'r') as file:
        number_of_lines = int(file.readline())
        words = []
        for i in range(number_of_lines):
            words.append(file.readline().rstrip().upper())
        return words


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


class PuzzleWord:
    def __init__(self, word: str, orientation: Orientation, is_inverted: bool, start: Tuple[int, int], end: Tuple[int, int]):
        self.word = word
        self.is_inverted = is_inverted
        self.end = end
        self.start = start
        self.orientation = orientation

    def __str__(self):
        inverted = "(Inverted)" if self.is_inverted else ""
        return f"{self.word} {self.start} -[{self.orientation}{inverted}]-> {self.end}"

    def __repr__(self):
        return str(self)


class PuzzleWordsLookup:
    def __init__(self, words: List[str], puzzle: Puzzle):
        self.words = words
        self.puzzle = puzzle

    def resolve(self) -> List[PuzzleWord]:
        words_in_puzzle = []
        for word in self.words:
            words_in_puzzle.append(self.look_for_word(word))
        return words_in_puzzle

    def look_for_word(self, word: str) -> Optional[PuzzleWord]:
        for row_index in range(len(self.puzzle.rows)):
            for letter_index in range(len(self.puzzle.rows[row_index])):
                if self.puzzle.get(row_index, letter_index) == word[0]:
                    for orientation in Orientation:
                        # look in the "normal way": for example:
                        # looking in Horizontal in the "normal" way means
                        # we look -->
                        found = self.look_for_word_with_orientation(word, (row_index, letter_index), orientation, False)
                        if found is not None:
                            return PuzzleWord(word, orientation, False, (row_index, letter_index), found)

                        # look in the "inverted way"
                        # while in the "inverted way"
                        # we look <--
                        found = self.look_for_word_with_orientation(word, (row_index, letter_index), orientation, True)
                        if found is not None:
                            return PuzzleWord(word, orientation, True, (row_index, letter_index), found)

        # fuck
        print(f"Could not find '{word}'")
        return None

    def look_for_word_with_orientation(self, word: str, start: Tuple[int, int], orientation: Orientation,
                                       inverted: bool) -> Optional[Tuple[int, int]]:
        change_vector = orientation.get_vector()
        if inverted:
            change_vector = -change_vector[0], -change_vector[1]

        current_index = 1
        current_position = 0, 0

        # print("\n\n")
        # print("start", start, "word", word, "orientation", orientation, "inverted", inverted)
        # print("\n\n")

        while current_index < len(word):
            current_position = start[0] + current_index * change_vector[0], start[1] + current_index * change_vector[1]

            if not self.puzzle.in_bounds(current_position[0], current_position[1]):
                return None

            car = self.puzzle.get(current_position[0], current_position[1])
            # print(current_position, "character", car, "index", current_index, "word[index]", word[current_index])

            if car != word[current_index]:
                return None

            current_index += 1

        return current_position
