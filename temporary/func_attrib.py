#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Module demonstrates function attributes.

.. _PEP 484:
    https://www.python.org/dev/peps/pep-0484/

.. _Google Python Style Guide:
    http://google.github.io/styleguide/pyguide.html
"""

def grow_list(val: None = None, my_list: list = None) -> list:
    """Appending values to a list.

    Args:
        param_func (Any): Returns result.

    Returns:
        function: Return debugger function.
    """
    if my_list:
        my_list.append(val)
    else:
        my_list = [val]
    
    return my_list

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