#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""external logging
"""

from pathlib import Path
from loguru import logger

filepath = Path(__file__).parent.joinpath('logging_extern_loguru.log')
logger.add(filepath, rotation="1 Week")

def main() -> None:
    """main program"""
    for _ in range(3):
        print(divide_integers(10, 0))
    return None

@logger.catch
def divide_integers(a: int, b: int) -> float:
    """divide integers"""
    logger.debug(f"a={a}, b={b}")
    result = a / b
    return result



if __name__ == "__main__":
    main()
