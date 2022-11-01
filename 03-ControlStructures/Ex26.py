# The payment card is secured with a four-digit PIN code (0805).
# Write a program that checks if the PIN code entered in the payment terminal is correct.
# The user has up to three possibilities for entering a PIN code. In case of three unsuccessful attempts, the card is blocked.

code = "0805"
x = ""
count = 0

while x != code:

    if count >= 3:
        print("Sorry, your payment card has been blocked.")
        break

    x = input("Enter the PIN code: ")

    if x == code:
        print("Correct.")
    else:
        count += 1
        print("Incorrect...")