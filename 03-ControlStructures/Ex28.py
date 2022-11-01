# Write a program that displays the first fifty words of the Fibonacci sequence.
# The sequence is defined as follows: the first term is equal to 0, the second is equal to 1,
# each subsequent term is the sum of the previous two. Sample result below.

# https://en.wikipedia.org/wiki/Fibonacci_number
# 0 1 1 2 3 5 8 13 21 34 ...

for i in range(50):
    if i == 0:
        l2 = 0
    elif i == 1:
        l1 = l2
        l2 = 1
    else:
        sum = l1 + l2
        l1 = l2
        l2 = sum
    
    print(l2, end=" ")