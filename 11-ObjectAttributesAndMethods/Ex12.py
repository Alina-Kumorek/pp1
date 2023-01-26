# Operator overloading is defining the meaning of existing operators for your own data types.
# Often implemented in the form of the use of special methods. For example, in Python,
# the new functionality for the comparison operator == can be implemented by defining the __eq__ function in the class.

# On the Internet, find examples of __eq__ definitions. Then complete the Point class below,
# describing a point on the plane with coordinates (x, y), by adding the __eq__ method to compare two points.

#     class Point():
#         def __init__(self,x,y):
#             self.x = x
#             self.y = y
#         def __str__(self):
#             return f'P({self.x},{self.y})'

# Using the Point class, create a program that calculates the distance on the plane between two defined points. 
# Using the conditional statement check if these points are identical - use the comparison operator ==, i.e. p1 == p2.
# If the points are identical, display a message that the distance between them is 0. Otherwise, calculate and display
# the distance between the two points.

class Point():

    @staticmethod
    def distance(pointA, pointB):
        if pointA == pointB:
            print(f"The distance between points {pointA} and {pointB} is 0")
        else:
            d = ((pointA.x - pointB.x)**2 + (pointA.y - pointB.y)**2) ** (1/2)
            print(f"The distance between points {pointA} and {pointB} is {d}")

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'P({self.x},{self.y})'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
p1 = Point(25, 48)
p2 = Point(28, 45)
p3 = Point(25, 48)

Point.distance(p1, p2)
Point.distance(p1, p3)