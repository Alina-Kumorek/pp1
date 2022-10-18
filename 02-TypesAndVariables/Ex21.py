###
# Guessing game against computer
###

import random

number = random.randint(1, 6)

guess = int(input("Guess the number (1-6): "))

if number == guess:
    print("True")