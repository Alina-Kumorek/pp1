# Find any text file on the Internet and download it to your computer.
# Then write a program that copies the contents of this file to the copylines.txt file.
# Copy the contents of the file line by line.
# Finally, open both files in any text editor and check that their contents are the same.

f1 = open("sample1.txt")
f2 = open("copylines.txt", "w")

for line in f1:
    f2.write(line)

f1.close()
f2.close()