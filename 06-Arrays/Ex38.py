# A function create_2d_arr(x,y) creates and returns two dimensional array with values of 0.
# Create a program and the function. Then create a two-dimensional array with dimensions of 3 by 5.
# Display the created array.

def create_2d_arr(x,y):
    arr = []
    for i in range (y):
        a = []
        for j in range(x):
            a.append(0)
        arr.append(a)
    return arr

print(create_2d_arr(3, 5))