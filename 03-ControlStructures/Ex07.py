# X contains any integer value. Write a program to check that the value is even.

x = int(input("Input an integer: "))

y = x % 2

if y == 0:
    print("The value is even.")
else:
    print("The value is odd.")
