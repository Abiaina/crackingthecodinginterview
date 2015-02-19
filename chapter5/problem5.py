#
# Write a function to determine the number of bits to convert integer A to
# integer B.
#
# EXAMPLE
#
# Input 31, 14
# Output: 2
#


def hamming(A, B):
    C = A ^ B
    count = 0
    while C:
        count += C % 2
        C >>= 1
    return count
