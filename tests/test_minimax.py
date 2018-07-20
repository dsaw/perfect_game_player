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

    def test_node_representation(self):
        '''
        '''

        self.node.state = [['o','x'],['x','x']]
        self.assertEqual(str(self.node),'o|x\nx|x\n')

if __name__ == '__main__':
    unittest.main(verbosity=2)
