#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""callback example"""

from typing import Any


def main() -> None:
    """main function"""
    num: tuple = (8, 5)
    ans: object = caller(called, num)
    print("Multiplication =", ans)
    return None

def called(n: tuple) -> int:
    """called function"""
    return n[0]*n[1]

def caller(func: Any, n: object) -> object:
    """caller function"""
    return func(n)

if __name__ == "__main__":
    main()
