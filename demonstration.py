from math import pi
from typing import List

# The four pillars of OOP are inheritence, polymorphism, Encapsulation, and abstraction
# Below are examples that show each pillar in action

################################
# Inheritence and Polymorphism #
################################

# Shape is the base class
class Shape:
    # The area method
    def area(self):
        raise "This method is not implemented"

    # The frobulate method
    def frobulate(self):
        print("I am doing something!\nNot sure what...")

# Rectange inherits from Shape
# It inherits all of Shape methods except for the __init__ method
class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    # The Rectangle implements its own area method
    def area(self):
        return self.w * self.h

# Circle inherits from Shape
# It inherits all of Shape methods except for the __init__ method
class Circle(Shape):
    def __init__(self, r):
        self.r = r

    # The Circle implements its own area method
    def area(self):
        return pi * (self.r ** 2)

# Because of inheritence, Rectangle is a Shape
assert(isinstance(Rectangle(1, 1), Shape))

# It is also an instance of Reactange
assert(isinstance(Rectangle(1, 1), Rectangle))

# Though a Rectangle it is not a Circle
assert(not isinstance(Rectangle(1, 1), Circle))

# But Circle is still a Shape
assert(isinstance(Circle(2), Shape))

# Creating a circle with radius 10
my_circle = Circle(10)

# We can get its area, implemented by the Circle class
print(my_circle.area())

# We can also frobulate the Circle, implemented by the Shape class
my_circle.frobulate()

# This leads us to polymorphism
# Because Rectangle and Circle are both Shapes, we know they implement the area method
# Thus if we have a list of Shapes, we can iterate over each callng the area method
# Polymorphism is that even though we are calling the same name of a method (area) it is calling 
# a different function based on the Shape's type

# For example we have a list of shapes
shape_list: List[Shape] = [Circle(10), Rectangle(20, 30), Circle(2), Rectangle(1, 0), Rectangle(4, 5)]

# Now if we iterate over the list, we dont have to check whether the element is a Rectangle or 
# Cirle. Polymorphism takes care of it for us.
for shape in shape_list:
    print(shape.area())

###############
# Abstraction #
###############

# A Pretty Point Class
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # These are dunder methods that correspond to different operators

    # Addition
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    # Subtraction
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    
    # Negation
    def __neg__(self):
        return Point(-self.x, -self.y)

# Abstraction is the ability to more clearly express what the program is doing
# without the unnessicary details of how it is doing it

# We have two points
point1 = Point(1, 1)
point2 = Point(3, 2)

# With abstraction we can add them like so
added_point = point1 + point2
# This is more clear and makes the program more readable

##################
# Encapsulation #
##################

# A class that controls an led
class Led:
    def __init__(self):
        self._on = False

    def toggle(self):
        if self._on:
            # Turn the led off
            # THIS IS A COMPLEX PROCESS AND IS NOT THE SAME AS TURNING IT ON
            pass
        else:
            # Turn the led on
            # THIS IS A COMPLEX PROCESS AND IS NOT THE SAME AS TURNING IT OFF
            pass
        self._on = not self._on

# Encapsulation is the idea that an object should be manipulated only through its 
# methods. In this example it is critical that self._on is not changed outside of the
# toggle method. If it were it could mess up the complex processes being performed.
