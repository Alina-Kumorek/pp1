# Search he Internet and familiarise yourself with RPN (Reverse Polish Notation).
# Then, write a program that calculates RPN expressions. RPN can be conveniently
# evaluated using a stack structure. A user can enter by the keyboard any number,
# an operator (+ - * / ) or the equal sign (=).
#     a.	If the entered value is a number, push the number on to the stack
#     b.	If the entered value is an operator, pop two items from the top of the stack,
#         do the calculation, and push the result of the operation on to the stack.
#     c.	If the entered value is an equal sigh, pop the final result from the stack
#         and display the result of calculation.

# Using the program, calculate the value of RPN expressions:
# 	Expression						RPN (Reverse Polish Notation)
# 	2 + 3 =							2 3 + =
# 	2 * (4 + 1) =					2 4 1 + * =
# 	(2 + 3) * ( 4 + 5) =			2 3 + 4 5 + * =
# 	8 / (3 + 1) * (3 - 2 + 4) = 	8 3 1 + / 3 2 – 4 + * =

import stack

list = " 0123456789+-*/"
operators = "+-*/"

isCorrect = False
while not isCorrect:
    exp = input("Expression [0-9, +, -, *, /, =]: ")

    if exp == "q":
        break

    isCorrect = True
    for i in exp[0:len(exp)-1]:
        if i not in list:
            isCorrect = False
    if not exp.endswith("="):
        isCorrect = False

for i in exp:
    if i.isnumeric():
        stack.push(int(i))
    elif i in operators:
        a = stack.pop()
        b = stack.pop()
        if i == "+":
            c = b + a
        elif i == "-":
            c = b - a
        elif i == "*":
            c = b * a
        elif i == "/":
            c = b / a
        stack.push(c)
    elif i == "=":
        end = stack.pop()

print("Result:", end)