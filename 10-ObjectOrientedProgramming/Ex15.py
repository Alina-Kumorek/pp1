# The medical thermometer measures the patient's temperature in the range from 34.0 to 42.0 degrees Celsius,
# with an accuracy of 0.1 degrees. Write a program in which define a class that describes the states and behaviors of the thermometer.
# The thermometer should enable temperature measurement (do it by generating a random number from the 34.0 to 42.0 range)
# and display the measured value. If the temperature is at least 37 degrees Celsius,
# the thermometer should additionally display the 'Fever' message, e.g.

# Temperature: 37.2C (fever)

# When the temperature is at least 41.0, the thermometer should additionally display the message 'CRITICAL TEMPERATURE!!'.
# Place the class definition and the main program in separate files. Then use the program and:
import thermometer

# a.	Create a thermometer
t = thermometer.Thermometer()

# b.	Turn thermometer on
t.turn_on()
t.display()

# c.	Measure temperature
t.measure()

# d.	Display temperature
t.display()

# e.	Turn thermometer off
t.turn_off()
t.display()