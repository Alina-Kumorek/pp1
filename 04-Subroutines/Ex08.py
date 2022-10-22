# Define a function that displays integer numbers from 1 to N.
# Then call the function and display numbers from 1 to 15.

def display_integers(n):

    for i in range(1, n + 1):
        print(i, end = " ")

display_integers(15)