# Write a program that creates the following pattern.

msg = ""

for i in range(1, 10):
    for j in range(i):
        msg += str(i)
    msg += "\n"

print(msg)