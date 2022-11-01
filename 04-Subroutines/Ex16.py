# Each month of a calendar year can be expressed by its name or by a number that indicates the position of the month in year.
# Define a function month(n) that returns a month name based on the month number (values from 1 to 12).
# Then create a program and display the name of the month 7.

def month(n):
    if n == 1:
        return "january"
    if n == 2:
        return "february"
    if n == 3:
        return "march"
    if n == 4:
        return "april"
    if n == 5:
        return "may"
    if n == 6:
        return "june"
    if n == 7:
        return "july"
    if n == 8:
        return "august"
    if n == 9:
        return "septemper"
    if n == 10:
        return "october"
    if n == 11:
        return "november"
    if n == 12:
        return "december"

print(month(7))