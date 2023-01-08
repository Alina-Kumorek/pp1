# The following program displays the contents of a file, line by line:
#     f = open("filename.txt")
#     for line in f:
#         print(line, end="")
#     f.close()
# Rewrite the program using the "with ..." as construct. Then check that the program is working properly.

f = open("filename.txt")

lines = f.readlines()
x = 0

while x < len(lines):
    print(lines[x], end="")
    x += 1

f.close()