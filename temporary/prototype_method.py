#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Prototype Method is a Creational Design Pattern which aims to reduce the number of classes used for an application. It allows you to copy existing objects independent of the concrete implementation of their classes. Generally, here the object is created by copying a prototypical instance during run-time. 
It is highly recommended to use Prototype Method when the object creation is an expensive task in terms of time and usage of resources and already there exists a similar object. This method provides a way to copy the original object and then modify it according to our needs.

Problems we face without Prototype Method
Suppose we have a Shape class that produces different shapes such as circle, rectangle, square, etc and we already have an object of it. Now we want to create the exact copy of this object. How an ordinary developer will go? 
He/She will create a new object of the same class and will apply all the functionalities of the original objects and copy their values. But we can not copy each and every field of the original object as some may be private and protected and are not available from the outside of the object itself. 
Problems are not over here! you also become dependent on the code of other class which is certainly not a good practice in Software Development.

For better understanding, let’s understand the example of Courses At GeeksforGeeks that provides courses like SDE, DSA, STL, etc. Creating objects for similar courses, again and again, is not a good task to utilize the resources in a better way.

Less number of SubClasses : All the other Creational Design Patterns provides a lot of new subClasses which are definitely not easy to handle when we are working on a large project. But using Prototype Design Pattern, we get rid of this.
Provides varying values to new objects: All the highly dynamic systems allows you to define new behavior through object composition by specifying values for an object’s variables and not by defining new classes.
Provides varying structure to new objects: Generally all the applications build objects from parts and subparts. For convenience, such applications often allows you instantiate complex, user-defined structures to use a specific subcircuit again and again.
Disadvantages
Abstraction: It helps in achieving the abstraction by hiding the concrete implementation details of the class.
Waste of resources at lower level: It might be proved as the overkill of resources for a project that uses very few objects
Applicability
Independency from Concrete Class: Prototype method provides the way to implement the new objects without depending upon the concrete implementation of the class.
Recurring problems : Prototype method is also used to solve the recurring and complex problems of the software development.

.. _PEP 484:
    https://www.python.org/dev/peps/pep-0484/

.. _Google Python Style Guide:
    http://google.github.io/styleguide/pyguide.html

.. _Original source:
    https://www.geeksforgeeks.org/python-design-patterns/
"""

# Solution by Prototype Method:
# To deal with such problems, we use the Prototype method. We would create separate classes for Courses_At_GFG and Course_At_GFG_Cache which will help us in creating the exact copy of already existing object with the same field properties. This method delegates the cloning process to the actual objects that are being cloned. Here we declare a common interface or class which supports object cloning which allows us to clone the object without coupling our code to the class of that method. 
# An object that supports cloning is called as Prototype.

# import the required modules
 
from abc import ABCMeta, abstractmethod
import copy
 
 
# class - Courses at GeeksforGeeks
class Courses_At_GFG(metaclass = ABCMeta):
     
    # constructor
    def __init__(self):
        self.id = None
        self.type = None
 
    @abstractmethod
    def course(self):
        pass
 
    def get_type(self):
        return self.type
 
    def get_id(self):
        return self.id
 
    def set_id(self, sid):
        self.id = sid
 
    def clone(self):
        return copy.copy(self)
 
# class - DSA course
class DSA(Courses_At_GFG):
    def __init__(self):
        super().__init__()
        self.type = "Data Structures and Algorithms"
 
    def course(self):
        print("Inside DSA::course() method")
 
# class - SDE Course
class SDE(Courses_At_GFG):
    def __init__(self):
        super().__init__()
        self.type = "Software Development Engineer"
 
    def course(self):
        print("Inside SDE::course() method.")
 
# class - STL Course
class STL(Courses_At_GFG):
    def __init__(self):
        super().__init__()
        self.type = "Standard Template Library"
 
    def course(self):
        print("Inside STL::course() method.")
 
# class - Courses At GeeksforGeeks Cache
class Courses_At_GFG_Cache:
     
    # cache to store useful information
    cache = {}
 
    @staticmethod
    def get_course(sid):
        COURSE = Courses_At_GFG_Cache.cache.get(sid, None)
        return COURSE.clone()
 
    @staticmethod
    def load():
        sde = SDE()
        sde.set_id("1")
        Courses_At_GFG_Cache.cache[sde.get_id()] = sde
 
        dsa = DSA()
        dsa.set_id("2")
        Courses_At_GFG_Cache.cache[dsa.get_id()] = dsa
 
        stl = STL()
        stl.set_id("3")
        Courses_At_GFG_Cache.cache[stl.get_id()] = stl
 
# main function
if __name__ == '__main__':
    Courses_At_GFG_Cache.load()
 
    sde = Courses_At_GFG_Cache.get_course("1")
    print(sde.get_type())
 
    dsa = Courses_At_GFG_Cache.get_course("2")
    print(dsa.get_type())
 
    stl = Courses_At_GFG_Cache.get_course("3")
    print(stl.get_type())


