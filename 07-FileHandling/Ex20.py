# Create a program that writes 50 random integers between 100 and 999 to a text file,
# each number on a separate line.

import random

integers = []

for i in range(1, 50):
    integers.append(f"{random.randint(100, 999)}\n")
integers.append(f"{random.randint(100, 999)}")

f = open("random.txt", "w")
f.writelines(integers)
f.close()