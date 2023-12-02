#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Generic class example

.. _PEP 484:
    https://www.python.org/dev/peps/pep-0484/

.. _Google Python Style Guide:
    http://google.github.io/styleguide/pyguide.html

.. _Original source:
    https://www.geeksforgeeks.org/python-design-patterns/
"""

from logging import Logger
from typing import TypeVar, Generic


def main():
    """main function"""
    lv0 = LoggedVar(1, "Chris", None)
    lv1 = LoggedVar(2.4, "Chris", None)

T = TypeVar("T")

class LoggedVar(Generic[T]):
    def __init__(self, value: T, name: str, logger: Logger) -> None:
        self.name = name
        self.logger = logger
        self.value = value

    def set(self, new: T) -> None:
        self.log("Set " + repr(self.value))
        self.value = new
    
    def get(self) -> T:
        self.log("Get " + repr(self.value))
        return self.value
    
    def log(self, message: str) -> None:
        self.logger.info("%s : %s", self.name, message)

if __name__ == "__main__":
    main()