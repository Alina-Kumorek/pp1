# Write a program to find the second largest element in an array. Sample result:
#     Array: [5,1,9,6,1]
#     Result: 6

arr = [5,1,9,6,1]

# Find the largest element
largest = arr[0]

for i in arr:
    if i > largest:
        largest = i


# Find an element that is different that the largest one
second = largest
count = 0

while second == largest:
    if arr[count] != largest:
        second = arr[count]
    else:
        count += 1

# Find the second largest element
for i in range(count, len(arr)):
    if arr[i] > second and arr[i] < largest:
        second = arr[i]

# Print results
print(f"Array: {arr}\nResult: {second}")