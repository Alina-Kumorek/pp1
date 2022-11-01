# The following function evaluates the factorial recursively.
# Analyze the program. Do you understand how it works?
# Then run the program and calculate the factorial value for n = 5.

def factorial(n):

    # 0! = 1, 1! = 1
    if n==0 or n==1:
        return 1

    # n! = n * (n-1)!
    if n > 1:
        return n * factorial(n-1)
  
x = 5
print( f"{x}! = {factorial(x)}" )
