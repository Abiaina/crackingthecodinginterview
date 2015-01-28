#
# In the classic problem of the Towers of Hanoi, you have 3 towers and N disks
# of different sizes that can slide onto any tower. The puzzle starts with
# disks sorted in ascending order of size from top to bottom (i.e. each disk
# sits on top of an even larger one). You have the following constraints:
#
# (1) Only one disk can be moved at a time.
# (2) A disk is slid of the top of one tower onto the next tower.
# (3) A disk can only be placed on top of a larger disk.
#
# Write a program to move the disks from the first tower to the last using
# stacks.
#
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
