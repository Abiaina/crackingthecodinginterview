#
# Assume you have a method isSubstring which checks if one word is a substring
# of another.  Given two strings, s1 and s2, write code to check if s2 is a
# rotation of s1 using only one call to isSubstring (e.g. "waterbottle" is a
# rotation of "erbottlewat").
#


def is_substring(s1, s2):
    return s1 in s2


def is_rotation(s1, s2):
    return is_substring(s2, s1 + s1)


def main():
    assert is_rotation("erbottlewat", "waterbottle",)
    assert not is_rotation("waterbottle", "gogomobile")

if __name__ == "__main__":
    main()
