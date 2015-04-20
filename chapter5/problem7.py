#
# An array contains all the integers from 0 to n, except for one number, which
# is missing. In this problem, we cannot access an entire integer in A with a
# single operation. The elements of A are represented in binary, and the only
# operation we can use to access them is "fetch the jth bit of A[i]", which
# takes constant time. Write code to find the missing integer. Can you do it
# in O(n) time?
#
import math


class Array(object):
    """Stores numbers, allows access to each number bit by bit only."""

    def __init__(self, n, missing):
        """Create an array storing numbers from zero to n inclusive, with the
        exception of a single missing number."""
        if n == missing:
            raise ValueError("n may not be the missing number")
        self.n = n
        self.numbers = range(self.n + 1)
        self.numbers.remove(missing)

    def access(self, i, j):
        """Return the jth bit of the ith number.  The LSB is the zeroth bit."""
        return (self.numbers[i] >> j) & 0x1

    def __len__(self):
        return len(self.numbers)


def solve(A):
    #
    # The idea is to recover the missing number bit by bit, by counting the
    # number of ones and zeros in each bit place.  After each recovered bit, we
    # can discard any remaining numbers that have a different bit value in that
    # bit place.
    #
    indices = range(len(A))
    num_bits = int(math.ceil(math.log(A.n, 2)))
    missing_number = 0

    for j in xrange(num_bits):
        zeros = []
        ones = []
        for i in indices:
            if A.access(i, j) == 1:
                ones.append(i)
            else:
                zeros.append(i)

        if A.n % 2 == 1:
            missing_bit = 1 if len(ones) < len(zeros) else 0
        else:
            missing_bit = 1 if len(ones) < len(zeros) - 1 else 0
        missing_number += missing_bit << j
        indices = ones if missing_bit == 1 else zeros

    return missing_number
