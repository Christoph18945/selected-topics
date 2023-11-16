#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""special parameters
"""

    # modules/sequential.py
    # calc: Calculations = Calculations()

    start_time = time.perf_counter()

    for _ in range(4):
        ...
        # calc.calc_square(10)

    end_time = time.perf_counter()
    print(f"Took: {end_time - start_time} seconds")