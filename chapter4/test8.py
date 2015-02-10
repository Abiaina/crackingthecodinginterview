import unittest
import random
import sys
import copy
import nose.tools

import tree
import problem8


def random_int():
    return int(random.random() * sys.maxint)


def random_str():
    return "%08d" % (random_int() % 0xffffffff)


def create_random_tree(max_depth, value_fn):
    root = tree.Node(0)
    stack = [(0, root)]
    while stack:
        depth, node = stack.pop()
        if depth == max_depth:
            continue
        node.left = tree.Node(value_fn())
        node.right = tree.Node(value_fn())

        if 0.0 <= random.random() < 0.05:
            continue
        elif 0.05 <= random.random() < 0.10:
            stack.append((depth + 1, node.left))
        elif 0.10 <= random.random() < 0.15:
            stack.append((depth + 1, node.right))
        else:
            stack.append((depth + 1, node.right))
            stack.append((depth + 1, node.left))

    t = tree.Tree()
    t.root = root
    return t


def random_node(t, max_depth):
    depth = int(random.random() * max_depth)
    node = t.root
    while depth:
        next_node = node.left if random.random() < 0.5 else node.right
        if next_node:
            depth -= 1
            node = next_node
        else:
            break
    return node


class TestIsSubtree(unittest.TestCase):

    HUGE_HEIGHT = 24
    TINY_HEIGHT = 10

    def test_easy(self):
        huge = create_random_tree(TestIsSubtree.HUGE_HEIGHT / 2, random_int)
        tiny = create_random_tree(TestIsSubtree.TINY_HEIGHT / 2, random_str)
        tiny_copy = copy.deepcopy(tiny)

        self.assertFalse(problem8.is_subtree(huge, tiny))

        random_node(huge, TestIsSubtree.HUGE_HEIGHT / 2).left = tiny_copy.root

        self.assertTrue(problem8.is_subtree(huge, tiny))

    #
    # I've disabled this test because it takes too long (around half a minute,
    # with the majority of the time spent creating the huge tree).
    #
    @nose.tools.nottest
    def test_hard(self):
        huge = create_random_tree(TestIsSubtree.HUGE_HEIGHT, random_int)
        tiny = create_random_tree(TestIsSubtree.TINY_HEIGHT, random_str)
        tiny_copy = copy.deepcopy(tiny)

        self.assertFalse(problem8.is_subtree(huge, tiny))

        random_node(huge, TestIsSubtree.HUGE_HEIGHT).left = tiny_copy.root

        self.assertTrue(problem8.is_subtree(huge, tiny))
