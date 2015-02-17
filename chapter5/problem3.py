#
# Given a positive integer, print the next smallest and the next largest number
# that have the same number of 1 bits in their binary representation.
#


def larger(n):
    if n == 0:
        raise ValueError("number has no 1 bits")
    num_ones = 0
    counter = 0
    mask = 1
    while not (num_ones and n & mask == 0):
        counter += 1
        if mask & n:
            num_ones += 1
        mask <<= 1
    n |= mask
    mask -= 1
    n &= ~mask
    mask >>= counter - num_ones + 1
    return n | mask


def smaller(n):
    tmp = n
    num_bits = 0
    while tmp:
        num_bits += 1
        tmp >>= 1

    num_zeros = 0
    counter = 0
    mask = 1
    while not (num_zeros and n & mask):
        if counter == num_bits:
            raise ValueError("number can be represented entirely by 1 bits")
        counter += 1
        if mask & n == 0:
            num_zeros += 1
        mask <<= 1

    mask = (mask << 1) - 1
    n &= ~mask
    lsb_mask = (1 << (num_zeros - 1)) - 1
    mask = (mask >> 1) & ~lsb_mask
    return n | mask


def solution(n):
    return larger(n), smaller(n)
