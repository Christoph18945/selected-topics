#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Example of Calling values by reference and value.

.. _PEP 484:
    https://www.python.org/dev/peps/pep-0484/

.. _Google Python Style Guide:
    http://google.github.io/styleguide/pyguide.html

.. _Original source:
    https://www.geeksforgeeks.org/is-python-call-by-reference-or-call-by-value/  
"""

def main() -> None:
    """driver code"""
    # call by value
    value_1: str = "This is a Teststring"
    call_by_value(value_1)
    print(f"Outside {call_by_value.__name__} function: {value_1}")
    # call by reference
    list_1 = [10,20,30,40]
    call_by_reference(list_1)
    print(f"Outside {call_by_reference.__name__} function: {list_1}")
    return None

def call_by_value(value_1: str) -> str:
    """Example call by value.

    Python utilizes a system, which is known as “Call by
    Object Reference” or “Call by assignment”. In the event
    that you pass arguments like whole numbers, strings or
    tuples to a function, the passing is like call-by-value
    because you can not change the value of the immutable
    objects being passed to the function.

    Args:
        value_1 (str): Plain text.

    Returns:
        str: The return value is a text string.
    """
    value_1 = "Another random test string."
    print(f"Inside {call_by_value.__name__} function: {value_1}")
    return value_1

def call_by_reference(my_list: list) -> list:
    """Example call by reference.

    Whereas passing
    mutable objects can be considered as call by reference
    because when their values are changed inside the function,
    then it will also be reflected outside the function.

    Args:
        my_list (list): Input list.

    Returns:
        list: Return called list.
    """
    my_list.append([50,60,70])
    print(f"Inside {call_by_reference.__name__} function: {my_list}")
    return list

if __name__ == "__main__":
    main()
