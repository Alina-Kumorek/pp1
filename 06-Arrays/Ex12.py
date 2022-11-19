# An array contains values: [[2,5,4],[9,0,3]]. Create a program that displays:
#   a.	the array
#   b.	size of the array (number of rows and columns)
#   c.	value 5 from the array
#   d.	value 3 from the array
#   e.	second row of the array as below:
#       9 0 3
#   f.	all values from the array as below:
#       2 5 4 
#       9 0 3
#   g.	last column of the array as below:
#       4
#       3

arr = [[2,5,4],[9,0,3]]

print(arr)
print(f"rows:\t\t{len(arr)}\ncolumns:\t{len(arr[0])}")
print(arr[0][1])
print(arr[1][2])

for i in arr[1]:
    print(i, end=" ")
print()

for i in arr:
    for j in i:
        print(j, end=" ")
    print()

for i in arr:
    print(i[-1])