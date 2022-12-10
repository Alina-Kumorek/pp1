# Write a program that displays the difference between the largest and smallest values in an array of integers.
# Sample result:
#     Array: [5,1,9,6,1]
#     Result: 8

arr = [5,1,9,6,1]

# Determine for first two elements
if arr[0] < arr [1]:
    smallest = arr [0]
    largest = arr [1]
else:
    smallest = arr [1]
    largest = arr [0]

# Check entire array
for i in range(2, len(arr)):
    if arr[i] < smallest:
        smallest = arr[i]
    elif arr[i] > largest:
        largest = arr[i]

# Calculate the difference
difference = largest - smallest

# Print results
print(f"Array: {arr}\nResult: {difference}")