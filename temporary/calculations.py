#!/usr/bin/python3
# -*- coding: utf-8 -*-

import math

class Calculations:

    def __init__(self) -> None:
        ...

    def calc_square(self, num_elements: int) -> int:
        res = 0
        for i in range(num_elements):
            res += math.sqrt(i)
        
        return res
