import unittest
from connect4_solver import *

class TestConnect4(unittest.TestCase):

    def setUp(self):
        board = [['r', 'y', 'r', 'y', 'r', 'y', 'r'],
                 ['y', 'r', 'y', 'r', 'y', 'r', 'y'],
                 ['r', 'y', 'r', 'y', 'r', 'y', 'r'],
                 ['y', 'r', 'y', 'r', 'y', 'r', 'y'],
                 ['r', 'y', 'r', 'y', 'r', 'y', 'r'],
                 ['y', 'r', 'y', 'r', 'y', 'r', 'y']
                 ]

        self.node = Connect4Node(board)


    def test_if_endgame_is_win(self):
        board = [['.','.','.','.','.','.','.'],
                 ['.','.','.','.','.','.','.'],
                 ['.','.','.','y','.','.','y'],
                 ['.','.','.','r','r','r','r'],
                 ['y','.','y','y','y','r','r'],
                 ['y','.','r','y','r','y','r']
                 ]

        self.assertEqual(win_for_player(board,'r'), True)


    def test_if_endgame_is_draw(self):


        self.assertEqual(self.node.if_leaf(), True)


    def test_count_tokens_row(self):

        count_twos_yellow = count_two_in_row(self.node.state,'y')
        count_twos_red = count_two_in_row(self.node.state,'r')

        self.assertEqual(count_twos_red,count_twos_yellow)


if __name__ == '__main__':
    unittest.main()
