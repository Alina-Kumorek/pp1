import random

# read from the keyboard and return integer number
def read_number():
    return int(input("Enter a number: "))

# create and return random integer number in the range of <1,9>
def generate_number():
    return random.randint(1,9)