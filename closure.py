#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Closure example

Demonstration of closures: Nested function that allows
access variables of the outer function even after the
outer function is already closed.

.. _PEP 484:
    https://www.python.org/dev/peps/pep-0484/

.. _Google Python Style Guide:
    http://google.github.io/styleguide/pyguide.html
"""

import time

def main() -> None:
    """driver code"""
    outer_function("Hello World!")
    return None

def outer_function(msg) -> None:
    """The outer function.

    Args:
        msg (Any): Message as plain text.

    Returns:
        function: Return the inner_function.
    """
    outer_msg = "Outer: " + msg
    print(outer_msg)
    current_time = time.time()
    print(current_time)

    def inner_function() -> None:
        """Debug function.

        Returns:
            None: Print results.
        """
        # access variable in outer_function
        print("Inner: '" + outer_msg + "'")
        print("Current time: ", current_time)
    
    return inner_function()

if __name__ == "__main__":
    main()
