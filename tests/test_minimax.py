import unittest

from pgameplayer import minimax_tree


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

    def test_should_return_tuple_of_next_move(self):
        '''
        Minimax should return tuple of (move,val)
        :return:
        '''
        self.node.state = [['o','x'],['.','.']]

        return_args = minimax_tree.minimax(self.node, True)

        self.assertIsInstance(return_args,tuple)
        self.assertTupleEqual(return_args,([],None))



if __name__ == '__main__':
    unittest.main(verbosity=2)
