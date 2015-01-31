#
# An animal shelter holds only dogs and cats and operates strictly on a "first
# in, first out" basis.  People must adopt the "oldest" (based on arrival time)
# of all animals at the shelter, or they can select if they prefer a dog or cat
# (and receive the oldest animal of that type).  They cannot select which
# specific animal they would like.  Create the data structures to maintain this
# system, and implement operations such as enqueue, dequeue_dog, dequeue_cat,
# and dequeue_any.  You may use the built-in LinkedList data structure.
#
import sys
from queue import Queue


class Animal(object):
    DOG = 0
    CAT = 1

    def __init__(self, name, type_):
        self.name = name
        self.type_ = type_


class AnimalShelter(object):

    def __init__(self):
        self.dogs = Queue()
        self.cats = Queue()
        self.ordinal = 0

    def enqueue(self, animal):
        queue = self.dogs if animal.type_ == Animal.DOG else self.cats
        queue.enqueue((self.ordinal, animal))
        self.ordinal += 1

    def dequeue_dog(self):
        return self.dogs.dequeue()[1]

    def dequeue_cat(self):
        return self.cats.dequeue()[1]

    def dequeue_any(self):
        try:
            dog_ord, _ = self.dogs.peek()
        except ValueError:
            dog_ord = sys.maxint
        try:
            cat_ord, _ = self.cats.peek()
        except ValueError:
            cat_ord = sys.maxint
        queue = self.dogs if dog_ord < cat_ord else self.cats
        return queue.dequeue()[1]
