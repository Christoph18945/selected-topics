#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Descripe abstract datatype protocl with a list example.


"""

from typing import Protocol

def main():
    """main function"""

    values = [1,2,3]
    iterate_over_length(values)

# Protocol is a class that do not declare functions
# but does not implement them:
# https://docs.python.org/3/library/collections.abc.html
class SizedIterable(Protocol):
    """SizedIterable"""
    def __len__(self):
        """Inbuilt len method must be supported."""
        pass

    def __getitem__(self, i: int):
        """Inbuilt getitem is predefined"""
        pass

def iterate_over_length(obj: SizedIterable) -> None:
    """Iterate over list."""
    for i in range(len(obj)):
        print(obj[i])
    return None

if __name__ == "__main__":
    main()