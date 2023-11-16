#!/usr/bin/python3
# -*- coding: utf-8 -*-

from __future__ import annotations
from typing import Union, Any, SupportsFloat
import numbers
from math import sqrt
from functools import total_ordering

@total_ordering
class Vector2D:
    """Vector2D class to perform simple vector operations"""
    def __init__(self, x: SupportsFloat = 0, y: SupportsFloat = 0) -> None:
        """Creates a vector instance with the given x and y values"""
        if isinstance(x, numbers.Real) and isinstance(y, numbers.Real):
            self.x = x
            self.y = y
        else:
            raise TypeError('You must pass in int/float values for x and y!')

    def __call__(self) -> str:
        """Callable for the vector instance to return its representation"""
        print("Calling the __call__ function!")
        return self.__repr__()

    def __repr__(self) -> str:
        """The vector instance representation"""
        return f'vector.Vector2D({self.x}, {self.y})'

    def __str__(self) -> str:
        """vector instance as a string"""
        return f'({self.x}, {self.y})'

    def __bool__(self) -> bool:
        """Returns the truth value of the vector instance"""
        return bool(abs(self))

    def __abs__(self) -> float:
        """Returns the length (magnitude) of the vector instance
        """
        return sqrt(self.x**2.0 + self.y**2.0)

    def check_vector_types(self, vector2: Vector2D):
        """Checks if the self and vector2 are an instance of the Vector2D class"""
        if not isinstance(self, Vector2D) or not isinstance(vector2, Vector2D):
            raise TypeError('You have to pass in two instances of the vector class!')

    def __eq__(self, other_vector: Any) -> bool:
        """Check if the vector instances have the same values"""
        self.check_vector_types(other_vector)
        is_equal = False
        if self.x == other_vector.x and self.y == other_vector.y:
            is_equal = True
        return is_equal

    def __lt__(self, other_vector: Vector2D) -> bool:
        """Check if the self instance is less than the other vector instance"""
        self.check_vector_types(other_vector)
        is_less_than = False
        if abs(self) < abs(other_vector):
            is_less_than = True
        return is_less_than

    def __add__(self, other_vector: Vector2D) -> Vector2D:
        """Returns the additon vector of the self and the other vector instance"""
        self.check_vector_types(other_vector)
        x_value = self.x + other_vector.x
        y_value = self.y + other_vector.y
        return Vector2D(x_value, y_value)

    def __sub__(self, other_vector: Vector2D) -> Vector2D:
        """Returns the subtraction vector of the self and the other vector instance"""
        self.check_vector_types(other_vector)
        x_value = self.x - other_vector.x
        y_value = self.y - other_vector.y
        return Vector2D(x_value, y_value)

    def __mul__(self, other: Union[Vector2D, SupportsFloat]) -> Union[Vector2D, SupportsFloat]:
        """Returns the multiplication of the self vector and the other vector(or number) instance"""
        if isinstance(other, Vector2D):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, numbers.Real):
            return Vector2D(self.x * other, self.y * other)
        else:
            raise TypeError('You must pass in a vector instance or an int/float number!')

    def __truediv__(self, other: SupportsFloat) -> Vector2D:
        """Returns the multiplication of the self vector and the other vector(or number) instance"""
        if isinstance(other, numbers.Real):
            if other != 0.0:
                return Vector2D(self.x / other, self.y / other)
            else:
                raise ValueError('You cannot divide by zero!')
        else:
            raise TypeError('You must pass in an int/float value!')
