import unittest
import logging
import logging.config
import time
import minimax_tree
import tictactoe_solver


class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        root_board = [['.'] * 3 for _ in range(3)]
        self.node = tictactoe_solver.TicTacToeNode(root_board)
        logging.basicConfig(filename="tictac.log", level=logging.DEBUG)

    def tearDown(self):
        pass

    def test_next_moves(self):
        '''
        Tests if 9 boards are generated for root board
        :return:
        '''
        moves_lst = self.node.generate_moves(True)
        self.assertEqual(moves_lst[0].state[0][0], 'x')
        self.assertEqual(moves_lst[4].state[1][1], 'x')
        self.assertEqual(len(moves_lst), 9)

    def test_minimax(self):
        '''
        Tests minimax algo on root board of xo
        It will output time elapsed.
        :return:
        '''
        start = time.time()

        val = minimax_tree.minimax(self.node, True)

        end = time.time()
        print('Time elapsed : {}'.format(end - start))
        self.assertEqual(val, 0)
        print(val)


    def test_compute_heuristic(self):
        '''
        Tests if the heuristic returns appropriate value
        :return:
        '''
        board1 = [['o','x',' .'],['x','o','x'],['.','.','.']]
        board2 = [['x','.',' .'],['.','o','o'],['x','.','x']]

        self.assertAlmostEqual(tictactoe_solver.compute_heuristic(board1,True),-16)
        self.assertAlmostEqual(tictactoe_solver.compute_heuristic(board2,True),16)


    def test_minimax_depth_limited(self):
        '''
        Tests depth limited minimax algorithm
        :return:
        '''
        start = time.time()

        val = minimax_tree.depth_limited_minimax(self.node, 3, True)

        end = time.time()
        logging.info('Minimax depth {} \tTime elapsed: {}'.format(3, end - start))
        self.assertEqual(val, 0)
        print(val)

    def test_evaluate(self):
        '''
        Test if node value is None as it is not leaf
        '''

        self.assertIsNone(self.node.evaluate())


if __name__ == '__main__':
    unittest.main(verbosity=2)
