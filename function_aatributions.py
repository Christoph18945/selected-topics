#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Module demonstrates function attributes.

.. _PEP 484:
    https://www.python.org/dev/peps/pep-0484/

.. _Google Python Style Guide:
    http://google.github.io/styleguide/pyguide.html
"""

def main() -> None:
    """driver code"""
    print(dir(grow_list)) # return all function attributes
    print(grow_list.__name__) # return function name
    print(grow_list.__doc__) # return function docstring
    print(grow_list.__defaults__) # return all default values of function parameters    
    print(grow_list.__code__.co_argcount) # return number of arguments
    print(grow_list.__code__.co_varnames) # return all paramter names
    return None

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

if __name__ == "__main__":
    main()
