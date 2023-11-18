#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Iterator method

It is a Behavioral Design Pattern that allows us to traverse the elements of the collections without taking the exposure of
in-depth details of the elements. It provides a way to access the elements of complex data structure sequentially without repeating them.
According to GangOfFour, Iterator Pattern is used ” to access the elements of an aggregate object sequentially without exposing its underlying
implementation”.

.. _PEP 484:
    https://www.python.org/dev/peps/pep-0484/

.. _Google Python Style Guide:
    http://google.github.io/styleguide/pyguide.html

.. _Original source:
    https://www.geeksforgeeks.org/python-design-patterns/
"""

# Problem Without using Iterator Method
# Imagine you are creating an application for small kids which takes any valid alphabet as input and return all the alphabets up to that.
# When this application will be used only a few times, it is okay to run For loop and While loop again and again but when the frequency of
# running increases this process becomes quite inefficient. So, we have to find a way in order to avoid these loops. This problem may
# become bigger when we will work on complex non-linear data structures like Trees, Graphs where traversing is not that simple as in an array. 
# The following diagram depicts the image of the Tree data structure.

# Solution Using Iterator Method
# Here we will discuss the solution for the above-described problem. It’s always handy for Python users to use Iterators for traversing any
# kind of data structure doesn’t matter they are linear or no-linear data structures. We have two options to implement Iterators in Python
# either we can use the in-built iterators to produce the fruitful output or explicitly we can create iterators with the help of Generators.
# In the following code, we have explicitly created the Iterators with the help of generators.

""" helper method for iterator"""

def main() -> None:
    """main function"""
    alphabets_upto_K = alphabets_upto('K')
    alphabets_upto_M = alphabets_upto('M')
    for alpha in alphabets_upto_K:
        print(alpha, end=" ")
    print()
    for alpha in alphabets_upto_M:
        print(alpha, end=" ")
    """call the inbuiltIterators"""
    inBuilt_Iterator1()
    inBuilt_Iterator2()
    return None

def alphabets_upto(letter):
    """Counts by word numbers, up to a maximum of five"""
    for i in range(65, ord(letter)+1):
        yield chr(i)

# Following code is the example of using an in-built iterator method
def inBuilt_Iterator1():
    """utility function"""
    alphabets = [chr(i) for i in range(65, 91)]
    """using in-built iterator"""
    for alpha in alphabets:
        print(alpha, end = " ")
    print()

def inBuilt_Iterator2():
    """utility function"""    
    alphabets = [chr(i) for i in range(97, 123)]
    """using in-built iterator"""
    for alpha in alphabets:
        print(alpha, end = " ")
    print()

if __name__ == "__main__" :
    main()
