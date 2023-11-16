#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Multiple dispatching example

When dealing with multiple types which are interacting, a program can
get particularly messy. For example, consider a system that parses and
executes mathematical expressions. You want to be able to say Number
+ Number, Number * Number, etc., where Number is the base class
for a family of numerical objects. But when you say a + b, and you don’t
know the exact type of either a or b, so how can you get them to interact
properly?

The answer starts with something you probably don’t think about: Python
performs only 'single dispatching'. That is, if you are performing an
operation on more than one object whose type is unknown, Python can
invoke the dynamic binding mechanism on only one of those types. This
doesn’t solve the problem, so you end up detecting some types manually
and effectively producing your own dynamic binding behavior.

The solution is called multiple dispatching. Remember that
polymorphism can occur only via member function calls, so if you want
double dispatching to occur, there must be two member function calls: the
first to determine the first unknown type, and the second to determine the
second unknown type. With multiple dispatching, you must have a
polymorphic method call to determine each of the types. Generally, you’ll
set up a configuration such that a single member function call produces
more than one dynamic member function call and thus determines more
than one type in the process. To get this effect, you need to work with
more than one polymorphic method call: you’ll need one call for each
dispatch. The methods in the following example are called compete( )
and eval( ), and are both members of the same type. (In this case there
will be only two dispatches, which is referred to as double dispatching). If
you are working with two different type hierarchies that are interacting,
then you’ll have to have a polymorphic method call in each hierarchy. Add
"""

from __future__ import generators
import random

class Outcome:

    def __init__(self, value, name):
        self.value = value
        self.name = name

    def __str__(self):
        return self.name
    
    def __eq__(self, other):
        return self.value == other.value

Outcome.WIN = Outcome(0, "win")
Outcome.LOSE = Outcome(1, "lose")
Outcome.DRAW = Outcome(2, "draw")

class Item(object):

    def compete(self, item):
        # Use a tuple for table lookup:
        return outcome[self.__class__, item.__class__]

    def __str__(self):
        return self.__class__.__name__

class Paper(Item): pass
class Scissors(Item): pass
class Rock(Item): pass

outcome = {
(Paper, Rock): Outcome.WIN,
(Paper, Scissors): Outcome.LOSE,
(Paper, Paper): Outcome.DRAW,
(Scissors, Paper): Outcome.WIN,
(Scissors, Rock): Outcome.LOSE,
(Scissors, Scissors): Outcome.DRAW,
(Rock, Scissors): Outcome.WIN,
(Rock, Paper): Outcome.LOSE,
(Rock, Rock): Outcome.DRAW,
}

def match(item1, item2):
    print("%s <--> %s : %s" % (item1, item2, item1.compete(item2)))

# Generate the items:
def itemPairGen(n):
    # Create a list of instances of all Items:
    Items = Item.__subclasses__()
    for i in range(n):
        yield (random.choice(Items)(),
    random.choice(Items)())
    for item1, item2 in itemPairGen(20):
        match(item1, item2)
