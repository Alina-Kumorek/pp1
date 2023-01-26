# Write a program in which create a University class, consisting of one field containing the name
# of the university and one method to display this name.

# class University():

#     # object constructor (__init__ method)
#     def __init__(self):
#         # object attributes (object features)
#         self.name = 'CUE'    

#     # object methods (object behaviors)
#     def print_name(self):  
#         print(self.name)

# Then create a University class object and call the method to display the name of the university.

class University():

    # object constructor (__init__ method)
    def __init__(self):
        # object attributes (object features)
        self.name = 'CUE'    

    # object methods (object behaviors)
    def print_name(self):  
        print(self.name)

u = University()
u.print_name()