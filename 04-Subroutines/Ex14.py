# Define an anonymous function that calculates the body mass index (BMI)
# for the given weight in kg and height in cm. Then calculate BMI for Peter (81kg, 182cm).

bmi = lambda m, h: m / ( h / 100) ** 2

print(f"Peter's BMI: {bmi(81, 182)}")