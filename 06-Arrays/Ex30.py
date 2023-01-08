# Create a function minmax(array) that, for the given array of integers,
# returns a two-element array containing the smallest and largest values in the given array.
# Sample result:

#     Array:  [4,2,8,4,7,9,5]
#     Result: [2,9]

def minmax(array):
    return [min(array), max(array)]

arr = [4,2,8,4,7,9,5]

print(f"Array:\t{arr}")
print(f"Result:\t{minmax(arr)}")