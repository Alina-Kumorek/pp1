import random

class Thermometer():

    def __init__(self):
        self.is_on = False
        self.temp = None
    
    def turn_on(self):
        self.is_on = True
    
    def turn_off(self):
        self.is_on = False
    
    def measure(self):
        if self.is_on:
            self.temp = 34 + random.randint(0, 80) / 10
    
    def display(self):
        if self.is_on:
            if self.temp == None:
                print("Make a measurement!")
            else:
                print(f"Temperature: {self.temp}C", end="")
                if self.temp >= 41.0:
                    print(" CRITICAL TEMPERATURE!!")
                elif self.temp >= 37.0:
                    print(" (fever)")
                else:
                    print()