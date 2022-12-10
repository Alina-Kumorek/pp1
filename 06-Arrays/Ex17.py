# Create a program that computes the second power of each array element. Sample result:
#     Array: 8 2 5 1 9
#     2nd power: 64 4 25 1 81

arr = [8, 2, 5, 1, 9]

print("Array:", end=" ")

for i in arr:
    print(i, end=" ")
print()

print("2nd power:", end=" ")

for i in arr:
    print(i**2, end=" ")
print()