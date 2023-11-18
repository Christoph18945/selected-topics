#!/usr/bin/python3
# -*- coding: utf-8 -*-

import math
from typing import Literal

def main() -> None:
    """main function"""
    accepts_only_four(4)   # OK
    accepts_only_four(19)  # Rejected
    return None

def accepts_only_four(x: Literal[4]) -> None:
    """demonstrate Literal type"""
    pass

class Calculations:
    """Calculations class"""
    def __init__(self):
        """class constructor"""
        pass

    def calc_square(self, num_elem: int) -> (float | Literal[0]):
        """calculate the square of two integers"""
        res: int = 0
        for i in range(num_elem):
            res += math.sqrt(i)
        return res

if __name__ == "__main__":
    main()