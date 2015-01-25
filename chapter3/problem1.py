class TripleStack(object):

    def __init__(self, size=100):
        self.size = size
        self.array = [None] * size * 3
        self.tops = [-1, -1, -1]

    def push(self, stack, value):
        if stack not in [0, 1, 2]:
            raise ValueError("invalid stack number")
        elif self.tops[stack] == self.size - 1:
            raise ValueError("stack %d is full" % stack)
        self.tops[stack] += 1
        idx = self.__abs_index(stack, self.tops[stack])
        self.array[idx] = value

    def pop(self, stack):
        if stack not in [0, 1, 2]:
            raise ValueError("invalid stack number")
        elif self.tops[stack] == -1:
            raise ValueError("stack %d is empty" % stack)
        idx = self.__abs_index(stack, self.tops[stack])
        value = self.array[idx]
        self.tops[stack] -= 1
        return value

    def peek(self, stack):
        if stack not in [0, 1, 2]:
            raise ValueError("invalid stack number")
        elif self.tops[stack] == -1:
            raise ValueError("stack %d is empty" % stack)
        idx = self.__abs_index(stack, self.tops[stack])
        return self.array[idx]

    def __abs_index(self, stack, rel_index):
        return 3*rel_index + stack
