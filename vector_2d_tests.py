#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Test class Vector2D.
"""

import unittest
from vector_2d import Vector2D

def main():
    """driving code"""
    unittest.main()

class Vector2DTests(unittest.TestCase):
    """class Vector2DTests"""
    def setUp(self) -> None:
        """setting up vectors"""
        self.vector_1: Vector2D = Vector2D(0, 0)
        self.vector_2: Vector2D = Vector2D(-1, 1)
        self.vector_3: Vector2D = Vector2D(2.5, -2.5)

    def test_equality(self) -> None:
        """tests the equality operator"""
        self.assertNotEqual(self.vector_1, self.vector_2)
        expected_result = Vector2D(-1, 1)
        self.assertEqual(self.vector_2, expected_result)

    def test_add(self) -> None:
        """tests the addition operator."""
        result = self.vector_1 + self.vector_2
        expected_result = Vector2D(-1, 1)
        self.assertEqual(result, expected_result)

    def test_sub(self) -> None:
        """tests the subtraction operator"""
        result = self.vector_2 - self.vector_3
        expected_result = Vector2D(-3.5, 3.5)
        self.assertEqual(result, expected_result)

    def test_mul(self) -> None:
        """tests the multiplication operator"""
        result1 = self.vector_1 * 5
        expected_result1 = Vector2D(0.0, 0.0)
        self.assertEqual(result1, expected_result1)
        result2 = self.vector_1 * self.vector_2
        expected_result2 = 0.0
        self.assertEqual(result2, expected_result2)

    def test_div(self):
        """ Tests the multiplication operator"""
        result = self.vector_3 / 5
        expected_result = Vector2D(0.5, -0.5)
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    main()