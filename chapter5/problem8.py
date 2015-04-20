#
# A monochrome screen is stored as a single array of bytes, allowing 8
# consecutive pixels to be stored in one byte.  The screen has width w, where
# w is divisible by 8.  Implement a function
# draw_horizontal_line(screen, width, x1, x2, y).
#
from __future__ import division


def draw_horizontal_line(screen, width, x1, x2, y):
    assert x1 < x2
    assert x2 - x1 <= width
    first = y * width // 8 + x1 // 8
    last = y * width // 8 + x2 // 8
    assert last <= len(screen)

    if first == last:
        screen[first] |= (0xff >> (x1 % 8)) - (0xff >> (x2 % 8))
    else:
        screen[first] |= 0xff >> (x1 % 8)
        for i in xrange(first + 1, last):
            screen[i] = 0xff
        if last < len(screen):
            screen[last] |= 0xff - (0xff >> (x2 % 8))
