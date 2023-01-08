# Create a program that sorts elements of an array containing integer numbers.
# Apply the Bubble Sort sorting algorithm. Define a function bubblesort(array) that returns the sorted array.
# Try to sort and display any three arrays.

def bubblesort(array):

    done = False

    while done != True:
        changed = False

        # Compare each (exept the last) element of the array with the next one and change their location if needed
        for i in range(len(array) - 1):
            a = array[i]
            b = array[i + 1]
            if a > b:
                array[i] = b
                array[i + 1] = a
                changed = True

        # Check if there were any changes made in the current loop iteration
        if changed == False:
            done = True
    
    return array

import random

arr1 = []
arr2 = []
arr3 = []

for i in range(random.randint(1, 30)):
    arr1.append(random.randint(0, 100))

for i in range(random.randint(1, 30)):
    arr2.append(random.randint(0, 100))

for i in range(random.randint(1, 30)):
    arr3.append(random.randint(0, 100))

print(f"{arr1}\n{bubblesort(arr1)}\n\n{arr2}\n{bubblesort(arr2)}\n\n{arr3}\n{bubblesort(arr3)}")