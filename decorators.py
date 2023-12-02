#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Example of Decorators.

Decorators wraps a function by anotherone. It takes
a function as an argument and returns a closure. The
closure runs the previous in function with the *args
and **kwargs arguments.

.. _PEP 484:
    https://www.python.org/dev/peps/pep-0484/

.. _Google Python Style Guide:
    http://google.github.io/styleguide/pyguide.html
"""

from functools import wraps

def main() -> None:
    """driver code"""
    calculate_sum(2,2,4)
    return None

def debug(param_func):
    """Debug function.

    Args:
        param_func (Any): Function as a parameter.

    Returns:
        function: Return debugger function.
    """
    @wraps(param_func)
    def debugger(*args, **kwargs) -> object:
        """Debugger itself.

        Args:
            param_func (Any): Returns result.

        Returns:
            function: Return debugger function.
        """
        args_values_types: list = [(a, type(a)) for a in args]
        kwargs_values_types: list = [(k, v, type(v)) for k, v in kwargs.items()]
        print(f"Args: {args_values_types}")
        print(f"Kwargs: {kwargs_values_types}")
        fn_result = param_func(*args, **kwargs)
        print(f"Function {param_func.__name__} returns: {fn_result}")
        return fn_result
    return debugger

@debug
def calculate_sum(val_a: int, val_b: int, res_c: int = 0) -> int:
    """Calculate the sum of 3 values.

    Args:
        val_a, val_b, val_c (int): Integer value of choice.

    Returns:
        int: Return the result.
    """
    res: int = val_a + val_b if res_c else 0
    return res

if __name__ == "__main__":
    main()
