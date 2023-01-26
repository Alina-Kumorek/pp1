# Add a set_name() method in the University class that allows you to rename the university
# (change the field value).

# def set_name(self, name):
#     self.name = name

# Then modify the program to change the name of the university in the created object.
# Enter MIT which stands for Massachusetts Institute of Technology, and display this changed name.

class University():

    # object constructor (__init__ method)
    def __init__(self):
        # object attributes (object features)
        self.name = 'CUE'    

    # object methods (object behaviors)
    def print_name(self):  
        print(self.name)
    
    def set_name(self, name):
        self.name = name

u = University()
u.set_name("MIT")
u.print_name()