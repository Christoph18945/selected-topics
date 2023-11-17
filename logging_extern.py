#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""installation of loguru:
pip3 install loguru
https://github.com/Delgan/loguru
"""

from pathlib import Path
from loguru import logger

# logger settings
filepath = Path(__file__).parent.joinpath('log_loguru.log')
logger.add(filepath, rotation="1 Week")

@logger.catch
def divide_integers(a: int, b: int) -> float:
    """divide integers
    """
    logger.debug(f"a={a}, b={b}")
    result = a / b
    return result

def main():
    """main program
    """
    for _ in range(3):
        print(divide_integers(10, 0))

if __name__ == "__main__":
    main()
