# A two-dimensional array of the size 3 by 5 contains integer numbers.
# Create a program that swaps the first and the last row.
# Display array values in rows and columns before and after changes.

import random

arr = []
for i in range(5):
    a = []
    for j in range(3):
        a.append(random.randint(0, 99))
    arr.append(a)

print(arr)

first_row = arr[0]
last_row = arr[-1]

arr[0] = last_row
arr[-1] = first_row

print(arr)