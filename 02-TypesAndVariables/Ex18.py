###
# Calculating area of a triangle
# from the lenght of its sides
# using the Heron formula.
###

# get the lenghts of the sides
a = float(input("side a = "))
b = float(input("side b = "))
c = float(input("side c = "))

# calculate area
s = (a + b + c) / 2
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

# display result
print(f"Area of the triangle = {area}")