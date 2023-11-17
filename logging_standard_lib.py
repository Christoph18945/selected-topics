#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
DEBUG: Detailed debug information
INFO: Things working as intended
WARNING: Something unexpected happened
ERROR: The software cannot perform some function
CRITICAL: Program crashes for example
"""

import logging
from pathlib import Path

# Setup the logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Formatter, FileHandler
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(funcName)s:%(message)s')
filepath = Path(__file__).parent.joinpath('log_standard.log')
file_handler = logging.FileHandler(filepath)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def main():
    """main program"""
    for _ in range(3):
        print(divide_integers(10, 0))

def divide_integers(val_a: int, val_b: int) -> float:
    """divide integers
    """
    try:
        logger.debug(f"a={val_a}, b={val_b}")
        result = val_a / val_b
        return result
    except Exception as e:
        logger.exception(f"Exception was raised: {e}")

if __name__ == "__main__":
    main()
