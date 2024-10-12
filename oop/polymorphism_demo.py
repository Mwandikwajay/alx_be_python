
import math

# Base Class - Shape
class Shape:
    def area(self):
        """Method to be overridden in derived classes."""
        raise NotImplementedError("Subclasses must override the area method.")

# Derived Class - Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        """Initialize a rectangle with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Calculate the area of the rectangle."""
        return self.length * self.width

# Derived Class - Circle
class Circle(Shape):
    def __init__(self, radius):
        """Initialize a circle with radius."""
        self.radius = radius

    def area(self):
        """Calculate the area of the circle."""
        return math.pi * (self.radius ** 2)
