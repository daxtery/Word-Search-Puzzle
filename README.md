# Word Search Puzzle

`python generate.py generate_tests\entrada1.txt`

```
OLA
ADEUS
TESTE
SOL
LUA
MESA
CADEIRA
MOCHILA
N K F D G E L Q
M E S A H M O G
T E S T E O S A
Z R T L W C Q D
R W U R O H W E
Y A Z L D I N U
O C A D E L A S
A R I E D A C P
```

`python search.py search_tests\2cheias.txt`

```
{'AFOGAMENTO': None,
 'AGUA': [(1, 0),(2, 0),(3, 0),(4, 0)] (Horizontal),
 'BOMBEIROS': None,
 'CHEIAS': None,
 'CHUVA': [(5, 3),(6, 3),(7, 3),(8, 3),(9, 3)] (Horizontal),
 'NADAR': None,
 'PERIGO': [(0, 5),(0, 4),(0, 3),(0, 2),(0, 1),(0, 0)] (Inverted Vertical),
 'PREVENCAO': None,
 'RIOS': [(6, 5),(5, 4),(4, 3),(3, 2)] (Inverted Diagonal),
 'RISCO': [(4, 9),(5, 9),(6, 9),(7, 9),(8, 9)] (Horizontal),
 'SALVAMENTO': [(8, 0),(8, 1),(8, 2),(8, 3),(8, 4),(8, 5),(8, 6),(8, 7),(8, 8),(8, 9)] (Vertical),
 'TEMPESTADE': None}
```