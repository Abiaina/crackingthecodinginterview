#
# Given a circular linked list, implement an algorithm which returns the node
# at the beginning of a loop.
#


def start_of_loop(sll):
    """Simple implementation using a buffer."""
    seen = set()
    curr = sll.head
    while curr:
        if curr in seen:
            return curr
        seen.add(curr)
        curr = curr.next_
    return None


def start_of_loop2(sll):
    """A "clever" implementation that does not use a buffer."""
    #
    # Use Floyd's cycle finding algorithm
    # (http://en.wikipedia.org/wiki/Cycle_detection#Tortoise_and_hare)
    # to determine if we are stuck in a loop.
    #
    tortoise = sll.head
    hare = sll.head.next_
    if hare:
        hare = hare.next_
    while hare and tortoise and hare != tortoise:
        tortoise = tortoise.next_
        hare = hare.next_
        if hare:
            hare = hare.next_
    if hare is None or tortoise is None:
        return None
    #
    # We are now in a loop. Let's find its size.
    #
    loop_length = 1
    hare = hare.next_
    while hare != tortoise:
        hare = hare.next_
        loop_length += 1
    #
    # Use a leading pointer to find the start of the loop.
    #
    hare = tortoise = sll.head
    for _ in xrange(loop_length):
        hare = hare.next_
    while hare != tortoise:
        hare = hare.next_
        tortoise = tortoise.next_
    return hare
