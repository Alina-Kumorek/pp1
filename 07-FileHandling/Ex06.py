# In any text editor (e.g. Windows Notepad), create a file countries.txt in which save,
# in separate lines, names of five countries. Then create a program that displays the file content.

file = open('countries.txt','r')
file_content = file.read()
file.close()
print( file_content )