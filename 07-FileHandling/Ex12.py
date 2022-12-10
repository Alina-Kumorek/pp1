# Create a program that allows you to add a name of next product you want to buy at the end of the text file shopping.txt.
# Enter the product name from the keyboard. Tip: open the file in appending mode.

x = input("Podaj nazwę produktu: ")

file = open("shopping.txt","a")
file.write(x + "\n")
file.close()