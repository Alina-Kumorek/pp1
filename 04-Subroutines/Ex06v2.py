# Define a function that displays numbers in the layout as below (like on a phone keypad).
# Apply an loop statement. Then call the function.

def keypad():

    for i in range(1, 8, 3):
        print (i, i + 1, i + 2)

keypad()