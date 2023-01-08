# Write a program that checks whether the first array is a subset of the second one
# (whether all elements of the first array appear in the second array).

def check_subset(array1, array2):
    is_sub = True

    for i in array1:
        if i not in array2:
            is_sub = False
    
    return is_sub

import random

arr1 = []
arr2 = []

for i in range(random.randint(3, 8)):
    arr1.append(random.randint(0, 99))

if random.randint(0, 1):
    for i in range(random.randint(0, 4)):
        arr2.append(random.randint(0, 99))
    arr2 += arr1
else:
    for i in range(random.randint(3, 12)):
        arr2.append(random.randint(0, 99))

print(f"Array1: {arr1}")
print(f"Array2: {arr2}")
print(f"Is a subset?: {check_subset(arr1, arr2)}")