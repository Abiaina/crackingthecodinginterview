#
# You are given two 32-bit numbers, N and M, and two positions, i and j.  You
# can assume that the bits j through i have enough space to fit all of M.  That
# is, if M = 10011, you can assume that there are at least 5 bits between j and
# i.  You would not, for example, hav ej = 3 and i = 2, because M could not
# fully fit between bit 3 and bit 2.
#
# EXAMPLE:
# Input:  N = 10000000000 M = 10011 i = 2 j = 6
# Output: N = 10001001100
#


def clear_range(N, i, j):
    mask = ((1 << (j + 1)) - 1) - ((1 << i) - 1)
    return N & (~mask)


def insert(N, M, i, j):
    return clear_range(N, i, j) | (M << i)
