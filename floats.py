#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Short discussion about floats.

Subjects covered: print, round, compare

Python floats (64 bit = 8 Bytes)
sign: 11 bits
exponent: 11 bits
significant bits: 52 bits
"""

import math
import sys

def main() -> None:
    """main program"""
    # total of 24 bytes:
    # 8 bytes - value
    # 16 bytes - others
    val_1: float = 42.3
    val_1_size = sys.getsizeof(val_1)
    print(val_1_size) # size provided in bytes
    print(val_1)

    # precisely print with 32 floating values
    float_print(val_1)

    # Why comparison of floats does not work?
    my_fraction_0 = 0.3
    float_print(my_fraction_0)

    my_fraction_1 = 1 / 10 + 1 / 10 + 1 / 10
    float_print(my_fraction_1)

    # The compared floats should be equal, but
    # they are not
    if my_fraction_0 == my_fraction_1:
        print("Compared floats are equal!")
    else:
        print("Compared floats are not equal!")

    # What to do to realistically compare floats.
    # The following can be done ...
    print(floats_are_equal(my_fraction_0, my_fraction_1))
    print(math.isclose(my_fraction_0, my_fraction_1))

    # Attention with rounded values
    my_float_0: float = 42.424242
    float_print(my_float_0)

    my_float_0_rounded0: float = round(my_float_0)
    float_print(my_float_0_rounded0)

    # round to the 4th decimal place
    my_float_0_rounded1: float = round(my_float_0, 4)
    float_print(my_float_0_rounded1)
    
    # For negative is raised to the next multiple of 10 to the power
    # Meas for example rounded to 10**-1, 10**-2 or 10**-3
    my_float_0_rounded1 = round(my_float_0, -1)
    my_float_0_rounded1 = round(my_float_0, -2)
    my_float_0_rounded1 = round(my_float_0, -3)

    return None

def floats_are_equal(x: float, y: float) -> bool:
    """Compare two float values"""
    epsilon = 1e-15
    # NOTE: Relative tolerance depends on
    # the size of both values. The smaller
    # the values, the smaller the allowed
    # tolerance is.
    # Here: absolute tolerance:
    difference = math.fabs(x - y)
    return difference < epsilon

def float_print(value: float) -> None:
    """Precisely print a float value"""
    print(f"{value:.32f}")

if __name__ == "__main__":
    main()