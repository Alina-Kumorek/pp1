# Define a function rand_elem(array) that returns a randomly selected array element.
# Using the function, display a few randomly selected array elements.

def rand_elem(array):
    import random
    return array[random.randint(0, len(array) - 1)]

import random

arr = []
for i in range(random.randint(3, 20)):
    arr.append(random.randint(0, 99))

print(arr)
print(rand_elem(arr))
print(rand_elem(arr))
print(rand_elem(arr))