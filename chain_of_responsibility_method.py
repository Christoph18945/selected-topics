#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Chain of Responsibility Method

It is Behavioral design pattern and it is the object-oriented version of if … elif … elif … else and make us
capable to rearrange the condition-action blocks dynamically at the run-time. It allows us to pass the requests
along the chain of handlers. The processing is simple, whenever any handler received the request it has two
choices either to process it or pass it to the next handler in the chain. 

This pattern aims to decouple the senders of a request from its receivers by allowing the request to move through chained receivers until it is handled. 

Advantages
Single Responsibility Principle: It's easy to decouple the classes here that invoke operations from classes that perform operations.
Open/Closed principle: We can introduce the new code classes without breaking th existing client code.
Increases Flexibility: While giving the responsibilities to the objects, it increases the flexibility of the code.

Disadvantages
Unassured about request: This method doesn't provide any assurance whether the object will be received or not.
Spotting characteristics: Due to debugging, it becomes difficult task to observe the characteristics of operations.
Depreciated System Performance: It might affect the system's performance due to continuous cycle calls

Applicability
Processing several handlers in order: Chain of responsibility method helps very much when it is required to process several handlers in a particular order because the linking is possible in any order
Decoupling requests: This method is generally used when you want to decouple the request's sender and receiver.
Unspecified handlers: When you don't want to specify handlers in the code, it is always preferred to use the Chain of Responsibility.

.. _PEP 484:
    https://www.python.org/dev/peps/pep-0484/

.. _Google Python Style Guide:
    http://google.github.io/styleguide/pyguide.html

.. _Original source:
    https://www.geeksforgeeks.org/python-design-patterns/
"""

def main() -> None:
    """main function"""
    """Create a client object"""
    user = User()
    """Create requests to be processed"""
    string = "GeeksforGeeks"
    requests = list(string)
    """Send the requests one by one, to handlers as per the sequence of handlers defined in the Client class"""
    user.agent(requests)
    return None

class AbstractHandler(object):
    """Parent class of all concrete handlers"""
    def __init__(self, nxt):
        """change or increase the local variable using nxt"""
        self._nxt = nxt
 
    def handle(self, request):
        """It calls the processRequest through given request"""
        handled = self.processRequest(request)
        """case when it is not handled"""
        if not handled:
            self._nxt.handle(request)
 
    def processRequest(self, request):
        """throws a NotImplementedError"""
        raise NotImplementedError('First implement it !')

class FirstConcreteHandler(AbstractHandler):
    """Concrete Handler # 1: Child class of AbstractHandler"""
    def processRequest(self, request):
        '''return True if request is handled '''
        if 'a' < request <= 'e':
            print("This is {} handling request '{}'".format(self.__class__.__name__, request))
            return True

class SecondConcreteHandler(AbstractHandler):
    """Concrete Handler # 2: Child class of AbstractHandler"""
    def processRequest(self, request):
        '''return True if the request is handled'''
        if 'e' < request <= 'l':
            print("This is {} handling request '{}'".format(self.__class__.__name__, request))
            return True

class ThirdConcreteHandler(AbstractHandler):
    """Concrete Handler # 3: Child class of AbstractHandler"""
    def processRequest(self, request):
        '''return True if the request is handled'''
        if 'l' < request <= 'z':
            print("This is {} handling request '{}'".format(self.__class__.__name__, request))
            return True

class DefaultHandler(AbstractHandler):
    """Default Handler: child class from AbstractHandler"""
    def processRequest(self, request):
        """Gives the message that the request is not handled and returns true"""
        print("This is {} telling you that request '{}' has no handler right now.".format(self.__class__.__name__,                                                                           request))
        return True

class User:
    """User Class"""
    def __init__(self):
        """Provides the sequence of handles for the users"""
        initial = None
        self.handler = FirstConcreteHandler(SecondConcreteHandler(ThirdConcreteHandler(DefaultHandler(initial))))
 
    def agent(self, user_request):
        """Iterates over each request and sends them to specific handles"""
        for request in user_request:
            self.handler.handle(request)

if __name__ == "__main__":
    main()
