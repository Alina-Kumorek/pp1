# Define a function that displays numbers in the layout as below (like on a phone keypad).
# Apply an loop statement. Then call the function.

def keypad():

    x = 1

    for i in range(3):
        print (x, x + 1, x + 2)
        x += 3

keypad()