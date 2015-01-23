#
# Implement an algorithm to delete a node in the middle of a singly linked
# list, given access only to that node.
#
# EXAMPLE:
# Input: the node c from the linked list a->b->c->d->e
# Result: nothing is returned, but the new linked list looks like a->b->d->e
#


def delete_middle(node):
    if node.next_ is None:
        raise ValueError("node is at the end of the list")
    node.payload = node.next_.payload
    node.next_ = node.next_.next_
