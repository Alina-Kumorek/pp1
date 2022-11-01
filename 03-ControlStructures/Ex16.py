# Write a program that displays two numbers entered from the keyboard in ascending order.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a < b:
    print(f"Numbers in ascending order: {a}, {b}")
elif a > b:
    print(f"Numbers in ascending order: {b}, {a}")