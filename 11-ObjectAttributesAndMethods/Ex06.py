# An attribute created outside of the __init__ method is a class attribute.
# A class attribute holds a value that is common (and therefore identical) to all objects created from that class.

# Run the program below. Note how the class attribute is declared and how it is modified.
# Specify a class attribute in the program, the place where it is modified and the place where its value was used.

# class definition
class Film():
    
    # class variables
    cinema = "Multikino"
    
    def __init__(self, title):
        self.title = title
    
    def __str__(self):
        return f"{self.title} ({Film.cinema})"
    
# program
film1 = Film("The Shawshank Redemption")
print(film1)
film2 = Film("Pulp Fiction")
print(film2)

# renaming the cinema (changing the value
# of a class variable) 
Film.cinema = "Cinema City"
print(film1)
print(film2)