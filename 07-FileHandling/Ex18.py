# Using any text editor, create the following two text files:

#     MeatAndFish.txt
#     Skinless white meat
#     Tuna fish
#     Luncheon meat
#     Lean cuts of red meat

#     GrainsAndBread.txt
#     Bread
#     Rice
#     All purpose flour
#     Breakfast cereal
#     Pasta 

# Then write a program that creates a shoppinglist.txt file, in which save the contents
# of the MeatAndFish.txt and the GrainsAndBread.txt files.

files = ["MeatAndFish.txt", "GrainsAndBread.txt"]
endF = open("shoppinglist.txt", "w")

for file in files:
    f = open(file)
    for line in f:
        endF.write(line)
    endF.write("\n")
    f.close()

endF.close()