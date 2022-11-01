# Let x and y denote the coordinates of a point on the plane.
# Write a program that determines in which quadrant of the coordinate system the point P (x, y)
# is located or on which axis it is located, or that it is located in the position (0,0) of the coordinate system.

# II  | I
# III | IV

import random

# determine plane position
x = random.randint(-5, 5)
y = random.randint(-5, 5)

q = ""

# determine quadrant
if x == 0:
    if y == 0:
        q = "in the position (0,0)"
    else:
        q = "on the Y axis"
elif y == 0:
    q = "on the X axis"
elif x > 0:
    if y > 0:
        q = "in the first quadrant"
    else:   # y < 0
        q = "in the fourth quadrant"
else:       # x < 0
    if y > 0:
        q = "in the second quadrant"
    else:   # y < 0
        q = "in the third quadrant"

# output
print(f"""x = {x}
y = {y}
Point P({x},{y}) is {q} of the coordinate system""")