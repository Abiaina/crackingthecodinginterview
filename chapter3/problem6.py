#
# Write a program to sort a stack in ascending order (with biggest items on
# top).  You may use at most one additional stack to hold items, but you may
# not copy the elements into any other data structure (such as an array). The
# stack supports the following operations: push, pop, peek and isEmpty.
#
from stack import Stack


def sort_stack(stack):
    if stack.is_empty():
        return

    buf = Stack()
    is_sorted = False

    #
    # Bubble-sort the stack into buf (in reverse order).
    # Copy buf back into stack.
    # Repeat until bubble sort step achieves nothing.
    #
    while not is_sorted:
        is_sorted = True
        buf.push(stack.pop())
        while not stack.is_empty():
            elt = stack.pop()
            if elt > buf.peek():
                tmp = buf.pop()
                buf.push(elt)
                buf.push(tmp)
                is_sorted = False
            else:
                buf.push(elt)
        while not buf.is_empty():
            stack.push(buf.pop())
