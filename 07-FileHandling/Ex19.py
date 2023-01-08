# Create a program that writes to a text file integer numbers in the range of <1,50>,
# every number in a separate line.

integers = []
for i in range(1, 51):
    integers.append(f"{i}\n")

f = open("integers.txt", "w")
f.writelines(integers)
f.close()