Solutions to Chapter 2
======================

The focus of this chapter is [linked lists](http://en.wikipedia.org/wiki/Linked_list).
The problems are mostly self-contained, with the exception of the implementation of the linked list.
More specifically, sll.py contains a trivial implementation of a singly linked list, which attempts to balance simplicity, brevity, and minimal code duplications in the solutions.
All the other problems include that module in order to minimize code duplication.

Testing
-------

The solutions to each problem are tested by a suite of [unit tests](https://docs.python.org/2/library/unittest.html). 
In order to run the tests for a particular module, use [nosetests](https://nose.readthedocs.org/en/latest/):

    nosetests problem2.py

Or to run tests for the entire chapter:

    nosetests *.py

Found a Bug?
------------

If you've found a bug or a test case that I'm not covering, please submit a pull request.
