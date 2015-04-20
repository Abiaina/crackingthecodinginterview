import unittest
import problem8


class TestDrawHorizontalLine(unittest.TestCase):

    def test_aligned1(self):
        screen = [0x00, 0x00, 0x00,
                  0x00, 0x00, 0x00,
                  0x00, 0x00, 0x00]
        expected = [0x00, 0x00, 0x00,
                    0x00, 0xff, 0x00,
                    0x00, 0x00, 0x00]
        problem8.draw_horizontal_line(screen, 24, 8, 16, 1)
        self.assertEquals(screen, expected)

    def test_aligned2(self):
        screen = [0x00, 0x00, 0x00,
                  0x00, 0x00, 0x00,
                  0x00, 0x00, 0x00]
        expected = [0xff, 0xff, 0x00,
                    0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00]
        problem8.draw_horizontal_line(screen, 24, 0, 16, 0)
        self.assertEquals(screen, expected)

    def test_aligned3(self):
        screen = [0x00, 0x00, 0x00,
                  0x00, 0x00, 0x00,
                  0x00, 0x00, 0x00]
        expected = [0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00,
                    0x00, 0x00, 0xff]
        problem8.draw_horizontal_line(screen, 24, 16, 24, 2)
        self.assertEquals(screen, expected)

    def test_partial1(self):
        screen = [0x00, 0x00, 0x00]
        expected = [0x00, 0x7e, 0x00]
        problem8.draw_horizontal_line(screen, 24, 9, 15, 0)
        self.assertEquals(screen, expected)

    def test_partial2(self):
        screen = [0x00, 0x00, 0x00]
        expected = [0x00, 0xff, 0x80]
        problem8.draw_horizontal_line(screen, 24, 8, 17, 0)
        self.assertEquals(screen, expected)

    def test_partial3(self):
        screen = [0x00, 0x00, 0x00]
        expected = [0x01, 0xff, 0x00]
        problem8.draw_horizontal_line(screen, 24, 7, 16, 0)
        self.assertEquals(screen, expected)

    def test_partial4(self):
        screen = [0x00, 0x00, 0x00]
        expected = [0x01, 0xff, 0x80]
        problem8.draw_horizontal_line(screen, 24, 7, 17, 0)
        self.assertEquals(screen, expected)
