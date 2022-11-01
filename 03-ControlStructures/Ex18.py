# There are coins of 1, 2 and 5 Polish Zlotys (PLN).
# Write a program showing any amount (natural number) read from the keyboard with as few coins as possible.

# get input
x = int(input("Enter the amount in PLN: "))

# calculate amount of coins
c5 = x // 5
r = x - c5 * 5

c2 = r // 2
r = r - c2 * 2

c1 = r

# display results
print(f"""The amount of PLN {x} in coins:
5 zł – {c5} 
2 zł – {c2} 
1 zł – {c1}""")