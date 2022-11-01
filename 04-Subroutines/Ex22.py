# Define an anonymous function that returns true when the number is even.

isEven = lambda number: number % 2 == 0

number = int(input("Enter a number: "))

print(f"Is the number ever?\t{isEven(number)}")