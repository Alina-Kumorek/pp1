# The array contains integer numbers from 1 to 999.
# Write a program that displays elements of the array formatted as below.

#     -----------------------------------------
#     |   1|  23|   5| 382|   1|  17|   4| 906|
#     -----------------------------------------

import random

arr = []
for i in range(random.randint(3, 10)):
    arr.append(random.randint(1, 999))

line = ""

for i in range(len(arr) * 5 + 1):
    line += "-"

disp = "|"

for i in arr:
    disp += str(i).rjust(4)
    disp += "|"

print(line)
print(disp)
print(line)