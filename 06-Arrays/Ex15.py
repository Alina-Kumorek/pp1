# An array contains values: [[0,0,0],[0,0,0],[0,0,0]].
# Create a program that replaces the values of the main diagonal with 1. Use loop statements.
# Display the modified array as below:
#     1 0 0
#     0 1 0
#     0 0 1

arr = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(arr)):
    arr[i][i] = 1

for i in arr:
    for j in i:
        print(j, end=" ")
    print()