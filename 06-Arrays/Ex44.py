# Create a function transpose_matrix(m) that returns transposed matrix m.
# Then create a program that displays transposed matrices, in rows and columns, for the following matrices.
#     a.	1 2 3
#           4 5 6
#           7 8 9
#     b.	1 2 3 4 5
#           6 7 8 9 0
#     c.	5 6 7 8

def transpose_matrix(m):
    arr = []
    # the array is multidimensional
    if type(m[0]) == type([0, 0, 0]):
        for i in range(len(m[0])):
            a = []
            for j in range(len(m)):
                a.append(m[j][i])
            arr.append(a)
    # the array is onedimensional
    if type(m[0]) == type(0):
        for i in range(len(m)):
            a = [m[i]]
            arr.append(a)
    return arr

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
            x += str(array[i][j]).rjust(max_max)
            if j != len(array[i]) - 1:
                x += " "
            else:
                x += "\n"

    return x

arr1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
arr2 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]]
arr3 = [5, 6, 7, 8]

print(display_arr(arr1))
print()
print(display_arr(transpose_matrix(arr1)))
print()
print("-----")
print()
print(display_arr(arr2))
print()
print(display_arr(transpose_matrix(arr2)))
print()
print("-----")
print()
print(arr3)
print()
print(display_arr(transpose_matrix(arr3)))