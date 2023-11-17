#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""special parameters
"""

import time
from calculations import Calculations

def main() -> None:
    """main function"""
    calc: Calculations = Calculations()
    start_time: float = time.perf_counter()
    for _ in range(4):
        calc.calc_square(10)

    end_time: float = time.perf_counter()
    print(f"Took: {end_time - start_time} seconds")
    return None

if __name__ == "__main__":
    main()