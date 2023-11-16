#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Example forusing keyword arguments.

A quick overview:
    normal args: *ARGS;
    default args: **KWARGS
    *ARGS: tuple
    **KWARGS: dict

.. _PEP 484:
    https://www.python.org/dev/peps/pep-0484/    

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

"""

import matplotlib.pyplot as plt

def plot_my_lists(list_x, list_y, **kwargs) -> None:
    """Plot values in a list as datapoints in a graph.

    Args:
        list_x (int): Data array.
        list_y (str): Data array.
        **kwargs (dict[str,Any]): Map with keywords and values. 

    Returns:
        None: Prints out results.
    """
    print(list_x, type(list_x))
    print(list_y, type(list_y))
    print(plt.scatter(list_x, list_y, **kwargs))
    # print(plt.show())

def my_function_1(a, *args, x=2, y=3, z=4, **kwargs) -> None:
    """Print out function values, arguments and keyword arguments.

    Args:
        a (int): The first parameter.
        *args (tuple): A tuple with arguments contained.
        x (int): 
        y (int):  
        z (int): 

    Returns:
        None: Print out results.
    """
    print(args, type(args))
    print(kwargs, type(kwargs))
    print(f'a: {a}, x: {x}, y: {y} , z: {z}, args: {args}, kwargs: {kwargs}')

def my_function_2(*args, **kwargs) -> None:
    """Print out values of arguments and keyword arguments.

    Args:
        *args (tuple): A tuple with arguments contained.
        **kwargs (dict[str,Any]): Map with keywords and values.

    Returns:
        None: Prints out results.
    """    
    print(args, type(args))
    print(kwargs, type(kwargs))
    print(f'args: {args}, kwargs: {kwargs}')

def my_function_3(val_a, *args, **kwargs) -> None:
    """Get values of args and kwargs plus type.

    Args:
        a (int): The first parameter.
        *args (str): The second parameter.
        x (int): 
        y (int):  
        z (int): 

    Returns:
        None: Prints out results.
    """     
    print(val_a)
    val_a *= 2
    print(val_a)
    print(args, type(args))
    print(kwargs, type(kwargs))
    print(f'args: {args}, kwargs: {kwargs}')

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