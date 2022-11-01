# A computer numeric keyboard has the arrangement of the keys as below.
# The included program code displays the computer keyboard.
# Analyse the program in terms of the displayed results.
# Do you understand each program statement?
# Then make a change in your program code. Replace the ‘for’ with a ‘while’ statement.

# 7 8 9     6+1 6+2 6+3
# 4 5 6     3+1 3+2 3+3
# 1 2 3     0+1 0+2 0+3

#for i in range(6,-1,-3):
#    for j in range(1,4):
#        print(f' {i+j}',end='')
#    print()

x = 6

while x >= 0:

    y = 1

    while y <= 3:
        print(f' {x+y}',end='')
        y += 1
    
    x -= 3
    print()