#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""profiling demonstration
"""

import cProfile
import pstats
import io
import random
from functools import wraps
from vector_2d import Vector2D

def main() -> None:
    """main function"""
    """"""
    test_addition()
    return None

def profile(f_n):
    """profile"""
    @wraps(f_n)
    def profiler(*args, **kwargs):
        profiler: object = cProfile.Profile()
        profiler.enable()
        f_n_result = f_n(*args, **kwargs)
        profiler.disable()
        stream = io.StringIO()
        ps: pstats.Stats = pstats.Stats(profiler, stream=stream).sort_stats('time')
        ps.print_stats()
        print(stream.getvalue())
        return f_n_result
    return profiler

@profile
def test_addition():
    """test addition"""
    for _ in range(100_000):
        vector_1: Vector2D = Vector2D(random.randint(-10, 10), random.randint(-10, 10))
        vector_2: Vector2D = Vector2D(random.randint(-10, 10), random.randint(-10, 10))
        sum_3: Vector2D = vector_1 + vector_2
        return sum_3

if __name__ == "__main__":
    main()
