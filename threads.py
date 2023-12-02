#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Example of Threads.


"""

import time
from threading import Thread

def main() -> None:
    """main function"""
    # Thread object is created here:
    # Passing function y name via target
    # args are the arguments for the worker function
    t1 = Thread(target=worker, name="t1", args=(2.0,))
    print(f"Ident: {t1.ident}")
    print(f"Alive: {t1.is_alive()}")
    print(f"Name: {t1.name}")
    
    t1.start() # start thread
    print(f"Ident: {t1.ident}")
    print(f"Alive: {t1.is_alive()}")
    print(f"Name: {t1.name}")
    # Here the Pyhton program would wait until
    # the thread finished the work
    t1.join()

    return None

def worker(sleep_time: float) -> None:
    """Worker"""
    print("Start worker")
    time.sleep(sleep_time)
    print("End worker")

if __name__ == "__main__":
    main()
