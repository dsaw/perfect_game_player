import unittest

import minimax_tree

class TestMinimaxDS(unittest.TestCase):

    def setUp(self):
        self.node = minimax_tree.Node()

    def tearDown(self):
        pass

    def test_eval_node(self):
        '''

        :return:
        '''
        self.assertIsNone(self.node.evaluate())



if __name__ == '__main__':
    unittest.main(verbosity=2)
    