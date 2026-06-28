#!/usr/bin/env python3
"""Shape module."""

from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract Shape."""

    @abstractmethod
    def area(self):
        """Area."""
        raise NotImplementedError

    @abstractmethod
    def perimeter(self):
        """Perimeter."""
        raise NotImplementedError


class Circle(Shape):
    """Circle."""

    PI = 3.141592653589793

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return Circle.PI * (self.radius ** 2)

    def perimeter(self):
        return 2 * Circle.PI * self.radius


class Rectangle(Shape):
    """Rectangle."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print shape information."""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
