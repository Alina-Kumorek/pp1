# Write a program that calculates the sum and arithmetic mean of numbers entered from the keyboard.
# Entering 0 ends entering numbers.

number = None
count = 0
sum = 0

while number != 0:

    if number != None:
        count += 1
        sum += number

    number = int(input("Enter number: "))

mean = sum / count

print(f"RESULT: Quantity={count}, Sum={sum}, Mean={mean}")