#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Memory addresses of variables.

.. _PEP 484:
    https://www.python.org/dev/peps/pep-0484/    

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html
"""

import random

def append_random_value(full_list: list) -> None:
    """Append list with a random value.
    """
    full_list.append(random.randint(-100, 100))

def main():
    """Driver code
    """
    # modules/boolean_satisfiability_problem_checker.py
    clauses = read_clauses("data/SAT_Problem.txt")
    solution = read_solution("data/SAT_Solution.txt")
    check_satisfation(clauses,solution)

    # modules/call_by_ref_and_call_by_value.py
    # call by value
    value_1: str = "This is a Teststring"
    call_by_value(value_1)
    print(f"Outside {call_by_value.__name__} function: {value_1}")
    # call by reference
    list_1 = [10,20,30,40]
    call_by_reference(list_1)
    print(f"Outside {call_by_reference.__name__} function: {list_1}")

    # modules/closure.py
    outer_function("Hello World!")

    # modules/decorators.py
    calculate_sum(2,2,4)

    # modules/func_attrib.py
    print(dir(grow_list)) # return all function attributes
    print(grow_list.__name__) # return function name
    print(grow_list.__doc__) # return function docstring
    print(grow_list.__defaults__) # return all default values of function parameters    
    print(grow_list.__code__.co_argcount) # return number of arguments
    print(grow_list.__code__.co_varnames) # return all paramter names

    # modules/has_table.py

    # modules/keywordd_arguments.py
    my_function_1(1, 3, 4, x=13.37, b=False, c=30, d=40.5)
    my_function_2(1, 3, 4, x=13.37, b=False, c=30, d=40.5)
    my_function_3(1, 3, 4, x=13.37, b=False, c=30, d=40.5)
    list_x = [-3, -2, -1, 1, 2, 3]
    list_y = [9, 4, 1, 1, 4, 9]
    plot_my_lists(list_x, list_y, c='red')    

    # modules/knapsack_problem.py
    profit = [60, 100, 120]
    weight = [10, 20, 30]
    W = 50
    n = len(profit)
    print(knap_sack(W, weight, profit, n))    

    # modules/mem_refs_2.py
    # mem_1: Memory = Memory()
    my_int_val_1: int = 100
    my_int_val_2: int = 100
    # print(mem_1.get_mem_addr(my_int_val_1))
    # 0x1c0b01b0d50
    # print(mem_1.get_mem_addr(my_int_val_2))
    # 0x1c0b01b0d50
    my_int_val_1: int = 1000
    my_int_val_2: int = 1000
    # print(mem_1.get_mem_addr(my_int_val_1))
    # 0x1c0b2bb5e30
    # print(mem_1.get_mem_addr(my_int_val_2))
    # 0x1c0b2bb5e30
    my_list1 = []
    print(random.seed(42))
    # None
    append_random_value(my_list1)
    print(my_list1)
    # [63]












































