# In the Arrays class, add three static methods that:

import random

class Arrays():

    @staticmethod
    def print_in_col(array):
        for c in array:
            print(c)
    
    @staticmethod
    def print_in_row(array):
        x = ""
        for c in array:
            x += str(c) + ", "
        x = x.rstrip(", ")
        print(x)

# a.	create an array with a given number of elements with the same values. Use list.append():
#     method_name(number_of_array_elements, value_of_array_elements)

    @staticmethod
    def value_array(number_of_array_elements, value_of_array_elements):
        arr = []
        for i in range(number_of_array_elements):
            arr.append(value_of_array_elements)
        return arr

# b.	create an array with a given number of elements and the random value of these elements in the range of <m, n>:
#     method_name(number_of_array_elements, value_from, value_to)

    @staticmethod
    def random_array(number_of_array_elements, value_from, value_to):
        arr = []
        for i in range(number_of_array_elements):
            arr.append(random.randint(value_from, value_to))
        return arr

# c.	determines the number of array elements whose values are in the given range <m, n>:
#     method_name(array, value_from, value_to)

    @staticmethod
    def determine_range(array, value_from, value_to):
        count = 0
        for i in array:
            if i >= value_from and i <= value_to:
                count +=1
        return count

# Then, write a program that creates a 10-element array with element values equal to 4
# and a 20-element array of random integers in the range of <-7,8>.
# Display the contents of arrays and calculate how many values between <-1,1> are contained in a 20-element array.

arr1 = Arrays.value_array(10, 4)
print("Array 1:")
Arrays.print_in_row(arr1)
print()

arr2 = Arrays.random_array(20, -7, 8)
print("Array 2:")
Arrays.print_in_row(arr2)
print()

c = Arrays.determine_range(arr2, -1, 1)
print(f"There're {c} values between <-1,1> in Array 2.")