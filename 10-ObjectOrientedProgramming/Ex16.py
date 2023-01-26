# The bank account has a 26-digit number assigned when creating an account. The initial account balance is PLN 0.
# You can deposit any amount on the account. You can also withdraw any amount from the account,
# provided that it does not exceed the account balance. If you try to withdraw a larger amount,
# the following message will be displayed: "Insufficient funds on the account". At any time, it is possible to display
# information about the number and balance of the bank account in the following format:

# Bank Account No: 11 1111 1111 1111 1111 1111 1111
# Balance: PLN 25,38

# Create a program that handles the bank account.
#     a.	Familiarises yourself with a problem.
#     b.	Identify an object
#     c.	Define the states and behaviors of the object.
#     d.	Transform the states and behaviors of the object into the fields and methods of the class that will serve as
#           a pattern for creating an object.
#     e.	Create a sketch of the class without creating any method content.
#     f.	Create the content of each method.

class Account():
    
    def __init__(self, account_no):
        self.account_no = account_no
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"You have deposited PLN {amount} successfully.")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds on the account")
        else:
            self.balance -= amount
            print(f"You have withdrawn PLN {amount} successfully.")
    
    def display(self):
        n = str(self.account_no)
        print("Bank Account No:", end=" ")
        print(n[:2], end="")
        for i in range(6):
            print(" " + n[i*4+2:i*4+6], end="")
        print()

        b = self.balance // 1
        r = self.balance - b
        r = str(r)
        print("Balance: PLN", str(b).removesuffix(".0") + ".", end="")
        if len(r) <= 4:
            print(r.ljust(2, "0"))
        else:
            print(r[2:4])

# Then use the program and:
# g.	Create a bank account with the number 12 3456 5555 9090 1111 0000 7722
acc = Account(12345655559090111100007722)

# h.	Display account balance
acc.display()

# i.	Deposit PLN 25,30
acc.deposit(25.30)

# j.	Display account balance
acc.display()

# k.	Withdraw PLN 31,70
acc.withdraw(31.70)

# l.	Display account balance
acc.display()

# m.	Withdraw PLN 14
acc.withdraw(14)

# n.	Display account balance
acc.display()
