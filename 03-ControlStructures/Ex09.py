# A user enters two integer numbers from the keyboard.
# Write a program that checks if at least one of them is positive.

a = int(input("Integer A: "))
b = int(input("Integer B: "))

if a > 0 or b > 0:
    print("At least one is positive.")
else:
    print("At least one isn't positive.")