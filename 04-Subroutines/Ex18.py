# Define a function that calculates the sum of number digits.
# Then use the function to calculate the sum of digits in the number 7182.

def sum_of_digits(number):

    number = str(number)
    count = 0

    for i in number:
        count += int(i)
    
    return count


print(sum_of_digits(7182))