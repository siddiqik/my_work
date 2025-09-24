"""
Create classes for the toolkit.
Each class defines a shape with its attributes
Attributes:
    Dimentions
    Area
    Describing
Importing math before hand allows
"""
import math
class Rectangle:
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def describe(self) -> str:
        return f"Rectangle(width={self.width} cm, height={self.height} cm)"

class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        return (self.radius ** 2) * math.pi

    def describe(self):
        return f"Circle(rad={self.radius} cm)"

class Triangle:
    def __init__(self, base: float, height: float):
        self.base = base
        self.height = height

    def area(self):
        return (self.base * self.height) * 0.5

    def describe(self):
        return f"Triangle(base={self.base} cm, height={self.height} cm)"