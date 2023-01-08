# Write a program to separate even and odd numbers of a given array of integers.
# Put all even numbers first, and then odd numbers.

import random

arr = []

for i in range(random.randint(3, 20)):
    arr.append(random.randint(0, 99))

print(f"Array: {arr}")

even = []
odd = []

for i in arr:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

sep = even + odd

print(f"Separated: {sep}")