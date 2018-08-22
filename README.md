# Perfect Game Player
> Predicts best move in board games using minimax algorithm.


It will generate next moves to board positions. Minimax tree algorithm is used to choose the best move at each turn. It can be used as a library for your board game needs.
Currently tested on tic tac toe game . A connect 4 implementation is given too.


## Installation


## Usage example
To use minimax, import and just pass in the board.

`ret = minimax_tree.minimax(start_board,true)`

It returns a tuple containing the best next board position and the position value.

`print(ret[0])`
 `print(ret[1])`
 
 To make use of minimax on a game, your code needs to subclass `Node` and implement its functions.
 




## TODO
* Add different games to run on i.e. Gomoku, Nim
* Method to visualise algorithm on XO
* Interactive Human v Bot game.
* Or any other ideas of your own.


## Meta

Devesh – [@WhoSawDevesh](https://twitter.com/WhoSawDevesh) – devesh47cool@gmail.com

Distributed under the GNU GPL v3.0 license. See ``LICENSE`` for more information.

[https://github.com/dsaw/perfect-game-player](https://github.com/dsaw/perfect-game-player)
