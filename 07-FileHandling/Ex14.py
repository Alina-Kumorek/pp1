# Write a program that calculates the number of lines for any text file.
# The user enters the name of the file from the keyboard.
# Display the result of the calculation (the file name and the number of lines).
# Do not display the contents of the file. Sample result:

#     File name: countries.txt
#     Number of lines: 14

name = input("File name: ")

f = open(name)
print(f"Number of lines: {len(f.readlines())}")
f.close()