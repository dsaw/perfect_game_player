import logging

logger = logging.getLogger("minimax")
# Straightforward minimax tree algorithm

PINF = 100
NINF = -100


class Node:
    ''' Node of minimax tree associated with a board state and player'''

    def __init__(self):
        self.state = None
        self.value = None
        self.player = True
        self.best_move = None

    def if_leaf(self):
        return True

    def generate_moves(self):
        return []

    def evaluate(self):
        return self.value

    def __str__(self):
        str = ''
        for r in range(len(self.state)):
            str += '|'.join(self.state[r]) + '\n'
        return str


def minimax(node, player):
    '''
    Main minimax function that obtains the best move to take
    :return:
    '''

    if node.if_leaf():
        return ([], node.evaluate())

    if player:
        maxv = NINF
        possible_moves = node.generate_moves(player)
        for child in possible_moves:
            (_, child.value) = minimax(child, not player)
            if child.value > maxv:
                maxv = child.value
                node.best_move = child.state

        node.value = maxv
        logger.debug("{} == {}".format(node.state, node.value))

        return (node.best_move, maxv)

    else:
        minv = PINF
        possible_moves = node.generate_moves(player)
        for child in possible_moves:
            (_, child.value) = minimax(child, not player)
            if child.value < minv:
                minv = child.value
                node.best_move = child.state
        node.value = minv
        logger.debug("{} == {}".format(node.state, node.value))

        return (node.best_move, minv)


# TODO: refactor to return next move too
def depth_limited_minimax(node, depth, player):
    '''
    Minimax algorithm that returns after a particular depth is reached
    :param node:
    :param depth:
    :param player:
    :return:
    '''
    if node.if_leaf() or depth == 0:
        return node.evaluate()

    if player:
        maxv = NINF
        possible_moves = node.generate_moves(player)
        for child in possible_moves:
            child.value = depth_limited_minimax(child, depth - 1, not player)
            if child.value > maxv:
                maxv = child.value
                node.best_move = child.state

        node.value = maxv
        logger.debug("{} == {}".format(node, node.value))
        return maxv

    else:
        minv = PINF
        possible_moves = node.generate_moves(player)
        for child in possible_moves:
            child.value = depth_limited_minimax(child, depth - 1, not player)
            if child.value < minv:
                minv = child.value
                node.best_move = child.state

        node.value = minv
        logger.debug("{} == {}".format(node, node.value))
        return minv


# alpha beta pruning takes a while

def alpha_beta_pruning_minimax(node, player, alpha, beta):
    '''
    Minimax variant that maintains max and min value for every node and prunes branches that are unnecessary
    '''

    if node.if_leaf():
        return node.evaluate()

    if player:
        possible_moves = node.generate_moves(player)
        for child in possible_moves:
            child.value = alpha_beta_pruning_minimax(child, not player, alpha, beta)
            if child.value > alpha:
                alpha = child.value
                node.best_move = child.state
            if alpha > beta:
                break

        node.value = alpha
        logger.debug(" {} == {}".format(node, node.value))
        return alpha

    else:
        possible_moves = node.generate_moves(player)
        for child in possible_moves:
            child.value = alpha_beta_pruning_minimax(child, not player, alpha, beta)
            if child.value < beta:
                beta = child.value
                node.best_move = child.state
            if alpha > beta:
                break
        node.value = beta
        logger.debug(" {} == {}".format(node, node.value))
        return beta
