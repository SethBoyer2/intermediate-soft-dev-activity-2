"""This module defines the Triangle class."""

from shape.shape import Shape
from abc import ABC, abstractmethod
import math

__author__ = "Seth Boyer"
__version__ = "1.0.0"


class Triangle(Shape):
    """
    if my name was scoobert i would have very few friends.
    """

    def __init__(self, color: str, side_1: int, side_2: int, side_3: int):

        super().__init__(color)

        if isinstance(side_1, int):
            self.__side_1 = side_1

        else:
            raise ValueError("Side 1 must be numeric.")

        if isinstance(side_2, int):
            self.__side_2 = side_2

        else:
            raise ValueError("Side 2 must be numeric.")

        if isinstance(side_3, int):
            self.__side_3 = side_3
        else:
            raise ValueError("Side 3 must be numeric.")

        if not (side_2 + side_3 > side_1 and
                side_1 + side_3 > side_2 and
                side_1 + side_2 > side_3):
            raise ValueError(
                "Please ensure all sides adhere to the triangle inequality theorem.")

    def __str__(self) -> str:
        return (
            super().__str__() + f"\n This triangle has three sides" +
            f" with lengths of {self.__side_1}, {self.__side_2} and {self.__side_3}.")

    def calculate_area(self) -> float:
        """
        This method takes three validated arguments, and uses
        them to calculate the area of the shape

        Args:
        side_1(int) : side 1 of the triangle
        side_2(int) : side 2 of the triangle
        side_3(int) : side 3 of the triangle

        Returns:
        Area(float) : The area of the shape
        """
        sp = (self.__side_1 + self.__side_2 + self.__side_3)/2
        self.area = math.sqrt(sp * (sp - self.__side_1) *
                              (sp - self.__side_2) * (sp - self.__side_3))
        self.area = round(self.area, 2)

    def calculate_perimeter(self) -> float:
        """
        This method takes three validated arguments and returns
        the sum as the perimeter of the shape

        Args:
        side_1(int) : side 1 of the triangle
        side_2(int) : side 2 of the triangle
        side_3(int) : side 3 of the triangle

        Returns:
        Perimeter(int): the sum of all three sides.
        """
        self.perimeter = (self.__side_1 + self.__side_2 + self.__side_3)
        self.perimeter = round(self.perimeter)
