# Create a function that convert two-dimensional (2D) array into 1D. Then create a program that displays 1D array for the following 2D arrays.
#     a.	2 3
#           1 5 
#     b.	5 0 3 7 5
#           9 0 9 1 2
#     c.	2 1
#           3 5
#           7 4
#           2 6

def arrayFlattener(array):

    x = []

    for i in range(len(array)):
        for j in range(len(array[i])):
            x.append(array[i][j])
    
    return x

arr1 = [[2, 3], [1, 5]]
arr2 = [[5, 0, 3, 7, 5], [9, 0, 9, 1, 2]]
arr3 = [[2, 1], [3, 5], [7, 4], [2, 6]]

print(arr1)
print(arrayFlattener(arr1))
print()
print(arr2)
print(arrayFlattener(arr2))
print()
print(arr3)
print(arrayFlattener(arr3))