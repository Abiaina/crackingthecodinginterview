#
# Write an algorithm such that if an element in an M*N matrix is 0, its entire
# row and column are set to zero.
#


def setzero(m):
    M = len(m)
    N = len(m[0])
    rows = set()
    cols = set()
    for i in xrange(M):
        for j in xrange(N):
            if m[i][j] == 0:
                rows.add(i)
                cols.add(j)
    for i in rows:
        for j in xrange(N):
            m[i][j] = 0
    for i in xrange(M):
        for j in cols:
            m[i][j] = 0
    return m
