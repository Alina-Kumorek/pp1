# The variables a and b contain the dimensions of the sides of the rectangle.
# Write a program that creates the following rectangle with dimensions a and b.
# Example result for a = 4 and b = 15:

a = 4
b = 15

for i in range(a):

    m = ""

    if i == 0 or i == a - 1:

        for j in range(b):
            m += "*"
    
    else:

        m += "*"

        for j in range(b - 2):
            m += " "
        
        m += "*"
    
    print(m)