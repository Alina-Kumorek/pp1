# In any text editor, create a file numbers.txt in which save, in separate lines, integer numbers.
# Then write a program that reads numbers from the numbers.txt file and calculates their sum.
# Tip: Read the next line from the file and convert it into a numeric value.

file = open('numbers.txt','r')
sum = 0
for number in file:
     sum += int(number)
file.close()
print(sum)