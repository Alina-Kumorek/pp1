# Write a program that converts any natural number to a binary number. Use the stack.
# To convert a number, divide the number by 2,
# each time taking the remainder of the division and putting the remainder on the stack.
# Repeat the division until the number you are dividing is zero. Then pop and display all values from the stack.
# Sample result for number 18:
# 	Division	Remainder
# 	18 / 2 = 9	0
# 	9 / 2 = 4	1
# 	4 / 2 = 2	0
# 	2 / 2 = 1	0
# 	1  / 2 = 0	1
# Natural number: 18
# Binary number: 10010

import stack

d = int(input("Natural number: "))

while d != 0:
    stack.push(d % 2)
    d //= 2

b = ""
while not stack.empty():
    b += str(stack.pop())

print("Binary number:", b)