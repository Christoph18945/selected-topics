#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Print out memory address of variable values.

.. _PEP 484:
    https://www.python.org/dev/peps/pep-0484/    

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html
"""

import ctypes


def main():
    """Driver code
    """
    # modules/mem_refs.py
    # memory_1: Memory = Memory()
    val: int = 10
    # print(memory_1.get_mem_addr(val))
    val1: int = 42
    val2: int = 42
    val3: int = 42
    # print(memory_1.get_mem_addr(val1))
    # print(memory_1.get_mem_addr(val2))
    # print(memory_1.get_mem_addr(val3))
    val1: float = 42.0
    val2: float = 42.0
    val3: float = 42.0
    # print(memory_1.get_mem_addr(val1))
    # print(memory_1.get_mem_addr(val2))
    # print(memory_1.get_mem_addr(val3))
    bool1: bool = True
    bool2: bool = True
    # print(memory_1.get_mem_addr(bool1))
    # print(memory_1.get_mem_addr(bool2))
    bool3: bool = False
    bool4: bool = False
    # print(memory_1.get_mem_addr(bool3))
    # print(memory_1.get_mem_addr(bool4))
    none1: None = None
    none2: None = None
    # print(memory_1.get_mem_addr(none1))
    # print(memory_1.get_mem_addr(none2))
    list1: list = [1,2,3,4,5,6,7,8,9,10]
    list2: list = list1
    # print(memory_1.get_mem_addr(list1))
    # print(memory_1.get_mem_addr(list2))
    list3: list = [1,2,3,4,5]
    list4: list = list3
    list5: list = list3
    print(ctypes.c_long.from_address(id(list3)))
    print(ctypes.c_long.from_address(id(list4)))
    print(ctypes.c_long.from_address(id(list5)))