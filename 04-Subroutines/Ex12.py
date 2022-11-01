# Define a function sum(N) that for the given natural number N calculates the sum of all natural numbers between 1 and N.
# Apply recursion. Then create a program that calculates the sum of natural numbers in the range <1,10>.

def sum(n):

    if n == 1:
        return 1
    
    if n > 1:
        return n + sum(n - 1)

x = 10
print(f"The sum of natural numbers in the range <1,{x}>: {sum(x)}")