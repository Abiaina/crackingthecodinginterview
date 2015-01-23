#
# Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP: how would you solve this problem if a temporary buffer was not
# allowed?
#


def rmdup(sll):
    """Remove duplicates by keeping track of seen elements in a buffer."""
    seen = set()
    prev = None
    current = sll.head
    while current:
        if current.payload in seen:
            prev.next_ = current.next_
            current = current.next_
        else:
            seen.add(current.payload)
            prev = current
            current = current.next_
    return sll  # for chaining


def rmdup2(sll):
    """Remove duplicates without using an additional buffer."""
    start = sll.head
    while start:
        node = start
        while node and node.next_:
            if node.next_.payload == start.payload:
                node.next_ = node.next_.next_
            node = node.next_
        start = start.next_
    return sll
