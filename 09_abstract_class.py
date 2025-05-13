# 9. Abstract Classes and Methods
# Assignment:
# Use the abc module to create an abstract class Shape with an abstract method area(). Inherit a class Rectangle that implements area().

# Create an instance of Rectangle and print the area.
from abc import ABC, abstractmethod

class Shape(ABC):
    #A decorator in Python is a function that modifies the behavior of another function or method,
    @abstractmethod 
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

area_of_rectangle = Rectangle(3 , 6)
print(f"Area of rectangle is: {area_of_rectangle.area()}")  # Output: Area of rectangle is: 18