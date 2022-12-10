# Create a program that displays all unique elements in an array. Sample result:
#     Array: 2 3 2 5 8 1 9 8
#     Unique elements: 3 5 1 9

arr = [2, 3, 2, 5, 8, 1, 9, 8]

print("Array:", end=" ")
for i in arr:
    print(i, end=" ")
print()

rejected = []
unique = []

for i in range(len(arr)):
    x = arr.pop()
    if x not in rejected:
        if x not in arr:
            unique.insert(0, x)
        else:
            rejected.append(x)

print("Unique elements:", end=" ")
for i in unique:
    print(i, end=" ")
print()