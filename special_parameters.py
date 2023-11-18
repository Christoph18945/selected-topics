#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""special parameters"""

def main():
    """driver code"""
    # combined_example(1, 2, 3) # missing mandatory keyword c!
    print(combined_example(1, 2, c=3))
    print(combined_example(1, b=2, c=3))
    # combined_example() got some positional-only arguments passed as keyword arguments: 'a'
    # print(combined_example(a=1, b=2, c=3))
    print(kwd_only_arg(a=3))
    # print(kwd_only_arg(3)) # missing mandatory keyword a!
    my_val = 5
    print(pos_only_arg(1))
    print(pos_only_arg(my_val))
    print(standard_argument(2))
    # print(standard_argument(a=2)) # standard_argument() got an unexpected keyword argument 'a'

def standard_argument(param_a) -> None:
    """if / and * are not present in the function
    definition, arguments may be passed to a function
    by position or by keyword"""
    print(param_a)

def pos_only_arg(a, /) -> None:
    """if positional-only, the parameters’ order matters, and the parameters
    cannot be passed by keyword. Positional-only parameters are placed before
    a / (forward-slash). Use positional-only if you want the name of the
    parameters to not be available to the user"""
    print(a)

def kwd_only_arg(*, a) -> None:
    """pos_only_arg(a=1) to mark parameters as keyword-only, indicating the
    parameters must be passed by keyword argument, place an * in the arguments
    list just before the first keyword-only parameter. use keyword-only when
    names have meaning and the function definition is more understandable by
    being explicit with names"""
    print(a)

def combined_example(a, /, b, *, c) -> None:
    """combine with special parameters"""
    print(a, b, c)

if __name__ == "__main__":
    main()
