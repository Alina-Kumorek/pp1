# Create a program that displays the contents of the countries.txt text file. At the beginning of each line, display the line number.
# Tip: you have to read and display text file line by line.

# display text file, line by line
file = open('countries.txt','r')
for line in file:
     print(line, end="")
file.close()
