# Define a function that checks if the number is within the given range <x, y>.
# The function returns boolean value. Then create a program and use the function you defined.

def check_range(number, x, y):
    
    if number >= x and number <= y:
        return True
    else:
        return False


number = int(input("Enter a number: "))
x = int(input("Enter the lower end of the range: "))
y = int(input("Enter the upper end of the range: "))

if check_range(number, x, y):
    print("Entered number is in the provided range.")
else:
     print("Entered number is NOT in the provided range.")