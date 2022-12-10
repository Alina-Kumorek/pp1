# Find any text file on the Internet and download it to your computer. Then write a program that displays its contents.

file = open('sample1.txt','r')
file_content = file.read()
file.close()
print( file_content )