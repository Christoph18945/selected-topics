#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Simulating the trash

Recycler
The nature of this problem is that the trash is thrown unclassified into a
single bin, so the specific type information is lost. But later, the specific
type information must be recovered to properly sort the trash. In the
initial solution, RTTI (described in Chapter 12 of Thinking in Java, 2nd
edition) is used. Add Comment

16 Addison-Wesley, 1999.
This is not a trivial design because it has an added constraint. That's what
makes it interesting—it's more like the messy problems you're likely to
encounter in your work. The extra constraint is that the trash arrives at
the trash recycling plant all mixed together. The program must model the
sorting of that trash. This is where RTTI comes in: you have a bunch of
anonymous pieces of trash, and the program figures out exactly what type
they are. Add Comment
# c12:recyclea:RecycleA.py
# Recycling with RTTI.
"""

from abc import abstractmethod
import math
import random
from typing import Iterator
import unittest

def main():
    unittest.main()

class Trash:
    """class trash"""
    def __init__(self, wt: float):
        self.weight = wt
    
    @abstractmethod
    def get_value(self):
        pass

    def get_weigth(self) -> float:
        return self.weight
 
    # Sums the value of Trash in a bin:
    def sum_value(iterator):
        val = 0.0
        it: Trash = Trash()
        while(it.next()):
            # One kind of RTTI:
            # A dynamically-checked cast
            t: Trash = it.next()
            # Polymorphism in action:
            val += t.get_weight() * t.get_value()
            print("weight of " +
            # Using RTTI to get type
            # information about the class:
            t.getClass().getName() + " = " + t.getWeight())
            print("Total value = " + val)

class Aluminium(Trash):
    """Class Aluminium"""
    def __init__(self, wt: float):
        self.val = 1.67

    def get_value(self):
        return self.val
        
    def set_value(self, new_val: float):
        self.val = new_val

class Paper(Trash):
    """Class Paper"""
    def __init__(self, wt: float):
        self.val = 10.0

    def get_value(self):
        return self.val
        
    def set_value(self, new_val: float) -> float:
        """Set a value."""
        new_valval = new_val
        return new_valval

class Glass(Trash):
    """Class Glass"""
    def __init__(self, wt: float):
        self.val = 10.0

    def get_value(self):
        return self.val
        
    def set_value(self, new_val: float) -> float:
        """Set a specific value."""
        new_valval = new_val
        return new_valval

class RecycleA(unittest.main):
    """Class RecycleA"""
    def __init__(self):
        self.bin: list = []
        self.glassBin: list = []
        self.paperBin: list = []
        self.alBin = []
        # Fill up the Trash bin:
        for i in range(30):
            match math.random() * 3:
                case 0 :
                    bin.append(Aluminium( random() * 100))
                    break
                case 1 :
                    bin.append(Paper(random() * 100))
                    break
                case 2 :
                    bin.append(Glass(random() * 100))
    def test(self):
        """Testing"""
        sorter: Iterator = bin.iterator()
        # Sort the Trash:
        while(sorter.hasNext()):
            t: object = sorter.next()
            # RTTI to show class membership:
            
            t = isinstance(t, Aluminium)
            if t is True:
                self.alBin.append(t)
                
            t = isinstance(t, Paper)
            if t is True:
                self.paperBin.append(t)
            
            t = isinstance(t, Glass)
            if t is True:
                self.glassBin.append(t)
            
            Trash.sum_value(self.alBin.iterator())
            Trash.sum_value(self.paperBin.iterator())
            Trash.sum_value(self.glassBin.iterator())
            Trash.sum_value(self.bin.iterator())

if __name__ == "__main__":
    main()
