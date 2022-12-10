# Create a program that saves, in separate lines, your name and surname, university name and field of study in a text file. 
# Tip: open a file in writing mode and then use the write() method.

file = open('my_data.txt','w')
file.write("Alina Kumorek\nUniwersytet Ekonomiczny w Krakowie\nInformatyka Stosowana")
file.close()