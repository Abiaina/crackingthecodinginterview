#
# Implement a function reverse(char *str) in C or C++ which reverses a
# null-terminated string.
#


def reverse(s):
    l = list(s)
    length = len(l)
    for i in range(length/2):
        l[i], l[length - i - 1] = l[length - i - 1], l[i]
    return "".join(l)


def main():
    assert reverse("misha") == "ahsim"
    assert reverse("mikhail") == "liahkim"
    assert reverse("foob") == "boof"
    assert reverse("radar") == "radar"

    s = raw_input("Enter a string: ")
    print "reverse(%s):" % repr(s), reverse(s)

if __name__ == "__main__":
    main()
