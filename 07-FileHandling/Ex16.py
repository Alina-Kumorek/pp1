# Find any text file on the Internet and download it to your computer.
# Then write a program that copies the contents of this file to the copy.txt file.
# Copy the contents of the file as a whole. Finally, open both files in any text editor and check that their contents are the same.

f1 = open("sample1.txt")
f2 = open("copy.txt", "w")

f2.write(f1.read())

f1.close()
f2.close()