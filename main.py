import sys

from generate import PuzzleGeneratorConfigConstructor, PuzzleConstructorFromConfig
from search import PuzzleWordsLookup

config = PuzzleGeneratorConfigConstructor.from_file(sys.argv[1])
puzzle = PuzzleConstructorFromConfig.construct_from_config(config)
assert puzzle, \
    f"Failed to create a puzzle with " \
    f"{config.rows} * {config.columns}, words: {config.words}, orientations: {config.orientations}"
words_list = '\n'.join([word for word in config.words])
print(words_list)
print(puzzle)
print(PuzzleWordsLookup(config.words, puzzle).resolve())
