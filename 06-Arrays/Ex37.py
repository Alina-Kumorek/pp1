# A two-dimensional array contains the following numbers:
#     7 3 7 9 0
#     2 9 0 1 5
#     3 8 6 4 7
#     8 7 1 1 5
# Create a program that calculates the sum of values in the last column.

arr = [[7, 3, 7, 9, 0], [2, 9, 0, 1, 5], [3, 8, 6, 4, 7], [8, 7, 1, 1, 5]]

arg = len(arr[0]) - 1
count = 0

for i in range(len(arr)):
    count += arr[i][arg]

print(arr)
print(count)