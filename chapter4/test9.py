from __future__ import print_function

import unittest

import tree
import problem9
import mock
import test6


class TestPath(unittest.TestCase):

    def setUp(self):
        sub = tree.Node(1)
        sub.left = tree.Node(5)
        sub.left.left = tree.Node(3)
        sub.left.left.left = tree.Node(8)
        sub.left.left.right = tree.Node(7)
        sub.left.right = tree.Node(-2)
        sub.left.right.left = tree.Node(2)
        sub.left.right.right = tree.Node(6)

        self.tree = tree.Tree()
        self.tree.root = tree.Node(-3)
        self.tree.root.left = tree.Node(4)
        self.tree.root.left.left = tree.Node(0)
        self.tree.root.left.right = sub
        self.tree.root.right = tree.Node(8)

        test6.add_parent_pointers(self.tree)

    #
    # http://stackoverflow.com/questions/12998908/is-it-possible-to-mock-pythons-built-in-print-function
    #
    @mock.patch("__builtin__.print")
    def test_path(self, mock_print):
        problem9.path(self.tree, 5)
        mock_print.assert_any_call([-3, 8])
        mock_print.assert_any_call([-3, 4, 1, 5, -2])
        mock_print.assert_any_call([5, -2, 2])
        mock_print.assert_any_call([5])
