#
# Given an image represented by an N*N matrix, write a method to rotate the
# image by 90 degrees.  Can you do this in place?
#


def swap(m, x1, y1, x2, y2):
    m[x1][y1], m[x2][y2] = m[x2][y2], m[x1][y1]


def transpose(m):
    N = len(m)
    for i in xrange(N):
        for j in xrange(i + 1, N):
            swap(m, i, j, j, i)
    return m  # return makes chaining functions easier


def flip_horiz(m):
    N = len(m)
    for i in xrange(N):
        for j in xrange(N / 2):
            swap(m, i, N - 1 - j, i, j)
    return m


def flip_vert(m):
    N = len(m)
    for i in xrange(N / 2):
        for j in xrange(N):
            swap(m, i, j, N - i - 1, j)
    return m


def rotate_clockwise(m):
    return transpose(flip_vert(m))


def rotate_anticlockwise(m):
    return transpose(flip_horiz(m))
