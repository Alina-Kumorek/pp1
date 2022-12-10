# Define a function occurs(number, array) that returns True if a given number is present in an array.
# Then create a program that checks whether the number entered from the keyboard is present
# in the array [15, 38, 7, 23, 14]. Sample result:
#     Number: 23
#     Array: 15 38 7 23 14
#     Result: number 23 appears in the array

def occurs(number, array):
    if number in array:
        return True
    else:
        return False

arr = [15, 38, 7, 23, 14]

n = int(input("Number: "))

print("Array:", end=" ")
for i in arr:
    print(i, end=" ")
print()

print("Result:", end=" ")
if occurs(n, arr):
    print(f"number {n} appears in the array")
else:
    print(f"number {n} doesn't appear in the array")