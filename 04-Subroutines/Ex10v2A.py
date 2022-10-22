# Define a function read_number() that returns an integer number entered from the keyboard.
# The function should print a text prompting user to enter the number 'Enter a number: '.
# Then use the function to read two numbers from the keyboard. Display their sum.

def read_number():
    x = int(input("Enter a number: "))
    return x

a = read_number()
b = read_number()

print(f"The sum of entered numbers is {x}")