import unittest

from problem4 import slice_tree
from tree import complete_tree


def extract_node_values(slices):
    """Each slice returned by slice_tree is a list of TreeNode objects.
    Convert that to a list of values stored within each TreeNode
    (simplifies testing)."""
    for slice_ in slices:
        for i, s in enumerate(slice_):
            slice_[i] = s.value
    return slices


class TestSliceTree(unittest.TestCase):

    def setUp(self):
        self.tree = complete_tree(4)

    def test_complete(self):
        slices = extract_node_values(slice_tree(self.tree))
        self.assertEquals(len(slices), 4)
        self.assertEquals(slices[0], [0])
        self.assertEquals(slices[1], [1, 2])
        self.assertEquals(slices[2], [3, 4, 5, 6])
        self.assertEquals(slices[3], [7, 8, 9, 10, 11, 12, 13, 14])

    def test_incomplete(self):
        self.tree.root.right.left = None
        self.tree.root.right.right = None
        slices = extract_node_values(slice_tree(self.tree))
        self.assertEquals(len(slices), 4)
        self.assertEquals(slices[0], [0])
        self.assertEquals(slices[1], [1, 2])
        self.assertEquals(slices[2], [3, 4])
        self.assertEquals(slices[3], [7, 8, 9, 10])
