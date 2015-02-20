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
        count += 1
        C = C & (C - 1)  # Clear the least significant bit
    return count
