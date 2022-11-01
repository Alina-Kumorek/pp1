# In the module mymath.py, create the following function definitions:
#   a.	read_number() that reads from the keyboard and returns integer number
#   b.	generate_number() that creates and returns random integer number in the range of <1,9>
# Then create a main program, in which, first import a module you created earlier.
# The program is a simple guessing game. The user enters a one-digit number from the keyboard.
# The computer then generates a random one-digit number. If the numbers match, the user wins the game. 

import mymath

x = mymath.read_number()

y = mymath.generate_number()

if x == y:
    print("You won!!!")
else:
    print("You lost :(")