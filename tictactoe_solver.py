import minimax_tree
import copy

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
        '''
        checks if node is either a win, loss or draw.
        :return: boolean
        '''

        if win_for_player(self.state,'x') or win_for_player(self.state,'o'):
            return True

        if any('.' in row for row in self.state):
            return False

        return True


    def generate_moves(self):
        '''
        Generates list of valid possible moves
        :return: list
        '''
        curboard = copy.copy(self.state)

        next_state = []
        if self.player:
            for r in range(3):
                for c in range(3):
                    if curboard[r][c] == '.':
                        newnode = TicTacToeNode(copy.copy(self.state))
                        newnode.state[r][c] = 'x'         # not following encapsulation
                        next_state.append(newnode)
        else:
            for r in range(3):
                for c in range(3):
                    if curboard[r][c] == '.':
                        newnode = TicTacToeNode(copy.copy(self.state))
                        newnode.state[r][c] = 'o'         # not following encapsulation
                        next_state.append(newnode)
        return next_state

