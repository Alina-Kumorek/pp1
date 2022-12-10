# Create a program that displays the name of month for a given month number (1 to 12).
# Define a month(n) function that returns the name of month for the number n. Store month names in an array.
# Using defined function, display month names for the following month numbers: 1, 2, 11, 12.

def month(n):
    arr = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    return arr[n-1]

print(f"1:\t{month(1)}\n2:\t{month(2)}\n11:\t{month(11)}\n12:\t{month(12)}")