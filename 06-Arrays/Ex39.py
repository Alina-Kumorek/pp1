# An array contains values: [[0,0,0,0,0],0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]].
# Create a program that modifies the array values to create a multiplication table as below.
# Use loop statements. Display the array.

#     1  2  3  4  5
#     2  4  6  8 10
#     3  6  9 12 15
#     4  8 12 16 20
#     5 10 15 20 25

def create_2d_arr(x,y):
    arr = []
    for i in range (y):
        a = []
        for j in range(x):
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
            x += str(arr[i][j]).rjust(max_max)
            if j != len(array[i]) - 1:
                x += " "
            else:
                x += "\n"
    
    return x

arr = create_2d_arr(5, 5)

for i in range(len(arr)):
    for j in range(len(arr[0])):
        arr[i][j] = (i + 1) * (j + 1)

print(display_arr(arr))