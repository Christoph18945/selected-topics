#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Facade Method

It is a Structural Design pattern that provides a simpler unified interface to a more complex system. The word Facade
means the face of a building or particularly an outer lying interface of a complex system, consists of several sub-systems.
It is an essential part Gang of Four design patterns. It provides an easier way to access methods of the underlying systems
by providing a single entry point.

Here, we create a Facade layer that helps in communicating with subsystems easily to the clients.

Advantages
Isolation: We can easily isolate our code from the complexity of a subsystem.
Testing Process: Using Facade Method makes the process of testing comparatively easy since it has convenient methods for common testing tasks.
Loose Coupling: Availability of loose coupling between the clients and the Subsystems.

Disadvantages 
Changes in Methods: As we know that in Facade method, subsequent methods are attached to Facade layer and any change in subsequent method may brings change in Facade layer which is not favorable.
Costly process: It is not cheap to establish the Facade method in our application for the system’s reliability.
Violation of rules: There is always the fear of violation of the construction of the facade layer.

Applicability 
Providing simple Interface: One of the most important application of Facade Method is that it is used whenever you want to provide the simple interface to the complex sub-system
Division into layers: It is used when we want to provide a unique structure to a sub-system by dividing them into layers. It also leads to loose coupling between the clients and the subsystem.

.. _PEP 484:
    https://www.python.org/dev/peps/pep-0484/

.. _Google Python Style Guide:
    http://google.github.io/styleguide/pyguide.html

.. _Original source:
    https://www.geeksforgeeks.org/python-design-patterns/
"""

# Problem without using Facade Method
# Imagine we have a washing machine which can wash the clothes, rinse the clothes and spin the clothes but all the tasks separately.
# As the whole system is quite complex, we need to abstract the complexities of the subsystems. We need a system that can automate the
# whole task without the disturbance or interference of us. 

# Solution using Facade Method
# To solve the above-described problem, we would like to hire the Facade Method. It will help us to hide or abstract the complexities
# of the subsystems as follows. 

def main() -> None:
    """main function"""
    washingMachine = WashingMachine()
    washingMachine.startWashing()
    return None

class Washing:
    '''Subsystem # 1'''
    def wash(self):
        print("Washing...")

class Rinsing:
    '''Subsystem # 2'''
    def rinse(self):
        print("Rinsing...")

class Spinning:
    '''Subsystem # 3'''
    def spin(self):
        print("Spinning...")

class WashingMachine:
    '''Facade'''
    def __init__(self):
        self.washing = Washing()
        self.rinsing = Rinsing()
        self.spinning = Spinning()
  
    def startWashing(self):
        self.washing.wash()
        self.rinsing.rinse()
        self.spinning.spin()

if __name__ == "__main__":
    main()
