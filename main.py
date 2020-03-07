from puzzle import PuzzleConstructor
from search import PuzzleWordsLookup, words_looking_for

nome = '2tempo.txt'  # input('nome do ficheiro(com extensão)')
puzzle = PuzzleConstructor.construct(nome)
print(PuzzleWordsLookup(words_looking_for(nome), puzzle).resolve())
