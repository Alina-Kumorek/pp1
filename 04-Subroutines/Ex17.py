# Create a program that calculates how many times the given letter appears in any text.
# Then create a program and check how many times the letter e’ appears in the text below.
# Define a function for making calculations.

# You never get a second chance to make a first impression

def count_letters(letter, text):

    count = 0

    for i in text:
        if i == letter:
            count += 1
    
    return count

print(count_letters("e", "You never get a second chance to make a first impression"))