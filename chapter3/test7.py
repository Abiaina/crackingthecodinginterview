import unittest

from problem7 import Animal, AnimalShelter


class TestAnimalShelter(unittest.TestCase):

    def setUp(self):
        self.shelter = AnimalShelter()
        self.shelter.enqueue(Animal("A", Animal.DOG))
        self.shelter.enqueue(Animal("B", Animal.DOG))
        self.shelter.enqueue(Animal("c", Animal.CAT))
        self.shelter.enqueue(Animal("D", Animal.DOG))
        self.shelter.enqueue(Animal("e", Animal.CAT))
        self.shelter.enqueue(Animal("F", Animal.DOG))
        self.shelter.enqueue(Animal("g", Animal.CAT))
        self.shelter.enqueue(Animal("h", Animal.CAT))

    def test_dequeue_any(self):
        self.assertEquals(self.shelter.dequeue_any().name, "A")
        self.assertEquals(self.shelter.dequeue_any().name, "B")
        self.assertEquals(self.shelter.dequeue_any().name, "c")
        self.assertEquals(self.shelter.dequeue_any().name, "D")

        self.shelter.enqueue(Animal("X", Animal.DOG))
        self.shelter.enqueue(Animal("Y", Animal.DOG))
        self.shelter.enqueue(Animal("Z", Animal.DOG))

        self.assertEquals(self.shelter.dequeue_any().name, "e")
        self.assertEquals(self.shelter.dequeue_any().name, "F")
        self.assertEquals(self.shelter.dequeue_any().name, "g")
        self.assertEquals(self.shelter.dequeue_any().name, "h")

        self.assertEquals(self.shelter.dequeue_any().name, "X")
        self.assertEquals(self.shelter.dequeue_any().name, "Y")
        self.assertEquals(self.shelter.dequeue_any().name, "Z")

        self.assertRaises(ValueError, self.shelter.dequeue_any)

    def test_dequeue_cat(self):
        self.assertEquals(self.shelter.dequeue_cat().name, "c")
        self.shelter.enqueue(Animal("X", Animal.DOG))

        self.assertEquals(self.shelter.dequeue_cat().name, "e")
        self.shelter.enqueue(Animal("Y", Animal.DOG))

        self.assertEquals(self.shelter.dequeue_cat().name, "g")
        self.shelter.enqueue(Animal("Z", Animal.DOG))

        self.assertEquals(self.shelter.dequeue_cat().name, "h")

        self.assertRaises(ValueError, self.shelter.dequeue_cat)

        self.assertEquals(self.shelter.dequeue_any().name, "A")
        self.assertEquals(self.shelter.dequeue_any().name, "B")
        self.assertEquals(self.shelter.dequeue_any().name, "D")
        self.assertEquals(self.shelter.dequeue_any().name, "F")
        self.assertEquals(self.shelter.dequeue_any().name, "X")
        self.assertEquals(self.shelter.dequeue_any().name, "Y")
        self.assertEquals(self.shelter.dequeue_any().name, "Z")

    def test_dequeue_dog(self):
        self.assertEquals(self.shelter.dequeue_dog().name, "A")
        self.shelter.enqueue(Animal("x", Animal.CAT))

        self.assertEquals(self.shelter.dequeue_dog().name, "B")
        self.shelter.enqueue(Animal("y", Animal.CAT))

        self.assertEquals(self.shelter.dequeue_dog().name, "D")
        self.shelter.enqueue(Animal("z", Animal.CAT))

        self.assertEquals(self.shelter.dequeue_dog().name, "F")

        self.assertRaises(ValueError, self.shelter.dequeue_dog)

        self.assertEquals(self.shelter.dequeue_any().name, "c")
        self.assertEquals(self.shelter.dequeue_any().name, "e")
        self.assertEquals(self.shelter.dequeue_any().name, "g")
        self.assertEquals(self.shelter.dequeue_any().name, "h")
        self.assertEquals(self.shelter.dequeue_any().name, "x")
        self.assertEquals(self.shelter.dequeue_any().name, "y")
        self.assertEquals(self.shelter.dequeue_any().name, "z")
