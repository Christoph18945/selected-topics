#!/usr/bin/python3
# -*- coding: utf-8 -*-

import math
from typing import Literal

class Calculations:
    """Calculations class"""
    def __init__(self) -> None:
        """class constructor"""
        pass

    def calc_square(self, num_elem: int) -> (float | Literal[0]):
        """calculate the square of two integers"""
        res: int = 0
        for i in range(num_elem):
            res += math.sqrt(i)
        return res
