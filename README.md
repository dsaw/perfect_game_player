# Perfect Game Player
> Predicts best move in board games using minimax algorithm.

 [![Build Status](https://travis-ci.org/dsaw/perfect_game_player.svg?branch=master)](https://travis-ci.org/dsaw/perfect_game_player)

It will generate the best next move to the  given board position. Minimax tree algorithm is used to choose the best move at each turn. It can be used as a library for your board game needs. You just have to create a new file for that game and subclass the main classes. 

## Analysis
I have tested this on tic tac toe game, which is simple enough for brute force minimax. A Connect 4 implementation is given too.

Function  |  Time
--------  |  ----
Brute Force Minimax | 1m 2s 
Depth Limited Minimax | 1s 750ms
Alpha Beta pruning | 24s 937ms

Of course, the variants give approximate solutions. Two heuristics were tried out but I ended up sticking to the one which scored positions of the grid.


## Installation

Clone the git repo.

```
git clone https://github.com/dsaw/perfect-game-player.git
```
Go to the directory and install it the standard way

```
python setup.py install
```

Or installing locally is fine (needs pip)
```
pip install .
```

## Usage example
The minimax tree can be used for testing and learning purposes. 
It is abstract in itself, so to use it in a game a separate solver needs to be written.
Currently, we have `connect4` and `tictactoe` as wrappers for this.
```
from pgameplayer.minimax_tree import *
from pgameplayer.solvers import *

start_board = tictactoe.TicTacToeNode([['.','.','.'],['.','.','.'],['.','.','.']])

ret = minimax(start_board,True)  # True if first player moves
```

The above is the brute force minimax. 
There is a depth limited version which takes the depth till which the best move will be calculated
```
ret = depth_limited_minimax(start_board,3,True)  # depth is 3
```
Another version is alpha beta pruning where unnecessary branches whose 
win' value is outside the range are pruned.

```
ret = alpha_beta_pruning_minimax(start_board,NINF,PINF,True)  # alpha is negative infinity & beta is positive infinity
```

The minimax functions returns a tuple containing the best next board position and the position value.

```
print(ret[0])  # [['.','.','.'],['.','x','.'],['.','.','.']]
print(ret[1])  # Tic tac toe is a draw given perfect play
```
 
 To make use of minimax on a game, your code needs to subclass `Node` and implement its functions.
 Take a look at the [code](https://github.com/dsaw/perfect-game-player/blob/master/tictactoe_solver.py) for details.

## Testing
Unit tests can be run with
```python setup.py test```

## TODO
* Add different games to run on i.e. Gomoku, Nim
* Method to visualise algorithm on XO
* Interactive Human v Bot game.
* Or any other ideas of your own.


## Meta

Devesh – [@WhoSawDevesh](https://twitter.com/WhoSawDevesh) – devesh47cool@gmail.com

Distributed under the GNU GPL v3.0 license. See ``LICENSE`` for more information.

[https://github.com/dsaw/perfect-game-player](https://github.com/dsaw/perfect-game-player)


<!-- image links -->

[travis-image]: https://travis-ci.org/dsaw/perfect-game-player.svg?branch=master
[travis-url]: https://travis-ci.org/dsaw/perfect-game-player#
