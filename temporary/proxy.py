#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Simple implementation of a proxy pattern

It isn’t necessary that Implementation have the same interface as
Proxy; as long as Proxy is somehow “speaking for” the class that it is
referring method calls to then the basic idea is satisfied (note that this
statement is at odds with the definition for Proxy in GoF). However, it is
convenient to have a common interface so that Implementation is
forced to fulfill all the methods that Proxy needs to call.
Of course, in Python we have a delegation mechanism built in, so it makes
the Proxy even simpler to implement:
"""

import string
import sys


class Implementation2:

    def f(self):
        print("Implementation.f()")
 
    def g(self):
        print("Implementation.g()")

    def h(self):
        print("Implementation.h()")

class Proxy2:

    def __init__(self):
        self.__implementation = Implementation2()

    def __getattr__(self, name):
        """
        The beauty of using __getattr__( ) is that Proxy2 is completely
        generic, and not tied to any particular implementation (in Java, a rather
        complicated “dynamic proxy” has been invented to accomplish this same
        thing).
        """
        return getattr(self.__implementation, name)

p = Proxy2()
p.f(); p.g(); p.h()


# State
# The State pattern adds more implementations to Proxy, along with a way
# to switch from one implementation to another during the lifetime of the
# surrogate:

# # Simple demonstration of the State pattern.

class State_d:

    def __init__(self, imp):
        self.__implementation = imp
 
    def changeImp(self, newImp):
        self.__implementation = newImp
 
    # Delegate calls to the implementation:
    def __getattr__(self, name):
        return getattr(self.__implementation, name)
    
class Implementation1:

    def f(self):
        print("Fiddle de dum, Fiddle de dee,")
 
    def g(self):
        print("Eric the half a bee.")
 
    def h(self):
        print("Ho ho ho, tee hee hee,")

class Implementation2:
    
    def f(self):
        print("We're Knights of the Round Table.")
 
    def g(self):
        print("We dance whene'er we're able.")
 
    def h(self):
        print("We do routines and chorus scenes")

    def run(b):
        b.f()
        b.g()
        b.h()
        b.g()
        b = State_d(Implementation1())
        
    run(b)
    b.changeImp(Implementation2())
    run(b)

# You can see that the first implementation is used for a bit, then the second
# implementation is swapped in and that is used.
# The difference between Proxy and State is in the problems that are solved.
# The common uses for Proxy as described in Design Patterns are: Add
# Comment
# 
# 1. Remote proxy. This proxies for an object in a different address
# space. A remote proxy is created for you automatically by the RMI
# compiler rmic as it creates stubs and skeletons.
# 
# 2. Virtual proxy. This provides “lazy initialization” to create
# expensive objects on demand.
# 
# 3. Protection proxy. Used when you don’t want the client
# programmer to have full access to the proxied object. 
# 
# 4. Smart reference. To add additional actions when the proxied
# object is accessed. For example, or to keep track of the number of
# references that are held for a particular object, in order to
# implement the copy-on-write idiom and prevent object aliasing. A
# simpler example is keeping track of the number of calls to a
# particular method.
# 
# You could look at a Python reference as a kind of protection proxy, since it
# controls access to the actual object on the heap (and ensures, for example,
# that you don’t use a null reference).
# [[ Rewrite this: In Design Patterns, Proxy and State are not seen as
# related to each other because the two are given (what I consider
# arbitrarily) different structures. State, in particular, uses a separate
# implementation hierarchy but this seems to me to be unnecessary unless
# you have decided that the implementation is not under your control
# (certainly a possibility, but if you own all the code there seems to be no
# reason not to benefit from the elegance and helpfulness of the single base
# class). In addition, Proxy need not use the same base class for its
# implementation, as long as the proxy object is controlling access to the
# object it “fronting” for. Regardless of the specifics, in both Proxy and
# State a surrogate is passing method calls through to an implementation
# object.]]]

# StateMachine
# While State has a way to allow the client programmer to change the
# implementation, StateMachine imposes a structure to automatically
# change the implementation from one object to the next. The current
# implementation represents the state that a system is in, and the system
# behaves differently from one state to the next (because it uses State).
# Basically, this is a “state machine” using objects.
# The code that moves the system from one state to the next is often a
# Template Method, as seen in the following framework for a basic state
# machine.
# Each state can be run( ) to perform its behavior, and (in this design) you
# can also pass it an “input” object so it can tell you what new state to move
# to based on that “input”. The key distinction between this design and the
# next is that here, each State object decides what other states it can move
# to, based on the “input”, whereas in the subsequent design all of the state
# transitions are held in a single table. Another way to put it is that here,
# each State object has its own little State table, and in the subsequent
# design there is a single master state transition table for the whole system.
#

# A State has an operation, and can be moved
# into the next State given an Input:
class State:
    """
    This class is clearly unnecessary, but it allows us to say that something is a
    State object in code, and provide a slightly different error message when
    all the methods are not implemented. We could have gotten basically the
    same effect by saying:
    class State: pass
    because we would still get exceptions if run( ) or next( ) were called for a
    derived type, and they hadn’t been implemented.    
    """
    def run(self):
        assert 1, "run not implemented"

    def next(self, input):
        assert 1, "next not implemented"


# The StateMachine keeps track of the current state, which is initialized
# by the constructor. The runAll( ) method takes a list of Input objects.
# This method not only moves to the next state, but it also calls run( ) for
# each state object – thus you can see it’s an expansion of the idea of the
# State pattern, since run( ) does something different depending on the
# state that the system is in.

# # Takes a list of Inputs to move from State to
# # State using a template method.
class StateMachine:
    
    def __init__(self, initialState):
        self.currentState = initialState
        self.currentState.run()
 
    # Template method:
    def runAll(self, inputs):
        """run_all() is a template method as well. This
        is typically but it is not required
        """
        for i in inputs:
            print(i)
            self.currentState = self.currentState.next(i)
            self.currentState.run()

# The StateMachine class simply defines all the possible states as static
# objects, and also sets up the initial state. The UnitTest creates a
# MouseTrap and then tests it with all the inputs from a
# MouseMoveList.
# While the use of if statements inside the next( ) methods is perfectly
# reasonable, managing a large number of these could become difficult.
# Another approach is to create tables inside each State object defining the
# various next states based on the input.
# Initially, this seems like it ought to be quite simple. You should be able to
# define a static table in each State subclass that defines the transitions in
# terms of the other State objects. However, it turns out that this approach
# generates cyclic initialization dependencies. To solve the problem, I’ve had
# to delay the initialization of the tables until the first time that the next( )
# method is called for a particular State object. Initially, the next( )
# methods can appear a little strange because of this.
# The StateT class is an implementation of State (so that the same
# StateMachine class can be used from the previous example) that adds a
# Map and a method to initialize the map from a two-dimensional array.
# The next( ) method has a base-class implementation which must be
# called from the overridden derived class next( ) methods after they test
# for a null Map (and initialize it if it’s null):
# #: c04:mousetrap2:MouseTrap2Test.py
# # A better mousetrap using tables

sys.path += ['../statemachine', '../mouse']

from State import State
from StateMachine import StateMachine
from MouseAction import MouseAction

class StateT(State):
    
    def __init__(self):
        self.transitions = None
 
    def next(self, input):
        if self.transitions.has_key(input):
            return self.transitions[input]
        else:
            raise "Input not supported for current state"

class Waiting(StateT):
    
    def run(self):
        print("Waiting: Broadcasting cheese smell")
 
    def next(self, input):
        # Lazy initialization:
        if not self.transitions:
            self.transitions = {
                MouseAction.appears : MouseTrap.luring
            }
        return StateT.next(self, input)

class Luring(StateT):
 
    def run(self):
        print("Luring: Presenting Cheese, door open")
 
    def next(self, input):
        # Lazy initialization:
        if not self.transitions:
            self.transitions = {
                MouseAction.enters : MouseTrap.trapping,
                MouseAction.runsAway : MouseTrap.waiting
            }
        return StateT.next(self, input)

class Trapping(StateT):

    def run(self):
        print("Trapping: Closing door")

    def next(self, input):
        # Lazy initialization:
        if not self.transitions:
            self.transitions = {
                MouseAction.escapes : MouseTrap.waiting,
                MouseAction.trapped : MouseTrap.holding
            }
        return StateT.next(self, input)

class Holding(StateT):

    def run(self):
        print("Holding: Mouse caught")
    
    def next(self, input):
        # Lazy initialization:
        if not self.transitions:
            self.transitions = {
                MouseAction.removed : MouseTrap.waiting
            }
        return StateT.next(self, input)

class MouseTrap(StateMachine):
    
    def __init__(self):
        # Initial state
        StateMachine.__init__(self, MouseTrap.waiting)
        # Static variable initialization:
        MouseTrap.waiting = Waiting()
        MouseTrap.luring = Luring()
        MouseTrap.trapping = Trapping()
        MouseTrap.holding = Holding()
        moves = map(string.strip,
        open("../mouse/MouseMoves.txt").readlines())
        mouseMoves = map(MouseAction, moves)
        MouseTrap().runAll(mouseMoves)

# The rest of the code is identical – the difference is in the next( ) methods
# and the StateT class.
# If you have to create and maintain a lot of State classes, this approach is
# an improvement, since it’s easier to quickly read and understand the state
# transitions from looking at the table.