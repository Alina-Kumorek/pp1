# Define a function power(x, n) that evaluates x**n. Apply recursion. Then calculate 5***3.
#   Tip: xn =  x * x**(n-1)

def power(x, n):

    # x**0 = 0
    if n == 0:
        return 0
    
    # x**1 = x
    if n == 1:
        return x
    
    # x**n = x * x ** (n-1)
    if n > 1:
        return x * power(x, n-1)
    
print(power(5, 3))