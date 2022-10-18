###
# Calculate body mass index
###

# Get data
h = float(input("Enter your height in cm: "))
m = float(input("Enter your weight in kg: "))

# Calculate
bmi = m / (h / 100) ** 2

# Display
print("BMI index:", bmi)