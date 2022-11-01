# Write a program that creates a multiplication table in the range 1 to 10 for any number entered by the user.

# get input
x = int(input("Enter number: "))

# display results
for i in range(1, 11):
    print(f"{x} x {i} = {x * i}")