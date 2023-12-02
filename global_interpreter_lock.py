#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Global interpreter lock.

Python Global Interpreter Lock (GIL) is a type of process lock which is used by python whenever it deals with processes. Generally, Python only uses only one thread to execute the set of written statements. This means that in python only one thread will be executed at a time. The performance of the single-threaded process and the multi-threaded process will be the same in python and this is because of GIL in python. We can not achieve multithreading in python because we have global interpreter lock which restricts the threads and works as a single thread.

What problem did the GIL solve for Python :

Python has something that no other language has that is a reference counter. With the help of the reference counter, we can count the total number of references that are made internally in python to assign a value to a data object. Due to this counter, we can count the references and when this count reaches to zero the variable or data object will be released automatically. For Example

Source of explanation: https://www.geeksforgeeks.org/what-is-the-python-global-interpreter-lock-gil/
"""

import math
import time
from threading import Thread

numbers = [
    1102023313711321,
    2102023313556361,
    2133132415198713,
    2456241020233131,
    2102124102331313,
    2102023151513137,
    2102023313112511,
]

def main() -> None:
    """main function"""
    # That could be done, but...
    start = time.perf_counter_ns()
    for number in numbers:
        is_prime(number)
    end = time.perf_counter_ns()
    print(f"time: {(end - start) / 1000000.0} ms")
    
    # ... this one here is faster
    # What is the GIL doing now?
    # GIL makes it that only one thread is executed
    # because every cycle, one thread is executed, therefore
    # no time is won here! THe GILs can not overlapp on the CPU
    threads = [Thread(target=is_prime, args=(number,)) for number in numbers]
    start = time.perf_counter_ns()
    print([t.start() for t in threads])
    print([t.join() for t in threads])
    end = time.perf_counter_ns()
    print(f"time: {(end - start) / 1000000.0} ms")
    return None

def is_prime(n):
    """Checkk if number is prime or not."""
    if n < 2:
        return False
    if n in {2, 3, 5, 7}:
        return True
    if n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0:
        return False
    upper_limit = int(math.sqrt(n)) + 1
    return all(n % i != 0 for i in range(11, upper_limit, 2))

if __name__ == "__main__":
    main()
