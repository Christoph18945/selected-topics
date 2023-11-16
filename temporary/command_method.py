#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""

Command Method is Behavioral Design Pattern that encapsulates a request as an object, thereby allowing for the parameterization of clients with different requests and the queuing or logging of requests. Parameterizing other objects with different requests in our analogy means that the button used to turn on the lights can later be used to turn on stereo or maybe open the garage door. It helps in promoting the “invocation of a method on an object” to full object status. Basically, it encapsulates all the information needed to perform an action or trigger an event.



.. _PEP 484:
    https://www.python.org/dev/peps/pep-0484/

.. _Google Python Style Guide:
    http://google.github.io/styleguide/pyguide.html

.. _Original source:
    https://www.geeksforgeeks.org/python-design-patterns/
"""

# Problem without using Command Method
# Imagine you are working on a code editor. Your current task is to add the new buttons in the toolbar of the editor for various different operations. It’s definitely easy to create a single Button Class that can be used for the buttons. As we know that all the buttons used in the editor look similar, so what should we do? Should we create a lot of sub-classes for each place where the button is used?

# Solution Using Command Method
# Let’s have a look at the solution for the above-described problem. It’s always a good idea to divide the software into different layers which helps in easy coding as well as debugging. The command pattern suggests that objects shouldn’t send these requests directly. Instead, you should extract all of the request details, such as the object being called, the name of the method and the list of arguments into a separate command class with a single method that triggers this request.

"""Use built-in abc to implement Abstract classes and methods"""
from abc import ABC, abstractmethod
  
"""Class Dedicated to Command"""
class Command(ABC):
      
    """constructor method"""
    def __init__(self, receiver):
        self.receiver = receiver
      
    """process method"""
    def process(self):
        pass
  
"""Class dedicated to Command Implementation"""
class CommandImplementation(Command):
      
    """constructor method"""
    def __init__(self, receiver):
        self.receiver = receiver
  
    """process method"""
    def process(self):
        self.receiver.perform_action()
  
"""Class dedicated to Receiver"""
class Receiver:
      
    """perform-action method"""
    def perform_action(self):
        print('Action performed in receiver.')
  
"""Class dedicated to Invoker"""
class Invoker:
      
    """command method"""
    def command(self, cmd):
        self.cmd = cmd
  
    """execute method"""
    def execute(self):
        self.cmd.process()
  
"""main method"""
if __name__ == "__main__":
      
    """create Receiver object"""
    receiver = Receiver()
    cmd = CommandImplementation(receiver)
    invoker = Invoker()
    invoker.command(cmd)
    invoker.execute()

