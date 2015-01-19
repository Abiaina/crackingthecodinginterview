#
# Implement a method to perform basic string compression using the counts of
# repeated characters.  For example, "aabcccccaaa" should become "a2b1c5a3".
# If the "compressed" string would not become smaller than the original string,
# your method should return the original string.
#


def compress(s):
    i = 0
    result = []
    while i < len(s):
        j = 1
        while i + j < len(s) and s[i + j] == s[i]:
            j += 1
        result.append("%s%d" % (s[i], j))
        i += j
    compressed = "".join(result)
    if len(compressed) < len(s):
        return compressed
    return s


def main():
    assert compress("aabcccccaaa") == "a2b1c5a3"
    assert compress("unique") == "unique"


if __name__ == "__main__":
    main()
