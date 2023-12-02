#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Dicussion about memory management.

Covered subjects: 
"""

import random
random.seed(42)

def main():
    """main function"""

    # get memory address
    val_0: int = 10
    print_mem_address(val_0)

    # All variables have the same
    # memory adress, because this 
    # variables beloware three different
    # instances.
    # For built-in/primary datatypes this values
    # are set already in the system. When starting
    # the program, vars 0 - 100 are already located
    # at a certain address. if there are more vars with
    # same values, they all point to the same address.
    # NOTE: This counts only for small integer values!
    #       24-28 bytes are relevant for diff. memory addresses
    val_1: int = 42
    val_2: int = 42
    val_3: int = 42
    print_mem_address(val_1)
    print_mem_address(val_2)
    print_mem_address(val_3)
    # The same goes for booleans as well
    bool_0 = True
    bool_1 = True
    bool_2 = False
    bool_3 = False
    print_mem_address(bool_0)
    print_mem_address(bool_1)
    print_mem_address(bool_2)
    print_mem_address(bool_3)

    # with floats
    float_1 = 42.0
    float_2 = 42.0
    float_3 = 42.0
    print_mem_address(float_1)
    print_mem_address(float_2)
    print_mem_address(float_3)

    # NOTE: In terms of performance, there are all the same
    # memory addresses, because there is one value already
    # savd at one address

    # what about lists:
    # here different memory adresses are used.
    # This goes for all complex datatypes.
    my_list_0: list = [1,2,3]
    my_list_1: list = my_list_0
    print_mem_address(my_list_0)
    print_mem_address(my_list_1)

    # do I change content of my_ist_1 as
    # well, when I change value in
    # my_list_1 as well
    my_list_1[0] = -1
    print_mem_address(my_list_0)
    print_mem_address(my_list_1)

    # Append value here in the list
    my_list_2: list = []
    print(app_rand_value(my_list_2))

    # Cosider the next example. Not here
    # that the sq_list() function is not
    # executed on the function. New generated
    # object is located on another address in memory.
    # The original object is not manipulated. So important:
    # If new list is manipulated, save the manipulated in
    # a new object
    my_list_4: list = [1,2,3]
    my_list_5 = sq_list(my_list_4)
    print(my_list_5)

def sq_list(l) -> list:
    print_mem_address(l)
    l = [val**2 for val in l]
    print_mem_address(l)
    return l

def app_rand_value(l) -> list:
    l.append(random.randint(-100,100))
    return l

def print_mem_address(var: object) -> None:
    """Print memory address of the variable"""
    print(hex(id(var)))

if __name__ == "__main__":
    main()