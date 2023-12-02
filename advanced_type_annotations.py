#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Getting deeper into Type Annotations

For type annotations in later than Python3.11.X: 
https://marketplace.visualstudio.com/items?itemName=matangover.mypy
https://microsoft.github.io/pyright/#/

Modules used here
https://docs.python.org/3/library/typing.html
"""

# from typing import reveal_type # type: ignore
from typing import Any, Dict, NewType, Union, Callable, List
# from typing import NoReturn

def main():
    """main program"""
    res = greeting("christoph")
    # print(reveal_type(res))

    # Any
    # should never be used because it communicates to
    # mypy that the funciton should no tbe used.
    # A part from dict[str, Any]. It means only that
    # the values can be of any datatype

    # List
    lst = [1,2,3.0,"dsadsa"]
    append_list(lst, 4) # error because wrong datatype

    # Tuple
    tpl_0 = (1, True) # error because three values must be provided
    # tpl_1: tuple[Any, Any, Any] = (1, True, "")
    print_3d_tuple(tpl_0)
    
    # Dict
    # Difference: Dict and Mapping. Mapping is not mutable
    my_dict = {"christoph": 34, "person": 38}
    iterate_over_dict(my_dict)

    # None versus NoReturn
    # NoReturn - When function only throws an exception.
    # Even if it is not used if None is returned implicitly
    # None - is used implicitly but can be written as well

    # Calable
    # print(function([1,2,3]))

    # Args and Kwargs
    call(f,1,2,3,a=1,b=2,c=3)

    # NewType and Type Alias
    UserId1 = NewType("userId1", int)
    UserId2 = int

# def f(*args: Any, **kwargs: Union[int, float]) -> None:
def f(*args: int, **kwargs: Union[int, float]) -> None:
    """f prints arguments and keyword arguents"""
    print(f"{args}, {kwargs}")

def call(f: Callable[..., None], *args: int, **kwargs: int) -> None:
    """Call function"""
    return f(*args, **kwargs)

# def function(values: List[int], print_fn: Callable[..., ], None]) -> None: # Define if parameter list is relevant
def function(values: List[int], print_fn: Callable[[List[int]], None]) -> None:
    """A function."""
    print_fn(values)

def print_list(values: List[int]) -> None:
    """print a list."""
    print(values)
    return None

def iterate_over_dict(my_dict: Dict[str, Union[int, float]]) -> None:
    """iterate over a provided dictionary"""
    for key, value in my_dict.items():
        print(key, value)
    return None

def print_3d_tuple(tpl: tuple[Any, Any, Any]) -> None:
    """Print 3-dimensional tuple"""
    for val in tpl:
        print(val)
    return None

def append_list(lst: list[float | int], val: float | int) -> None:
    """Append a list"""
    lst.append(val)

def greeting(name: str) -> str:
    """Print out the greeting section"""
    return f"hello {name}"

if __name__ == "__main__":
    main()
