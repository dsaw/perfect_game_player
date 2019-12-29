from pgameplayer import minimax_tree
import copy

# Making use of Minimax tree algorithm to solve board states of Tic Tac Toe


def compute_position_heuristic(board,player_token):
    '''

    :param board:
    :param player_token:
    :return:
    '''

    xo_diff = 0

    if board[0][0]=='x':
        xo_diff+=3
    elif board[0][0]=='o':
        xo_diff-=3

    if board[0][2]=='x':
        xo_diff+=3
    elif board[0][2] == 'o':
        xo_diff-=3

    if board[2][0]=='x':
        xo_diff+=3
    elif board[2][0] == 'o':
        xo_diff-=3

    if board[2][2]=='x':
        xo_diff+=3
    elif board[2][2] == 'o':
        xo_diff-=3

    if board[0][1]=='x':
        xo_diff+=1
    elif board[0][1] == 'o':
        xo_diff-=1

    if board[2][1]=='x':
        xo_diff+=1
    elif board[2][1] == 'o':
        xo_diff-=1

    if board[1][0]=='x':
        xo_diff+=3
    elif board[1][0] == 'o':
        xo_diff-=3

    if board[1][2]=='x':
        xo_diff+=3
    elif board[1][2] == 'o':
        xo_diff-=3

    if board[1][1]=='x':
        xo_diff+=5
    elif board[1][1] == 'o':
        xo_diff-=5

    return xo_diff

def compute_simple_heuristic(board,player_token):
    '''
    A heuristic that computes score of board states which are not leaves.
    :param board: 2d list
    :param player_token: bool
    :return:
    '''

    x_pot_wins = 0
    o_pot_wins = 0

    for r in range(3):
        if board[r][0] == board[r][1] == 'o' and board[r][2]== '.' or board[r][0] == board[r][2] == 'o' and board[r][1]== '.' \
                or board[r][2] == board[r][1] == 'o' and board[r][0]== '.':
            o_pot_wins += 1
    for r in range(3):
        if board[0][r] == board[1][r] == 'o' and board[2][r]== '.' or board[0][r] == board[2][r] == 'o' and board[1][r]== '.' \
                or board[2][r] == board[1][r] == 'o' and board[0][r]== '.':
            o_pot_wins += 1

    for r in range(3):
        if board[r][0] == board[r][1] == 'x' and board[r][2] == '.' or board[r][0] == board[r][2] == 'x' and board[r][
            1] == '.' \
                or board[r][2] == board[r][1] == 'x' and board[r][0] == '.':
            x_pot_wins += 1
    for r in range(3):
        if board[0][r] == board[1][r] == 'x' and board[2][r] == '.' or board[0][r] == board[2][r] == 'x' and board[1][
            r] == '.' \
                or board[2][r] == board[1][r] == 'x' and board[0][r] == '.':
            x_pot_wins += 1
    # diagonal check
    if board[0][0] == board[1][1] == 'x' and board[2][2] == '.' or board[0][0] == board[2][2] == 'x' and board[1][
        1] == '.' \
            or board[2][2] == board[1][1] == 'x' and board[0][0] == '.':
        x_pot_wins += 1

    if board[0][0] == board[1][1] == 'o' and board[2][2] == '.' or board[0][0] == board[2][2] == 'o' and board[1][
        1] == '.' \
            or board[2][2] == board[1][1] == 'o' and board[0][0] == '.':
        o_pot_wins += 1

    if board[0][2] == board[1][1] == 'x' and board[2][1] == '.' or board[0][2] == board[2][1] == 'x' and board[1][
        1] == '.' \
            or board[2][1] == board[1][1] == 'x' and board[0][2] == '.':
        x_pot_wins += 1

    if board[0][2] == board[1][1] == 'o' and board[2][1] == '.' or board[0][2] == board[2][1] == 'o' and board[1][
        1] == '.' \
            or board[2][1] == board[1][1] == 'o' and board[0][2] == '.':
        o_pot_wins += 1


    return (x_pot_wins - o_pot_wins)


def win_for_player(board,player_token):

    for r in range(3):
        if board[r][0]== player_token and board[r][1]== player_token and board[r][2]== player_token:
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

    heuristic = compute_position_heuristic

    def __init__(self,board):
        '''

        :param board: 3x3 character array with 'x','o' and '.'
        '''
        self.state = board
        self.player = True
        self.value = None
        self.best_move = None


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

    def generate_moves(self,player):
        '''
        Generates list of valid possible moves
        :param player: Boolean. x or o
        :return: list
        '''
        curboard = copy.copy(self.state)

        next_state = []
        if player:
            for r in range(3):
                for c in range(3):
                    if curboard[r][c] == '.':
                        newnode = TicTacToeNode(copy.deepcopy(self.state))
                        newnode.state[r][c] = 'x'         # not following encapsulation
                        next_state.append(newnode)
        else:
            for r in range(3):
                for c in range(3):
                    if curboard[r][c] == '.':
                        newnode = TicTacToeNode(copy.deepcopy(self.state))
                        newnode.state[r][c] = 'o'         # not following encapsulation
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
            self.value = TicTacToeNode.heuristic(self.state,self.player)

        # XO heuristic
        return self.value