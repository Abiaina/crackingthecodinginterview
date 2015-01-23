#
# Write code to partition a linked list around a value x, such that all nodes
# less than x come before all nodes greater than or equal to x.
#
from sll import SinglyLinkedList


def partition(sll, x):
    lt = SinglyLinkedList()
    geq = SinglyLinkedList()
    for value in sll:
        if value < x:
            lt.append(value)
        else:
            geq.append(value)
    return lt + geq
