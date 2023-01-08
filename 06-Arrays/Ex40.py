# An array contains integer numbers: [[-38, 19], [5,40],[-7,11],[29,16]].
# Create a program that finds the smallest and largest values in the array and in which row and column they are located.

arr = [[-38, 19], [5, 40], [-7, 11], [29, 16]]

arr_min = arr[0][0]
min_row = 0
min_col = 0

arr_max = arr[0][0]
max_row = 0
min_row = 0

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] < arr_min:
            arr_min = arr[i][j]
            min_row = i
            min_col = j
        if arr[i][j] > arr_max:
            arr_max = arr[i][j]
            max_row = i
            max_col = j

print(arr)
print(f"Min:\t{arr_min}\nRow:\t{min_row}\tColumn:\t{min_col}")
print(f"Max:\t{arr_max}\nRow:\t{max_row}\tColumn:\t{max_col}")