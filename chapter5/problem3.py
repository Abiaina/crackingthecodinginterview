#
# Given a positive integer, print the next smallest and the next largest number
# that have the same number of 1 bits in their binary representation.
#


def larger(n):
    if n == 0:
        raise ValueError("number has no 1 bits")
    mask = 0x01
    to_add = 0x02
    while n ^ mask == 0:
        mask <<= 1
        to_add <<= 1
    return n - mask + to_add


def smaller(n):
    tmp = n
    mask = 0x02
    to_add = 0x01
    while tmp:
        tmp >>= 1
        mask <<= 1
        to_add <<= 1
    while mask and n ^ mask == 0:
        mask >>= 1
        to_add >>= 1
    if not mask:
        raise ValueError("this number is already the smallest possible")
    return n - mask + to_add


def solution(n):
    return larger(n), smaller(n)
