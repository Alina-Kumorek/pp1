###
# Three dice rolls
###

import random

dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)
dice3 = random.randint(1, 6)

sum = dice1 + dice2 + dice3

print(f"""
    dice 1:\t{dice1}
    dice 2:\t{dice2}
    dice 3:\t{dice3}
    sum:\t{sum}
    """)