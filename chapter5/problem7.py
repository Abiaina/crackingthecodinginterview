#
# An array contains all the integers from 0 to n, except for one number, which
# is missing. In this problem, we cannot access an entire integer in A with a
# single operation. The elements of A are represented in binary, and the only
# operation we can use to access them is "fetch the jth bit of A[i]", which
# takes constant time. Write code to find the missing integer. Can you do it
# in O(n) time?
#

#
# Assume 32-bit integers
#
BIT_DEPTH = 32


class Array(object):

    def __init__(self, n, missing):
        if n == missing:
            raise ValueError("n may not be the missing number")
        self.n = n
        self.numbers = range(self.n + 1)
        self.numbers.remove(missing)

    def access(self, i, j):
        return (self.numbers[i] >> j) & 0x1

    def __len__(self):
        return len(self.numbers)


def solve(A):
    counter = [0] * BIT_DEPTH
    for i in range(A.n + 1):
        for j in range(BIT_DEPTH):
            counter[j] += (i >> j) & 0x1

    for i in range(len(A)):
        for j in range(BIT_DEPTH):
            counter[j] -= A.access(i, j)

    return sum([(a << b) for (a, b) in zip(counter, range(BIT_DEPTH))])
