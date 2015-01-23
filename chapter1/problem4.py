#
# Write a method to replace all spaces in a string with "%20".  You may assume
# that the string has sufficient space at the end to hold additional
# characters. (Note: if implementing in Java, please use a character array so
# that you can perform this operation in place)
#

SPACE = " "


def pad(l):
    """Pad a list with dummy elements."""
    return l + [None] * (l.count(SPACE) * 2)


def escape_spaces(s):
    l = list(s)
    length = len(l)
    num_spaces = l.count(SPACE)
    out = length - 1 + num_spaces * 2
    l = pad(l)
    for i in xrange(length - 1, -1, -1):
        if l[i] == SPACE:
            l[out - 2], l[out - 1], l[out] = "%", "2", "0"
            out -= 3
        else:
            l[out] = l[i]
            out -= 1
    return "".join(l)
