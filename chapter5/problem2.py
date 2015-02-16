#
# Given a real number between 0 and 1 (e.g., 0.72) that is passed in as a
# double, print the binary representation. If the number cannot be represented
# accurately in binary with at most 32 characters, print "ERROR."
#


def binary_repr(decimal):
    factor = 1.0
    bits = []
    for _ in range(32):
        if decimal == 0:
            break
        elif decimal >= factor:
            bits.append("1")
            decimal -= factor
        else:
            bits.append("0")
        factor /= 2
    if decimal > 0:
        return "ERROR"
    if not bits:
        return "0"
    bits.insert(1, ".")
    return "".join(bits)
