#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Factory Method

It is a Creational Design Pattern that allows an interface or a class to create an object, but lets subclasses decide
which class or object to instantiate. Using the Factory method, we have the best ways to create an object. Here, objects
are created without exposing the logic to the client, and for creating the new type of object, the client uses the
same common interface.
 
Problems we face without Factory Method:
Imagine you are having your own startup which provides ridesharing in different parts of the country. The initial version of the app only provides Two-Wheeler ridesharing but as time passes, your app becomes popular and now you want to add Three and Four-Wheeler ridesharing also. 
It's a piece of great news! but what about the software developers of your startup. They have to change the whole code because now most part of the code is coupled with the Two-Wheeler class and developers have to make changes to the entire codebase. 
After being done with all these changes, either the developers end with the messy code or with the resignation letter.

Its solution is to replace the straightforward object construction calls with calls to the special factory method. Actually,
there will be no difference in the object creation but they are being called within the factory method.

For example Our Two_Wheeler, Three_Wheeler, and Four_wheeler classes should implement the ridesharing interface which will declare a method called a ride. Each class will implement this method uniquely.

.. _PEP 484:
    https://www.python.org/dev/peps/pep-0484/

.. _Google Python Style Guide:
    http://google.github.io/styleguide/pyguide.html

.. _Original source:
    https://www.geeksforgeeks.org/python-design-patterns/
"""

def main() -> None:
    """main function"""
    # main method to call others
    f = FrenchLocalizer()
    e = EnglishLocalizer()
    s = SpanishLocalizer()
 
    # list of strings
    message = ["car", "bike", "cycle"]
 
    for msg in message:
        print(f.localize(msg))
        print(e.localize(msg))
        print(s.localize(msg)) 

    f = Factory("French")
    e = Factory("English")
    s = Factory("Spanish")
 
    message = ["car", "bike", "cycle"]
 
    for msg in message:
        print(f.localize(msg))
        print(e.localize(msg))
        print(s.localize(msg))

    return None  

# Python Code for Object
# Oriented Concepts without
# using Factory method

class FrenchLocalizer:
    """ it simply returns the french version """
    def __init__(self):
        self.translations = {"car": "voiture", "bike": "bicyclette",
                             "cycle":"cyclette"}
    def localize(self, msg):
        """change the message using translations"""
        return self.translations.get(msg, msg)

class SpanishLocalizer:
    """it simply returns the spanish version"""
    def __init__(self):
        self.translations = {"car": "coche", "bike": "bicicleta",
                             "cycle":"ciclo"}
 
    def localize(self, msg):
        """change the message using translations"""
        return self.translations.get(msg, msg)

class EnglishLocalizer:
    """Simply return the same message"""
    def localize(self, msg):
        return msg

# Python Code for factory method
# it comes under the creational
# Design Pattern

class FrenchLocalizer:
    """ it simply returns the french version """
    def __init__(self):
        self.translations = {"car": "voiture", "bike": "bicyclette",
                             "cycle":"cyclette"}
 
    def localize(self, msg):
        """change the message using translations"""
        return self.translations.get(msg, msg)

class SpanishLocalizer:
    """it simply returns the spanish version"""
    def __init__(self):
        self.translations = {"car": "coche", "bike": "bicicleta",
                             "cycle":"ciclo"}

    def localize(self, msg):
        """change the message using translations"""
        return self.translations.get(msg, msg)
 
class EnglishLocalizer:
    """Simply return the same message"""
    def localize(self, msg):
        return msg
 
def Factory(language ="English"):
    """Factory Method"""
    localizers = {
        "French": FrenchLocalizer,
        "English": EnglishLocalizer,
        "Spanish": SpanishLocalizer,
    }
    return localizers[language]()
 
if __name__ == "__main__":
    main()
