import copy
import minimax_tree


# Runs minimax on Connect 4 game


def win_for_player(board,player_token):
    """
    Four in a row, column or a diagonal
    :param board:
    :param player_token: 'r' / 'y'
    :return:
    """

    for r in range(6):
        for c in range(7):
            if board[r][c] == player_token and r <= 2:
                if board[r + 1][c] == board[r + 2][c] == board[r + 3][c] == player_token:
                    # vertical
                    return True

            if board[r][c] == player_token and c <= 3:
                if board[r][c + 1] == board[r][c + 2] == board[r][c + 3] == player_token:
                    # horizontal
                    return True

            if board[r][c] == player_token and c <= 3 and r <= 2:
                if board[r + 1][c + 1] == board[r + 2][c + 2] == board[r + 3][c + 3] == player_token:
                    # down diagonal
                    return True

            if board[r][c] == player_token and c <= 3 and r >= 3:
                if board[r -1][c + 1] == board[r - 2][c + 2] == board[r - 3][c + 3] == player_token:
                    # up diagonal
                    return True


    return False


class Connect4Node(minimax_tree.Node):
    '''
        :param board: 3x3 character array with 'x','o' and '.'
    '''


    heuristic = None

    def __init__(self,board):
        self.state = board
        self.player = True
        self.value = None
        self.best_move = None



    def if_leaf(self):
        if win_for_player(self.state,'r') or win_for_player(self.state,'y'):
            return True

        if any('.' in row for row in self.state):
            return False

        return True


    def generate_moves(self,player):
        '''
        Generate possible moves for next player
        :return:
        '''

        curboard = copy.copy(self.state)

        next_state = []
        player = 'y' if player else 'r'

        for c in range(7):
            for r in range(6):
                if self.state[r][c] !=  '.':
                    newnode = Connect4Node(copy.deepcopy(self.state))
                    newnode.state[r][c] = player  # not following encapsulation
                    next_state.append(newnode)
        return next_state


    def evaluate(self):
        ''' Set value of board. If its not a win, loss or a draw then heuristic is evaluated.

        '''
        if win_for_player(self.state, 'x'):
            self.value = minimax_tree.PINF
        elif win_for_player(self.state,'o'):
            self.value = minimax_tree.NINF
        elif not any('.' in row for row in self.state):
            self.value = 0
        else:
            self.value = Connect4Node.heuristic(self.state,self.player)

        # Connect 4 heuristic
        return self.value

