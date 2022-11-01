# Write a program that creates the following pattern.

msg = ""
r = 10

for i in range(1, r):
    if i <= r / 2:
        for j in range(i):
            msg += "* "
    else:
        for j in range(r - i):
            msg += "* "
    msg += "\n"

print(msg)