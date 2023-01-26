# Create a class that describes cell phones with at least 3 phone states and 2 behaviors.
# Define the text representation of an object. Then create 2 objects representing 2 phones.
# Display their features and call their bahaviors.

import random

class Cell_Phone():

    def __init__(self):
        self.is_on = False
        self.battery = 100
    
    def __str__(self):
        if self.is_on:
            return "The cell phone is ON. The battery has " + str(self.battery) + "% capacity left."
        else:
            return "The cell phone is OFF."

    def turn_on(self):
        if self.battery > 0:
            self.is_on = True
    
    def turn_off(self):
        self.is_on = False
    
    def use_battery(self, amount = 10):
        if self.battery > amount:
            self.battery -= amount
        else:
            self.battery = 0
            self.turn_off()
    
    def charge(self):
        self.battery = 100
    
    def text(self, phone_num):
        if self.is_on:
            input("Enter the message: ")
            print(phone_num, "received your text message.")
            self.use_battery()
    
    def call(self, phone_num):
        if self.is_on:
            if random.random() > 0.2:
                print(f"Your call with {phone_num} lasted {random.randint(1, 60)} min.")
            else:
                print(phone_num, "haven't picked up.")
            self.use_battery(20)

p1 = Cell_Phone()
print(p1)
p1.turn_on()
print(p1)
p1.text(564274938)
p1.call(743846374)
print(p1)
p1.use_battery(80)
print(p1)
p1.charge()
p1.turn_on()
print(p1)