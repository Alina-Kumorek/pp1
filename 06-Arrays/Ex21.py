# Define a function compare(array1, array2) that returns True if both arrays are the same.
# Arrays are the same if they have the same number of elements and values of elements in cells
# of arrays with the same index are equal. Then create a program and try to compare the following arrays: 
#     a.	["water","book","sky"]   ["water","book","sky"]
#     b.	[True,False]   [True,False,True]
#     c.	[5,3,1]   [5,3,1]
#     d.	[3,2,1]   [3,2]
# Display both arrays and the result of comparison. Sample result:
#     Array1: water book sky
#     Array2: water book sky
#     Comparison: arrays are the same

def compare(array1, array2):

    comp = True

    if len(array1) != len(array2):
        comp = False
    else:
        for i in range(len(array1)):
            if array1[i] != array2[i]:
                comp = False
    
    return comp

# arr1 = ["water","book","sky"]
# arr2 = ["water","book","sky"]

# arr1 = [True,False]
# arr2 = [True,False,True]

# arr1 = [5,3,1]
# arr2 = [5,3,1]

arr1 = [3,2,1]
arr2 = [3,2]

print("Array1:", end=" ")
for i in arr1:
    print(i, end=" ")
print()

print("Array2:", end=" ")
for i in arr2:
    print(i, end=" ")
print()

print("Comparison:", end=" ")
if compare(arr1, arr2):
    print("arrays are the same")
else:
    print("arrays are different")