"""
OPEN-CLOSED PRINCIPLE
Classes, modules, functions, etc. should be open for extension, but closed for modification.

Simply means that if you need to add additional functionality then you should NOT be editing the
existing classes or methods to make it happen.
"""
import math


# BAD EXAMPLE FIRST
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height


class AreaCalculator:
    def calculate_area(self, rectangle:Rectangle):
        return rectangle.width * rectangle.height


# Later, you need to add Circle class and support for calculating the area of a circle
class Circle:
    def __init__(self, radius):
        self.radius = radius

# Which means that you have to now "modify" this AreaCalculator! Which is BAD!!
class AreaCalculator:
    def calculate_area(self, shape):
        if isinstance(shape, Rectangle):
            return shape.width * shape.height
        elif isinstance(shape, Circle):
            return math.pi * (shape.radius ** 2)
        return None


"""
### WHY IS IT BAD?
In this example, if you need to add support for calculating the area of a circle, you would have
 to modify the AreaCalculator class, violating the Open-Closed Principle.
"""


#############################################################################################
#############################################################################################
# GOOD EXAMPLE NOW
#############################################################################################
#############################################################################################


from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def calculate_area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius


class AreaCalculator:
    def calculate_area(self, shape):
        return shape.calculate_area()


"""
### WHY IS IT GOOD?
In this improved example, we introduce an abstract base class Shape that declares the
 calculate_area method. Both Rectangle and Circle classes inherit from Shape and provide
  their own implementations of calculate_area. The AreaCalculator class now works with any
   shape that is a subclass of Shape without modification, adhering to the Open-Closed Principle.
    If you need to add a new shape, you can do so by creating a new class that extends Shape
     without changing the existing code
"""
