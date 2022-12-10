# An array contains a list of Polish names: Genowefa, Onufry, Celestyna, Alojzy, Pankracy.
# Create a program that displays the longest name (consisting of the largest number of characters). Sample result:
    # Names: Genowefa Onufry Celestyna Alojzy Pankracy
    # Longest name: Celestyna

arr = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]

max = ""

for i in arr:
    if len(i) > len(max):
        max = i

print("Names:", end=" ")
for i in arr:
    print(i, end=" ")
print()

print(f"Longest name: {max}")