import minimax_tree

# Making use of minimax tree algorithm to solve board states of Tic Tac Toe

def win_for_player(board,player_token):

    for r in range(3):
        if board[r][0]==player_token and board[r][1]==player_token and board[r][2]==player_token:
            return True
        if board[0][r] == player_token and board[1][r] == player_token and board[2][r] == player_token:
            return True

    # checking diagonal
    if board[0][0] == player_token and board[1][1] == player_token and board[2][2] == player_token:
        return True
    if board[0][2] == player_token and board[1][1] == player_token and board[2][0] == player_token:
        return True

    return False


class TicTacToeNode(minimax_tree.Node):
    '''
    Specialized class of Node.
    It represents one board position with the heuristic value for the given players move
    '''

    def __init__(self,board):
        '''

        :param board: 3x3 character array with 'x','o' and '.'
        '''
        self.state = board
        self.player = True
        self.value = None

    def if_leaf(self):

        if win_for_player(self.board,'x') or win_for_player(self.board,'o'):
            return True

        if any('.' in row for row in self.board):
            return False

        return True

