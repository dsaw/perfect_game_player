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
                        # down
                    return True

            if board[r][c] == player_token and c <= 3:
                if board[r + 1][c] == board[r + 2][c] == board[r + 3][c] == player_token:
                    # horizontal
                    return True

            if board[r][c] == player_token and c <= 3 and r <= 2:
                if board[r + 1][c + 1] == board[r + 2][c + 2] == board[r + 3][c + 3] == player_token:
                    # down diagonal
                    return True

            if board[r][c] == player_token and c <= 3 and r >= 3:
                if board[r -1][c + 1] == board[r - 2][c + 2] == board[r - 3][c + 3] == player_token:
                    # down diagonal
                    return True


    return False


class Connect4Node(minimax_tree.Node):
    '''
        :param board: 3x3 character array with 'x','o' and '.'
    '''

    def __init__(self,board):
        self.state = board
        self.player = True
        self.value = None
        self.best_move = None

    def if_leaf(self):
        pass