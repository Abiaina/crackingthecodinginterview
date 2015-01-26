#
# Imagine a literal stack of plates. If the stack gets too high, it might
# topple. Therefore, in real life, we would likely start a new stack when the
# previous stack exceeds some threshold.  Implement a data structure
# SetOfStacks that mimics this. SetOfStacks should be composed of several
# substacks and should create a new stack once the previous one exceeds
# capacity.  SetOfStacks.push() and SetOfStacks.pop() should behave identically
# to a single stack (that is, pop() should return the same values as it would
# if there was just a single stack).
#
# FOLLOW UP: Implement a function popAt(int index) which performs a pop
# operation on a specific sub-stack.
#
from stack import Stack


class SetOfStacks(object):

    def __init__(self, thresh=3):
        self.thresh = thresh
        #
        # We can't make it a Stack of Stacks since we need indexing for the
        # popAt method.
        #
        self.substacks = [Stack()]

    def push(self, value):
        if len(self.substacks[-1]) == self.thresh:
            self.substacks.append(Stack())
        self.substacks[-1].push(value)

    def pop(self):
        return self.pop_at(-1)

    def peek(self):
        return self.substacks[-1].peek()

    def pop_at(self, index):
        value = self.substacks[index].pop()
        #
        # Get rid of this substack if it's empty and isn't the last one
        #
        if len(self.substacks[index]) == 0 and len(self.substacks) > 1:
            del self.substacks[index]
        return value
