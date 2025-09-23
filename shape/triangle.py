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

        if side_2 + side_3 > side_1:
            self.__side_1 = side_1
        else:
            raise ValueError("Invalid length")

        if side_1 + side_3 > side_2:
            self.__side_2 = side_2
        else:
            raise ValueError("Invalid length")

        if side_1 + side_2 > side_3:
            self.__side_3 = side_3
        else:
            raise ValueError("Invalid length")

        def __str__(self) -> str:
            return (
                super().__str__() + f"\n This triangle has three sides" +
                f" with lengths of {self.side_1}, {self.side_2} and {self.side_3}.")

        @abstractmethod
        def calculate_area(self, side_1: int, side_2: int, side_3: int):
            sp = (side_1 + side_2 + side_3)/2
            area = math.sqrt(sp * (sp-side_1) * (sp - side_2) * (sp - side_3))
