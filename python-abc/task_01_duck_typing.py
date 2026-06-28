#!/usr/bin/env python3
"""Duck typing module."""

from abc import ABCMeta, abstractmethod
import math


class Shape(metaclass=ABCMeta):
    """Abstract Shape class."""

    @abstractmethod
    def area(self):
        """Return area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Return perimeter."""
        pass


class Circle(Shape):
    """Circle class."""

    def __init__(self, radius):
        self._radius = radius

    def area(self):
        return math.pi * (self._radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self._radius


class Rectangle(Shape):
    """Rectangle class."""

    def __init__(self, width, height):
        self._width = width
        self._height = height

    def area(self):
        return self._width * self._height

    def perimeter(self):
        return 2 * (self._width + self._height)


def shape_info(shape):
    """Print area and perimeter."""
    area = shape.area()
    perimeter = shape.perimeter()
    print("Area:", area)
    print("Perimeter:", perimeter)
