#
# Write a program to sort a stack in ascending order (with biggest items on
# top).  You may use at most one additional stack to hold items, but you may
# not copy the elements into any other data structure (such as an array). The
# stack supports the following operations: push, pop, peek and isEmpty.
#
from stack import Stack


def bubble_sort_iter(src, dst, compare):
    percolations = 0
    dst.push(src.pop())
    while not src.is_empty():
        elt = src.pop()
        if compare(elt, dst.peek()):
            tmp = dst.pop()
            dst.push(elt)
            dst.push(tmp)
            percolations += 1
        else:
            dst.push(elt)
    return percolations


def sort_stack(stack):
    if stack.is_empty():
        return

    buf = Stack()

    #
    # Bubble-sort stack into buf
    # Bubble-sort buf into stack (in reverse order).
    # Repeat until the second bubble sort step achieves nothing.
    #
    while True:
        bubble_sort_iter(stack, buf, lambda a, b: a > b)
        percolations = bubble_sort_iter(buf, stack, lambda a, b: a < b)
        if percolations == 0:
            break
