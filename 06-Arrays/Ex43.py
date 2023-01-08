# Create a function identity_matrix(n) that returns an identity matrix of size n
# (https://en.wikipedia.org/wiki/Identity_matrix).
# Then create a function that displays a 2D array in rows and columns.
# Finally, create a program that displays three identity matrices with dimensions of 3, 5 and 8.

def identity_matrix(n):
    arr = []
    for i in range (n):
        a = []
        for j in range(n):
            if i == j:
                a.append(1)
            else:
                a.append(0)
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

print(display_arr(identity_matrix(3)))
print()
print(display_arr(identity_matrix(5)))
print()
print(display_arr(identity_matrix(8)))