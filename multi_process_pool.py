#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Multi processing pool demonstration.

.. _PEP 484:
    https://www.python.org/dev/peps/pep-0484/    

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html
"""

import itertools
from multiprocessing import Pool, Process
import time
from calculations import Calculations

def main() -> None:
    """driver code"""
    NUM_PROCESSES: int = 4
    start_time: float = time.perf_counter()
    print(start_time)
    clc2: Calculations = Calculations()
    with Pool(processes=NUM_PROCESSES) as pool:
        pool.map(clc2.calc_square, itertools.repeat(8_000_000, NUM_PROCESSES))
        print(f"pool map: {pool.map(clc2.calc_square, [2,4,])}")
        end_time = time.perf_counter()
        print(end_time)
        print(f"Took: {end_time - start_time} seconds")

    processes: list = []
    clc1: Calculations = Calculations()
    for _ in range(NUM_PROCESSES):
        processes.append(Process(target=clc1.calc_square, args=[2]))
    print(processes)

    start_time = time.perf_counter()
    for process in processes:
        print(f"start process: {process.start()}")
    for process in processes:
        print(f"end process: {process.join()}")

    end_time = time.perf_counter()
    print(f"Took: {end_time - start_time} seconds")
    return None

if __name__ == "__main__":
    main()