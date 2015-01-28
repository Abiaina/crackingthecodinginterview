from stack import Stack


class Tower(Stack):
    """A stack that prohibits pushing a larger value on top of a smaller
    one."""

    def push(self, value):
        if len(self) and value >= self.peek():
            raise ValueError(
                "you can't push %d on top of %d" % (value, self.peek()))
        super(Tower, self).push(value)


class Hanoi(object):

    def __init__(self, discs):
        self.towers = [Tower(discs), Tower(), Tower()]

    def move(self, src, dst, depth):
        if depth == 1:
            dst.push(src.pop())
        else:
            buf = self.get_buffer(src, dst)
            self.move(src, buf, depth - 1)
            self.move(src, dst, 1)
            self.move(buf, dst, depth - 1)

    def get_buffer(self, src, dst):
        return [t for t in self.towers if t != src and t != dst][0]

    def solve(self):
        self.move(self.towers[0], self.towers[2], len(self.towers[0]))
