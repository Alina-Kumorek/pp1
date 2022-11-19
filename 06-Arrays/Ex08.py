# An array contains numbers: -15, 8, -31, 47, -2, 19. Create a program that finds and displays the maximum and minimum number. Do not use available functions.

arr = [-15, 8, -31, 47, -2, 19]

for i in range(len(arr)):
    if i == 0:
        min = arr[i]
        max = arr[i]
    else:
        if arr[i] < min:
            min = arr[i]
        elif arr[i] > max: # z jakiś powodów elif jest brzydki w tym wypadku
            max = arr[i]

print(f"{arr}\nmax:\t{max}\nmin:\t{min}")
