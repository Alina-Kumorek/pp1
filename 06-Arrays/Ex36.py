# A two-dimensional array of size 2 by 4 contains integer numbers.
# Create a program that displays array values in rows and columns.

def display_arr(array):

    # find how long are numbers in the array
    max_array = []

    for i in range(len(array)):
        max_array.append(max(array[i]))
    
    max_max = len(str(max(max_array)))

    # prepare string for displaying the array
    x = ""

    for i in range(len(array)):
        for j in range(len(array[i])):
            x += str(arr[i][j]).rjust(max_max)
            if j != len(array[i]) - 1:
                x += " "
            else:
                x += "\n"
    
    return x

import random

arr = []
for i in range(4):
    a = []
    for j in range(2):
        a.append(random.randint(0, 99))
    arr.append(a)

print(arr)
print()
print(display_arr(arr))