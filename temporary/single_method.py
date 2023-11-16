#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
What is Singleton Method in Python
Singleton Method is a type of Creational Design pattern and is one of the simplest design patterns00 available to us.
It is a way to provide one and only one object of a particular type. It involves only one class to create methods and specify the objects. 
Singleton Design Pattern can be understood by a very simple example of Database connectivity. When each object creates a unique Database
Connection to the Database, it will highly affect the cost and expenses of the project. So, it is always better to make a single connection
rather than making extra irrelevant connections which can be easily done by Singleton Design Pattern.





.. _PEP 484:
    https://www.python.org/dev/peps/pep-0484/

.. _Google Python Style Guide:
    http://google.github.io/styleguide/pyguide.html

.. _Original source:
    https://www.geeksforgeeks.org/python-design-patterns/
"""

class OnlyOne:
    """
    Because the inner class is named with a double underscore, it is private so
    the user cannot directly access it. The inner class contains all the methods
    that you would normally put in the class if it weren’t going to be a
    singleton, and then it is wrapped in the outer class which controls creation
    by using its constructor. The first time you create an OnlyOne, it
    initializes instance, but after that it just ignores you. Add Comment
    Access comes through delegation, using the __getattr__( ) method to
    redirect calls to the single instance. You can see from the output that even
    though it appears that multiple objects have been created, the same
    __OnlyOne object is used for both. The instances of OnlyOne are
    distinct but they all proxy to the same __OnlyOne object. Add Comment
    Note that the above approach doesn’t restrict you to creating only one
    object. This is also a technique to create a limited pool of objects. In that
    situation, however, you can be confronted with the problem of sharing
    objects in the pool. If this is an issue, you can create a solution involving a
    check-out and check-in of the shared objects. Add Comment
    """
    class __OnlyOne:
        def __init__(self, arg):
            self.val = arg
        
        def __str__(self):
            return 'self' + self.val
    
    instance = None
    def __init__(self, arg):
        if not OnlyOne.instance:
            OnlyOne.instance = OnlyOne.__OnlyOne(arg)
        else:
            OnlyOne.instance.val = arg
    
    def __getattr__(self, name):
        return getattr(self.instance, name)
    
class Borg:
    """
    Alex Martelli makes the observation that what we really want with a
    Singleton is to have a single set of state data for all objects. That is, you
    could create as many objects as you want and as long as they all refer to
    the same state information then you achieve the effect of Singleton. He
    accomplishes this with what he calls the Borg9, which is accomplished by
    setting all the __dict__s to the same static piece of storage:    
    """
    _shared_state = {}
    def __init__(self):
        self.__dict__ = self._shared_state

class Singleton(Borg):
    
    def __init__(self, arg):
        Borg.__init__(self)
        self.val = arg
    
    def __str__(self): return self.val 

class SingletonDecorator:
    """
    Two other interesting ways to define singleton10 include wrapping a class
    and using metaclasses. The first approach could be thought of as a class
    decorator (decorators will be defined later in the book), because it takes
    the class of interest and adds functionality to it by wrapping it in another
    class: 
    """
    def __init__(self,klass):
        self.klass = klass
        self.instance = None
    
    def __call__(self,*args,**kwds):
        if self.instance == None:
            self.instance = self.klass(*args,**kwds)
        return self.instance 

class SingletonMetaClass(type):
    """
    The second approach uses metaclasses, a topic I do not yet understand but
    which looks very interesting and powerful indeed (note that Python 2.2
    has improved/simplified the metaclass syntax, and so this example may
    change): 
    """
    def __init__(cls,name,bases,dict):
        super(SingletonMetaClass,cls)\
        .__init__(name,bases,dict)

        original_new = cls.__new__
        
        def my_new(cls,*args,**kwds):
            if cls.instance == None:
                cls.instance = \
                original_new(cls,*args,**kwds)
            return cls.instance

        cls.instance = None
        cls.__new__ = staticmethod(my_new)

class bar(object):
    __metaclass__ = SingletonMetaClass
    def __init__(self,val):
        self.val = val
    def __str__(self):
        return 'self' + self.val 





# Singleton Borg pattern
# Method 1: Monostate/Borg Singleton Design pattern
# Singleton behavior can be implemented by Borg’s pattern but instead of having only one instance of the class, there are multiple instances that share the same state. Here we don’t focus on the sharing of the instance identity instead we focus on the sharing state. 
class Borg:
 
    # state shared by each instance
    __shared_state = dict()
 
    # constructor method
    def __init__(self):
 
        self.__dict__ = self.__shared_state
        self.state = 'GeeksforGeeks'
 
    def __str__(self):
 
        return self.state
 
 
# main method
if __name__ == "__main__":
 
    person1 = Borg()    # object of class Borg
    person2 = Borg()    # object of class Borg
    person3 = Borg()    # object of class Borg
 
    person1.state = 'DataStructures'  # person1 changed the state
    person2.state = 'Algorithms'     # person2 changed the state
 
    print(person1)    # output --> Algorithms
    print(person2)    # output --> Algorithms
 
    person3.state = 'Geeks'  # person3 changed the
    # the shared state
 
    print(person1)    # output --> Geeks
    print(person2)    # output --> Geeks
    print(person3)    # output --> Geeks

# Double Checked Locking singleton pattern
import threading
 
 
class SingletonDoubleChecked(object):
 
    # resources shared by each and every
    # instance
 
    __singleton_lock = threading.Lock()
    __singleton_instance = None
 
    # define the classmethod
    @classmethod
    def instance(cls):
 
        # check for the singleton instance
        if not cls.__singleton_instance:
            with cls.__singleton_lock:
                if not cls.__singleton_instance:
                    cls.__singleton_instance = cls()
 
        # return the singleton instance
        return cls.__singleton_instance
 
 
# main method
if __name__ == '__main__':
 
    # create class X
    class X(SingletonDoubleChecked):
        pass
 
    # create class Y
    class Y(SingletonDoubleChecked):
        pass
 
    A1, A2 = X.instance(), X.instance()
    B1, B2 = Y.instance(), Y.instance()
 
    assert A1 is not B1
    assert A1 is A2
    assert B1 is B2
 
    print('A1 : ', A1)
    print('A2 : ', A2)
    print('B1 : ', B1)
    print('B2 : ', B2)

# classic implementation of Singleton Design pattern
# Creating a singleton in Python
# In the classic implementation of the Singleton Design pattern, we simply use the static method for creating the getInstance
# method which has the ability to return the shared resource. We also make use of the so-called Virtual private
# Constructor to raise the exception against it although it is not much required.
class Singleton:
 
    __shared_instance = 'GeeksforGeeks'
 
    @staticmethod
    def getInstance():
        """Static Access Method"""
        if Singleton.__shared_instance == 'GeeksforGeeks':
            Singleton()
        return Singleton.__shared_instance
 
    def __init__(self):
        """virtual private constructor"""
        if Singleton.__shared_instance != 'GeeksforGeeks':
            raise Exception("This class is a singleton class !")
        else:
            Singleton.__shared_instance = self
 
 
# main method
if __name__ == "__main__":
 
    # create object of Singleton Class
    obj = Singleton()
    print(obj)
 
    # pick the instance of the class
    obj = Singleton.getInstance()
    print(obj)