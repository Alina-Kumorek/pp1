# Write a program that calculates a dog's age in dog’s years.
# For the first two years, a dog's life is equal to 10.5 human years.
# After that, each dog year is equal to 4 human years.

# get input
h = int(input("Enter the dog's age in human years: "))

# calculate age in dog years
if h == 0:
    d = 0
elif h == 1:
    d = 10.5
elif h == 2:
    d = 21
else:
    d = 21 + 4 * (h - 2)

# display output
print(f"The dog's age in dog’s years is {d} years.")