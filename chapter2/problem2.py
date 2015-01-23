#
# Implement an algorithm to find the kth to last element of a linked list
#


def kth_to_last(sll, k):
    if k <= 0:
        raise ValueError("k must be positive")

    first = second = sll.head
    for _ in xrange(k - 1):
        if first is None:
            raise ValueError("list is too short")
        first = first.next_

    if first is None:
        raise ValueError("list is too short")

    while first.next_ is not None:
        first = first.next_
        second = second.next_
    return second.payload
