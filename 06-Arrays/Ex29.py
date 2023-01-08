# Write a program that, for the given array of real numbers, displays the number of elements
# that are greater than the given value entered from the keyboard.

import random

arr = []

for i in range(random.randint(4, 30)):
    arr.append(random.random()*random.randint(-100, 100))

print(f"Array: {arr}")

val = float(input("Enter a value: "))

count = 0
for i in arr:
    if i > val:
        count += 1

print(f"There is {count} elements greater than {val}")