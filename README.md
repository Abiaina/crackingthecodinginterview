crackingthecodinginterview
==========================

This repository contains solutions to the interview problems from ["Cracking the Coding Interview"](http://www.amazon.com/Cracking-Coding-Interview-Programming-Questions/dp/098478280X) by Gayle Laakmann McDowell.
The book comes with solutions and Java code, but I thought it would be a good exercise to code up my own solutions in Python.
The book contains more than the actual interview problems: resume preparation and interview tips, and inside info about how some of the major companies do their hiring.
I thoroughly recommend it.

Running the Solutions
---------------------

Each module corresponds to a chapter of the book.
Within each module, files named `problemX.py` contain solutions to problem X.
Some files contain main functions, so you can run them, for example:

    cd chapter1
    python problem1.py

Files named `testX.py` contain [unit tests](https://docs.python.org/2/library/unittest.html) for problem X.
To run the unit tests, you need to [nosetests](https://nose.readthedocs.org/en/latest/):

    cd chapter1
    nosetests test1.py

You can also run all the tests by:

    nosetests .

Found a Bug?
------------

If you've found a bug or a test case that I'm not covering, please submit a pull request.
