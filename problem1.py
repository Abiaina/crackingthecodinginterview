#
# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?
#


def is_unique(s):
    #
    # Runs in O(N) -- that's the time required to construct the set.
    # The len() operations are O(1).
    #
    return len(set(s)) == len(s)


def is_unique2(s):
    #
    # Version without additional data structures.
    # Runs in O(N^2).
    #
    for i, c1 in enumerate(s):
        for c2 in s[i+1:]:
            if c1 == c2:
                return False
    return True


def main():
    unique = ["fobar", "misha"]
    not_unique = ["foobar", "mikhail"]

    for s in unique:
        assert is_unique(s)
        assert is_unique2(s)

    for s in not_unique:
        assert not is_unique(s)
        assert not is_unique(s)

    s = raw_input("Enter a string: ")
    print "is_unique(%s):" % repr(s), is_unique(s)
    print "is_unique2(%s):" % repr(s), is_unique2(s)

if __name__ == "__main__":
    main()
