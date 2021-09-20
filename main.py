import sys

from generate import puzzle_generator_config_from_file, PuzzleConstructorFromConfig
from search import PuzzleWordsLookup

config = puzzle_generator_config_from_file(sys.argv[1])
puzzle = PuzzleConstructorFromConfig(config).try_construct()
assert puzzle, (
    f"Failed to create a puzzle with "
    f"{config.rows} * {config.columns}, words: {config.words}, orientations: {config.orientations}"
)
words_list = "\n".join([word for word in config.words])

print(words_list)
print(puzzle)
print(PuzzleWordsLookup(config.words, puzzle).resolve())
