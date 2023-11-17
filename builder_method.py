#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Builder Method

It is a Creation Design Pattern which aims to "Separate the construction of a complex object from its representation
so that the same construction process can create different representations." It allows you to construct complex
objects step by step. Here using the same construction code, we can produce different types and representations of the object easily.

It is basically designed to provide flexibility to the solutions to various object creation problems in object-oriented programming.

Advantages of using Builder Method:
Reusability: While making the various representations of the products, we can use the same construction code for other representations as well.
Single Responsibility Principle: We can separate out both the business logic as well as the complex construction code from each other.
Construction of the object: Here we construct our object step by step, defer construction steps or run steps recursively.

Disadvantages of using Builder method:
Code complexity increases: The complexity of our code increases, because the builder pattern requires creating multiple new classes.
Mutability: It requires the builder class to be mutable
Initialization: Data members of the class are not guaranteed to be initialized.

Applicability:
Constructing Complex objects : The Builder Method allows you to construct the products step-by-step. Even, we can defer the
execution of some steps without breaking the final product. To create an object tree, it is handy to call the steps recursively.It prevents the client code from fetching the incomplete data because it doesn’t allow the exposing of an unfinished object.
Differ by Representations: The Builder pattern is applicable when construction of various representations of the product involves
similar steps that differ only in the details. The base builder interface is used to define all the construction steps while these steps are implemented by concrete builders.

.. _PEP 484:
    https://www.python.org/dev/peps/pep-0484/

.. _Google Python Style Guide:
    http://google.github.io/styleguide/pyguide.html

.. _Original source:
    https://www.geeksforgeeks.org/python-design-patterns/
"""

def main() -> None:
    """main function"""
    # without builde rmethod
    sde = SDE()   # object for SDE
    dsa = DSA()   # object for DSA
    stl = STL()   # object for STL
    print(f'Name of Course: {sde} and its Fee: {sde.fee}')
    print(f'Name of Course: {stl} and its Fee: {stl.fee}')
    print(f'Name of Course: {dsa} and its Fee: {dsa.fee}')
    # with builder method
    dsa = DSA()  # object for DSA course
    sde = SDE()  # object for SDE course
    stl = STL()  # object for STL course
    complex_course = construct_course(Complexcourse)
    print(complex_course)
    return None

class DSA():
    """Class for Data Structures and Algorithms"""
    def Fee(self):
        self.fee = 8000
 
    def available_batches(self):
        self.batches = 5
 
    def __str__(self):
        return "DSA"
 
class SDE():
    """Class for Software development Engineer"""
    def Fee(self):
        self.fee = 10000
 
    def available_batches(self):
        self.batches = 4
 
    def __str__(self):
        return "SDE"
 
class STL():
    """class for Standard Template Library of C++"""
    def Fee(self):
        self.fee = 5000
 
    def available_batches(self):
        self.batches = 7
 
    def __str__(self):
        return "STL"

class Course:
    def __init__(self):
        self.Fee()
        self.available_batches()
 
    def Fee(self):
        raise NotImplementedError
 
    def available_batches(self):
        raise NotImplementedError
 
    def __repr__(self):
        return 'Fee : {0.fee} | Batches Available : {0.batches}'.format(self)
 
class DSA(Course):
    """Class for Data Structures and Algorithms"""
    def Fee(self):
        self.fee = 8000
 
    def available_batches(self):
        self.batches = 5
 
    def __str__(self):
        return "DSA"
 
class SDE(Course):
    """Class for Software Development Engineer"""
    def Fee(self):
        self.fee = 10000
 
    def available_batches(self):
        self.batches = 4
 
    def __str__(self):
        return "SDE"
 
class STL(Course):
    """Class for Standard Template Library"""
    def Fee(self):
        self.fee = 5000
 
    def available_batches(self):
        self.batches = 7
 
    def __str__(self):
        return "STL"

class ComplexCourse:
    def __repr__(self):
        return 'Fee : {0.fee} | available_batches: {0.batches}'.format(self)

class Complexcourse(ComplexCourse):
    def Fee(self):
        self.fee = 7000
 
    def available_batches(self):
        self.batches = 6

def construct_course(cls):
    course = cls()
    course.Fee()
    course.available_batches()
    return course    # return the course object

if __name__ == "__main__":
    main()
