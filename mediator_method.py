#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Mediator Method

It is a Behavioral Design Pattern that allows us to reduce the unordered dependencies between the objects. In a mediator environment, objects take the help of mediator objects to communicate with each other. It reduces coupling by reducing the dependencies between communicating objects. The mediator works as a router between objects and it can have it's own logic to provide a way of communication.

Design Components:
Mediator: It defines the interface for communication between colleague objects.
Concrete Mediator: It implements the mediator interface and coordinates communication between colleague objects.
Colleague: It defines the interface for communication with other colleagues
Concrete Colleague: It implements the colleague interface and communicates with other colleagues through its mediator.
Problem Without using Mediator Method
Imagine you are going to take admission in one of the elite courses offered by GeeksforGeeks such as DSA, SDE, and STL. Initially, there are very few students who are approaching to join these courses. Initially, the developer can create separate objects and classes for the connection between the students and the courses but as the courses become famous among students it becomes hard for developers to handle such a huge number of sub-classes and their objects.

Advantages
Single Responsibility Principle: Extracting the communications between the various components is possible under Mediator Method into a single place which is easier to maintain.
Open/Closed Principle: It's easy to introduce new mediators without disturbing the existing client code.
Allows Inheritance: We can reuse the individual components of the mediators as it follows the Inheritance
Few Sub-Classes: Mediator limits the Sub-Classing as a mediator localizes the behavior that otherwise would be disturbed among the several objects.
Disadvantages
Centralization: It completely centralizes the control because the mediator pattern trades complexity of interaction for complexity in the mediator.
God Object: A Mediator can be converted into a God Object (an object that knows too much or does too much).
Increased Complexity: The structure of the mediator object may become too much complex if we put too much logic inside it.
Applicability
Reduce the number of sub-classes: When you have realized that you have created a lot of unnecessary sub-classes, then it is preferred to use the Mediator method to avoid these unnecessary sub-classes.
Air Traffic Controller: Air traffic controller is a great example of a mediator pattern where the airport control room works as a mediator for communication between different flights.

.. _PEP 484:
    https://www.python.org/dev/peps/pep-0484/

.. _Google Python Style Guide:
    http://google.github.io/styleguide/pyguide.html

.. _Original source:
    https://www.geeksforgeeks.org/python-design-patterns/
"""

# Solution using Mediator Method
# Now let us understand how a pro developer will handle such a situation using the Mediator design pattern. We can create a separate mediator class named as Course and a User Class using which we can create different objects of Course class. In the main method, we will create a separate object for each student and inside the User class, we will create the object for Course class which helps in preventing the unordered code.

def main():
    """main function"""
    mayank: User = User('Mayank') # user object
    lakshya: User = User('Lakshya') # user object
    krishna: User = User('Krishna') # user object
    mayank.send_course("Data Structures and Algorithms")
    lakshya.send_course("Software Development Engineer")
    krishna.send_course("Standard Template Library")
    return None

class Course(object):
    """Mediator class."""
    def display_course(self, user, course_name):
        print("[{}'s course ]: {}".format(user, course_name))

class User(object):
    """A class whose instances want to interact with each other."""
    def __init__(self, name: str):
        self.name: str = name
        self.course: Course = Course()

    def send_course(self, course_name: str) -> None:
        """display course data"""
        self.course.display_course(self, course_name)
        return None

    def __str__(self) -> str:
        """human-readable string"""
        return self.name

if __name__ == "__main__":
    main()
