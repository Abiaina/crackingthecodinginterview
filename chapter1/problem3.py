#
# Given a string, determine if one is a permutation of the other
#
from collections import Counter


def is_permutation(s1, s2):
    return Counter(s1) == Counter(s2)


def main():
    s1 = raw_input("Enter a string: ")
    s2 = raw_input("Enter another string: ")
    print "is_permutation(%s, %s):" % (repr(s1), repr(s2)),
    print is_permutation(s1, s2)

if __name__ == "__main__":
    main()
