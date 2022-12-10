# An array contains integer numbers. Create a program that calculates and displays
# the number of even and odd valuesin the array. Use the “while” loop statement.

import random

arr = [random.randint(0,100) for i in range(random.randint(5,20))]
print(arr)

even = 0
odd = 0
index = 0

while index < len(arr):
    if arr[index] % 2 == 0:
        even += 1
    else:
        odd += 1
    index += 1

print(f"Even:\t{even}\nOdd:\t{odd}")