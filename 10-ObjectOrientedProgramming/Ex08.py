# Write a program in which you create a TV class that describes a TV set.
# The class should contain one boolean attribute called 'is_on' that specifies
# whether the TV set is turned on. Initially, the TV is turned off. Add turn_on() and
# turn_off() methods in the class to turn the TV on and off, respectively.
# Also add a show_status() method to display whether the TV is on or off.
# Sample message:

# TV is on

class TVset():

    def __init__(self):
        self.is_on = False
    
    def turn_on(self):
        self.is_on = True
    
    def turn_off(self):
        self.is_on = False
    
    def show_status(self):
        if self.is_on:
            print("TV is on")
        else:
            print("TV is off")

# Then try using the TV set in the program:
# a.	Create TV set
tv = TVset()
# b.	Show TV status
tv.show_status()
# c.	Turn TV on
tv.turn_on()
# d.	Show TV status
tv.show_status()
# e.	Turn TV off
tv.turn_off()
# f.	Show TV status
tv.show_status()