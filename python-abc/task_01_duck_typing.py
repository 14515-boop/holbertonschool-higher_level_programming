#!/usr/bin/env python3
"""Module for Shape, Circle and Rectangle."""

from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract Shape class."""

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """Circle class."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.141592653589793 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.141592653589793 * self.radius


class Rectangle(Shape):
    """Rectangle class."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print shape information."""
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
