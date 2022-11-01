# A natural number greater than 1 is called a prime if it has exactly
# 2 natural factors with the values 1 and this number.
# Write a program that finds N leading prime numbers.
# Read the value of N from the keyboard.
# Using loop statements check that the number N is divisible only by 1 and by N.

# Prime numbers: 2 3 5 7 11 …


# get N
n = int(input("The amount of prime numbers to calculate: "))

print("Prime numbers:", end="")

# loop until you find N prime numbers
count = 0
number = 2

while count < n:

    isPrime = True

    # check if number is a prime number
    for i in range(2, number):
        if number % i == 0:
            isPrime = False
        
    # when the checked number is prime
    if isPrime == True:
        count += 1
        print(f" {number}", end="")
        
    # update checked number
    number += 1