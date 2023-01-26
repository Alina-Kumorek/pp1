# Create a class with three static methods for calculating the surface area of figures: triangle, rectangle, circle.
# Then use these methods to calculate the area of the following figures:
# a.	Circle with a radius of 3
# b.	Rectangle with sided 4 and 7
# c.	Triangle with base 6 and height 2

class Surface():

    pi = 3.141592653589793

    @staticmethod
    def triangle(base, height):
        return (base * height) / 2
    
    @staticmethod
    def rectangle(sideA, sideB):
        return sideA * sideB
    
    @staticmethod
    def circle(radius):
        return Surface.pi * radius ** 2

print(Surface.circle(3))
print(Surface.rectangle(4, 7))
print(Surface.triangle(6, 2))