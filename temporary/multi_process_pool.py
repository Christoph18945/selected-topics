#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Multi processing pool demonstration.

.. _PEP 484:
    https://www.python.org/dev/peps/pep-0484/    

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html
"""

    # modules/multi_process_pool.py
    NUM_PROCESSES = 4
    start_time = time.perf_counter()
    # clc2: Calculations = Calculations()
    with Pool(processes=NUM_PROCESSES) as pool:
        # pool.map(clc2.calc_square, itertools.repeat(8_000_000, NUM_PROCESSES))
        # print(pool.map(clc2.calc_square, [2,4,]))
        end_time = time.perf_counter()
        print(f"Took: {end_time - start_time} seconds")

    # modules/multi_processing.py
    processes = []
    # clc1: Calculations = Calculations()

    for _ in range(NUM_PROCESSES):
        ...
        # processes.append(Process(target=clc1.calc_square, args=[2]))


    start_time = time.perf_counter()
    for process in processes:
        process.start()
    for process in processes:
        process.join()

    end_time = time.perf_counter()
    print(f"Took: {end_time - start_time} seconds")