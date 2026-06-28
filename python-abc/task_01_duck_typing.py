#!/usr/bin/env python3

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius = radius

    def area(self):
        return pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * pi * self.radius

    def __str__(self):
        return f"Circle(radius={self.radius})"


class Rectangle(Shape):
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side):
        if side <= 0:
            raise ValueError("Side must be positive")
        super().__init__(side, side)

    def __str__(self):
        return f"Square(side={self.width})"


class Triangle(Shape):
    def __init__(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Sides must be positive")
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Invalid triangle sides")
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        # Heron's formula
        s = (self.a + self.b + self.c) / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5

    def perimeter(self):
        return self.a + self.b + self.c

    def __str__(self):
        return f"Triangle(a={self.a}, b={self.b}, c={self.c})"


def shape_info(shape):
    print(shape)
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())


# Örnek kullanım
circle = Circle(5)
rectangle = Rectangle(4, 6)
square = Square(3)
triangle = Triangle(3, 4, 5)

for s in [circle, rectangle, square, triangle]:
    shape_info(s)
    print()
