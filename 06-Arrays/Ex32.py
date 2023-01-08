# Define a function that returns the elements of the array as a string, separated by commas.
# Using defined functions, display the contents of any array. Sample result:

#     Array: [5,4,3,2,6,5]
#     String: 5,4,3,2,6,5

def stringify(array):

    x = str(array[0])

    for i in range(1, len(array)):
        x += ","
        x += str(array[i])
    
    return x

import random

arr = []
for i in range(random.randint(3, 20)):
    arr.append(random.randint(0, 99))

print("Array:\t[", end="")
for i in range(len(arr)):
    if i < len(arr) - 1:
        print(arr[i], end=",")
    else:
        print(f"{arr[i]}]")

print(f"String:\t {stringify(arr)}")