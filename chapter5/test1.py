import unittest
import problem1


def to_decimal(binary_string):
    bits = [int(b) for b in binary_string]
    powers = reversed(range(len(binary_string)))
    return sum([(a * 2 ** b) for (a, b) in zip(bits, powers)])


def to_binary(decimal):
    bits = []
    while True:
        bits.append(str(decimal % 2))
        decimal >>= 1
        if not decimal:
            break
    return "".join(reversed(bits))


class TestToDecimal(unittest.TestCase):

    def test(self):
        self.assertEquals(to_decimal("00"), 0)
        self.assertEquals(to_decimal("01"), 1)
        self.assertEquals(to_decimal("10"), 2)
        self.assertEquals(to_decimal("11"), 3)
        self.assertEquals(to_decimal("1000"), 8)
        self.assertEquals(to_decimal("10000"), 16)
        self.assertEquals(to_decimal("100000"), 32)
        self.assertEquals(to_decimal("100010"), 34)


class TestToBinary(unittest.TestCase):

    def test(self):
        self.assertEquals(to_binary(0), "0")
        self.assertEquals(to_binary(1), "1")
        self.assertEquals(to_binary(2), "10")
        self.assertEquals(to_binary(3), "11")
        self.assertEquals(to_binary(8), "1000")
        self.assertEquals(to_binary(16), "10000")
        self.assertEquals(to_binary(32), "100000")
        self.assertEquals(to_binary(34), "100010")


class TestInsert(unittest.TestCase):

    def test_sanity(self):
        N = to_decimal("100000000000")
        M = to_decimal("10011")
        expected = to_decimal("100001001100")
        actual = problem1.insert(N, M, 2, 6)
        self.assertEquals(actual, expected)
