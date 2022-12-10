# An array contains integer numbers: 12, 6, 4, 9, 10.
# Create a program that displays the array values graphically as below.
# Define a function star(n) that returns the given number of asterisks as a string.
# Use a defined function in the program.
#     12: ************
#      6: ******
#      4: ****
#      9: *********
#     10: **********

def star(n):

    stars = ""
    
    for i in range(n):
        stars += "*"
    
    return stars

arr = [12, 6, 4, 9, 10]

for i in arr:

    # I think there's a simpler way of doing this
    if len(str(i)) < 2:
        print("", end=" ")
    
    print(f"{i}: {star(i)}")