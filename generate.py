import random
import string
import sys
from typing import List, Optional, Dict, Tuple

from puzzle import Puzzle
from orientation import Orientation, inverted_orientation_vector

from dataclasses import dataclass


@dataclass
class PuzzleGeneratorConfig:
    rows: int
    columns: int
    words: List[str]
    orientations: List[Orientation]


class PuzzleGeneratorConfigConstructor:
    @staticmethod
    def from_file(path: str) -> PuzzleGeneratorConfig:
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
    @staticmethod
    def construct_from_config(config: PuzzleGeneratorConfig) -> Optional[Puzzle]:
        rows: List[List[str]] = []
        for i in range(config.rows):
            row = []
            for j in range(config.columns):
                row.append(" ")
            rows.append(row)
        puzzle_with_words = PuzzleConstructorFromConfig._construct_from_config_helper(
            config, Puzzle(rows), 0
        )
        # We were unable to fit all the words there
        if puzzle_with_words is None:
            return puzzle_with_words

        for i in range(len(puzzle_with_words.rows)):
            for j in range(config.columns):
                if puzzle_with_words[(i, j)] == " ":
                    puzzle_with_words[i, j] = random.choice(string.ascii_uppercase)

        return puzzle_with_words

    @staticmethod
    def _construct_from_config_helper(
        config: PuzzleGeneratorConfig, puzzle: Puzzle, index: int
    ) -> Optional[Puzzle]:
        # base case; we've added all the words we wanted to, yay!
        if index == len(config.words):
            return puzzle

        word = config.words[index]
        # print("Adding", word)
        possible_for_this_word = (
            PuzzleConstructorFromConfig._possible_points_with_orientation(
                word, puzzle, config
            )
        )
        while len(possible_for_this_word) > 0:

            random_start_position = random.choice(list(possible_for_this_word.keys()))
            orientations_and_inverted = possible_for_this_word.get(
                random_start_position
            )
            del possible_for_this_word[random_start_position]

            for orientation, inverted in orientations_and_inverted:
                new_puzzle = PuzzleConstructorFromConfig._add_word(
                    word, puzzle, random_start_position, orientation, inverted
                )

                # print("Added", word, "Puzzle\n", new_puzzle)

                final_puzzle = (
                    PuzzleConstructorFromConfig._construct_from_config_helper(
                        config, new_puzzle, index + 1
                    )
                )
                # print("End", word, "Puzzle\n", final_puzzle)

                if final_puzzle is not None:
                    return final_puzzle

        # There's nowhere to place this :( We have failed.
        return None

    @staticmethod
    def _possible_points_with_orientation(
        word: str, puzzle: Puzzle, config: PuzzleGeneratorConfig
    ) -> Dict[Tuple[int, int], List[Tuple[Orientation, bool]]]:
        start_points = {}
        for row_index in range(len(puzzle.rows)):
            for letter_index in range(len(puzzle.rows[row_index])):
                # Sample here gets a random order of the list
                for orientation in random.sample(
                    config.orientations, len(config.orientations)
                ):
                    # Sample here gets a random order of the list
                    inverted_list = random.sample([True, False], 2)
                    for inverted in inverted_list:
                        if PuzzleConstructorFromConfig._possible_with_location_and_orientation(
                            word,
                            puzzle,
                            (row_index, letter_index),
                            orientation,
                            inverted,
                        ):
                            start_points.setdefault(
                                (row_index, letter_index), []
                            ).append((orientation, inverted))

        return start_points

    @staticmethod
    def _possible_with_location_and_orientation(
        word: str,
        puzzle: Puzzle,
        location: Tuple[int, int],
        orientation: Orientation,
        inverted: bool,
    ) -> bool:

        change_vector = (
            inverted_orientation_vector(orientation) if inverted else orientation.value
        )

        for i in range(len(word)):
            current_location = (
                location[0] + i * change_vector[0],
                location[1] + i * change_vector[1],
            )
            if not puzzle.in_bounds(current_location):
                return False
            if puzzle[current_location] != " " and puzzle[current_location] != word[i]:
                return False

        return True

    @staticmethod
    def _add_word(
        word: str,
        puzzle: Puzzle,
        location: Tuple[int, int],
        orientation: Orientation,
        inverted: bool,
    ) -> Puzzle:

        change_vector = (
            inverted_orientation_vector(orientation) if inverted else orientation.value
        )
        new_puzzle = puzzle.__copy__()

        for i in range(len(word)):
            current_location = (
                location[0] + i * change_vector[0],
                location[1] + i * change_vector[1],
            )
            puzzle[current_location] = word[i]

        return new_puzzle


if __name__ == "__main__":
    config = PuzzleGeneratorConfigConstructor.from_file(sys.argv[1])
    puzzle = PuzzleConstructorFromConfig.construct_from_config(config)
    assert puzzle, (
        f"Failed to create a puzzle with "
        f"{config.rows} * {config.columns}, words: {config.words}, orientations: {config.orientations}"
    )
    words_list = "\n".join([word for word in config.words])
    print(words_list)
    print(puzzle)
