#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Abstract Factory Method

Abstract Factory Method is a Creational Design pattern that allows you to produce the families of related objects without
specifying their concrete classes. Using the abstract factory method, we have the easiest ways to produce a similar type of
many objects. 

It provides a way to encapsulate a group of individual factories. Basically, here we try to abstract the creation of the objects
depending on the logic, business, platform choice, etc.

Problem we face without Abstract Factory Method:
Imagine you want to join one of the elite batches of GeeksforGeeks. So, you will go there and ask about the Courses available, their
Fee structure, their timings, and other important things. They will simply look at their system and will give you all the information
you required. Looks simple? Think about the developers how they make the system so organized and how their website is so lubricative.

Developers will make unique classes for each course which will contain its properties like Fee structure, timings, and other things.
But how they will call them and how will they instantiate their objects?

Here arises the problem, suppose initially there are only 3-4 courses available at GeeksforGeeks, but later they added 5 new courses. 
So, we have to manually instantiate their objects which is not a good thing according to the developer's side. 

.. _PEP 484:
    https://www.python.org/dev/peps/pep-0484/

.. _Google Python Style Guide:
    http://google.github.io/styleguide/pyguide.html

.. _Original source:
    https://www.geeksforgeeks.org/python-design-patterns/
"""

import random

def main() -> None:
    """main function"""
    # solution without factory method
    sde: SoftwareDevelopmentEngineer = SoftwareDevelopmentEngineer() # object for SDE class
    dsa: DataStructureAlgorithm = DataStructureAlgorithm() # object for DSA class
    stl: StandardTemplateLibrary = StandardTemplateLibrary() # object for STL class 
    print(f'Name of the course is {sde} and its price is {sde.get_price()}')
    print(f'Name of the course is {dsa} and its price is {dsa.get_price()}')
    print(f'Name of the course is {stl} and its price is {stl.get_price()}')
    # solution with factory method
    course: Course_At_GFG = Course_At_GFG(random_course)
    for i in range(5):
        course.show_course()
    return None

class DataStructureAlgorithm:
    """ Class DataStructureAlgorithm"""
    def get_price(self) -> int:
        """get price"""
        return 11000
 
    def __str__(self) -> str:
        """human-readable string"""
        return "DSA"
 
class StandardTemplateLibrary:
    """Class for Standard Template Library"""
    def get_price(self) -> int:
        return 8000
 
    def __str__(self) -> str:
        return "STL"
 
class SoftwareDevelopmentEngineer:
    """Class for Software Development Engineer"""
    def get_price(self)-> int:
        return 15000
 
    def __str__(self) -> str:
        return 'SDE'

"""    
Solution by using Abstract Factory Method:
Its solution is to replace the straightforward object construction calls with calls to the special abstract
factory method. Actually, there will be no difference in the object creation but they are being called within
the factory method. 

Now we will create a unique class whose name is Course_At_GFG which will handle all the object instantiation
automatically. Now, we don't have to worry about how many courses we are adding after some time.
"""

class Course_At_GFG:
    """ GeeksforGeeks portal for courses """
    def __init__(self, courses_factory = None):
        """course factory is out abstract factory"""
        self.course_factory = courses_factory
 
    def show_course(self) -> None:
        """creates and shows courses using the abstract factory"""
        course = self.course_factory()
        print(f'We have a course named {course}')
        print(f'its price is {course.get_fee()}')
        return None

class DSA:
    """Class DSA"""
    def get_fee(self) -> int:
        """return fee for class"""
        return 11000
 
    def __str__(self) -> str:
        """human readable str"""
        return "DSA"

class STL:
    """Class Standard Template Library"""
    def get_fee(self) -> int:
        """return fee for class"""
        return 8000

    def __str__(self) -> str:
        """human-readable str"""
        return "STL"

class SDE:
    """Class for Software Development Engineer"""
    def get_fee(self) -> int:
        """get fee of class"""
        return 15000
 
    def __str__(self) -> str:
        """human readable str"""
        return 'SDE'

def random_course() -> (object | (SDE | STL | DSA)):
    """A random class for choosing the course"""
    crs: object = random.choice([SDE, STL, DSA])()
    return crs

if __name__ == "__main__":
    main()
