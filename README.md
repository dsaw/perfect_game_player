# Perfect Game Player
> Predicts best move in board games using minimax algorithm.


It will generate the best next move to the  given board position. Minimax tree algorithm is used to choose the best move at each turn. It can be used as a library for your board game needs. You just have to create a new file for that game and subclass the main classes. 

## Analysis
I have tested this on tic tac toe game, which was simple enough for brute force minimax. A connect 4 implementation is given too.

Function  |  Time
--------  |  ----
Brute Force Minimax | 1m 2s 
Depth Limited Minimax | 1s 750ms
Alpha Beta pruning | 24s 937ms

Of course, the variants give approximate solutions. Two heuristics were tried out but I ended up sticking to the one which scored positions of the grid.


## Installation


## Usage example
To use minimax, import and just pass in the board.
```
from minimax_tree import *
start_board = [['.','.','.'],['.','.','.'],['.','.','.']]
ret = minimax(start_board,true)  # true for first player
```

This is the brute force minimax. There is a depth limited version and alpha beta pruning one too.

```
ret = depth_limited_minimax(start_board,3,true)  # depth is 3
ret = alpha_beta_pruning_minimax(start_board,NINF,PINF,true)  # alpha is negative infinity & beta is positive infinity
```

The brute force minimax returns a tuple containing the best next board position and the position value.

```
print(ret[0])  # [['.','.','.'],['.','x','.'],['.','.','.']]
print(ret[1])  # Tic tac toe is a draw given perfect play
```
 
 To make use of minimax on a game, your code needs to subclass `Node` and implement its functions.
 Take a look at the [code](https://github.com/dsaw/perfect-game-player/blob/master/tictactoe_solver.py) for details.




## TODO
* Add different games to run on i.e. Gomoku, Nim
* Method to visualise algorithm on XO
* Interactive Human v Bot game.
* Or any other ideas of your own.


## Meta

Devesh – [@WhoSawDevesh](https://twitter.com/WhoSawDevesh) – devesh47cool@gmail.com

Distributed under the GNU GPL v3.0 license. See ``LICENSE`` for more information.

[https://github.com/dsaw/perfect-game-player](https://github.com/dsaw/perfect-game-player)
