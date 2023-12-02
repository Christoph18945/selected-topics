#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Test code"""

import time
import random
from timeit import Timer
from functools import wraps
from vector_2d import Vector2D

def main() -> None:
    """main function"""
    code: str = '''vector_1 = Vector2D(random.randint(-10, 10), random.randint(-10, 10))
vector_2 = Vector2D(random.randint(-10, 10), random.randint(-10, 10))
class_3 = vector_1 + vector_2'''

    string_import: str = '''import random
from class.Vector2D import Vector2D'''    
    timer = Timer(code, setup=string_import)
    print(f"Mean computation time: {(sum(timer.repeat(repeat=3, number=100_000)) / 3)}")
    print("Own timer implementation: ")
    test_addition()
    print(test_addition())
    print("Standard lib timer implementation: ")
    test_addition_std_lib()
    return None

def timing(function):
    """timing"""
    @wraps(function)
    def timer(*args, **kwargs):
        start: float = time.perf_counter()
        func_result = function(*args, **kwargs)
        end: float = time.perf_counter()
        duration: float = end - start
        print(f"Function {function.__name__} took: {duration} seconds")
        return func_result
    return timer

@timing
def test_addition() -> Vector2D | None:
    """test addition"""
    for _ in range(100):
        vector_1 = Vector2D(random.randint(-10, 10), random.randint(-10, 10))
        vector_2 = Vector2D(random.randint(-10, 10), random.randint(-10, 10))
        class_3 = vector_1 + vector_2
        return class_3
    return None

def test_addition_std_lib() -> None:
    """test addition standard lib"""
    return None
