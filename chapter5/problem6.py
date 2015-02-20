#
# Write a program to swap the odd and even bits in an integer with as few
# instructions as possible.  E.g. bit 0 and bit 1 are swapped, bit 2 and bit 3
# are swapped, etc.
#


def calculate_mask(n):
    mask = 0
    while n:
        mask = (mask << 32) | 0x55555555
        n >>= 32
    return mask


def swap(n):
    mask = calculate_mask(n)
    return ((n & mask) << 1) | ((n & ~mask) >> 1)
