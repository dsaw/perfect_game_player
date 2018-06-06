
import logging



# Straightforward minimax tree algorithm

PINF  = 100
NINF = -100



class Node:
    ''' Node of minimax tree associated with a board state and player'''

    def __init__(self):
        self.state = None
        self.value = None
        self.player = True

    def if_leaf(self):
        return True

    def generate_moves(self):
        return []

    def evaluate(self):
        return self.value



def minimax(node,player):
    '''
    Main minimax function that calculates the
    :return:
    '''
    if node.if_leaf():
        return node.evaluate()

    if player:
        maxv = NINF
        for child in node.generate_moves():
            child.value = minimax(child,not player)
            if child.value > maxv:
                maxv = child.value
        node.value = maxv

    else:
        minv = PINF
        for child in node.generate_moves():
            child.value = minimax(child,not player)
            if child.value < minv:
                minv = child.value
        node.value = minv