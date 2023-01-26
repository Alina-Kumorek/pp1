# A static method is the kind of method that is called in the context of a class,
# not objects that are created from that class. The following program defines a static method.

# class Arrays():

#     @staticmethod
#     def print_in_col(array):
#         for c in array:
#             print(c)
            
# my_array = [4,1,8,7,2]
# Arrays.print_in_col(my_array)

# Then complete the class with another static method that displays the contents of an array in a row,
# separating the values with a comma. Make sure that the comma is not displayed after the last value.
# Call a new method in the program.

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
            
my_array = [4,1,8,7,2]
Arrays.print_in_col(my_array)
print()
Arrays.print_in_row(my_array)