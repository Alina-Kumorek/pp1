###
# Reading temperature in degrees Celcius from the keybord
# and converting it to Kelvin and Fagrenheit
###

# read temperature from the keyboard
c = int(input("Temperatura [°C]: "))

# convert to Kelvin
k = c + 273.15

# convert to Fahrenheit
f = (9/5) * c + 32

# display results
print(f"{k} K, {f} °F")