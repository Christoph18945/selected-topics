#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Generic functions.

"""

from typing import Protocol, TypeVar

def main():
    """main function"""
    print(repeat(1.0, 5))
    print(longest("christoph", "chris"))
    print(longest(1, 2))

class HasLen(Protocol):
    """"""
    def __len__(self) -> int:
        """"""
        ...

# the generic type
T1 = TypeVar("T1")
# set that a class is implemented, not how
T2 = TypeVar("T2", bound=HasLen)

# generic function:
# funcion is callable for all sorts of
# datatypes. Diff. to Any: with Any, mypy
# is deactivated and won't be linted.
def repeat(x: T1, n: int) -> list[T1]:
    """Repeat something"""
    return [x] * n

# Pass a protocol to bound certain functio nto it.
# In this case it is the len() function
def longest(x: T2, y: T2) -> T2:
    """Has longest parameter"""
    return x if len(x) >= len(y) else y

if __name__ == "__main__":
    main()