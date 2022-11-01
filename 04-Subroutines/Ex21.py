# Define an anonymous function that returns true when the first number is greater than the second one.
# Otherwise returns false. Use the conditional operator.

isGreater = lambda x, y: x > y

x = str(input("Enter the first number: "))
y = str(input("Enter the second number: "))

print(f"The first number is grater than the second one: {isGreater(x, y)}")