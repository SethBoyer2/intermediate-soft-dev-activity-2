"""This module defines the TestRectangle class.

Usage:
    To execute all tests in the terminal execute the following command:

    $ python -m unittest tests/test_rectangle.py
"""

__author__ = "Seth Boyer"
__version__ = "1.0.0"

import unittest
from shape.shape import Shape
from shape.rectangle import Rectangle


class TestClient(unittest.TestCase):
    def test_returns_object_with_expected_values(self):
        rectangle = Rectangle("Red", 8, 4)

        self.assertEqual("Red", rectangle._color)

    def test_exception_raised_when_color_blank(self):
        with self.assertRaises(ValueError):
            rectangle = Rectangle("", 8, 4)

    def test_exception_raised_when_length_invalid_type(self):
        with self.assertRaises(ValueError):
            self.rectangle = Rectangle("Red", "hi", 4)

    def test_exception_raised_when_width_invalid_type(self):
        with self.assertRaises(ValueError):
            rectangle = Rectangle("Red", 8, "hi")

    def setUp(self):
        self.rectangle = Rectangle("Red", 8, 4)

    def test_str_returns_expected_output(self):
        expected = (
            "The shape color is Red.\n"
            + " This rectangle has four sides, with the lengths of 8cm, 4cm, 8cm and 4cm"
        )
        self.assertEqual(expected, str(self.rectangle))

    def test_calculate_area(self):
        expected = 32
        self.rectangle.calculate_area()
        self.assertEqual(self.rectangle.area, expected)

    def test_calculate_perimeter(self):
        expected = 24
        self.rectangle.calculate_perimeter()
        self.assertEqual(self.rectangle.perimeter, expected)
