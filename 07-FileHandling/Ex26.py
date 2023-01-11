# Find any text file on the Internet and download it to your computer.
# Then write a program that displays all words with at least six letters from the file.
# Display each word on a separate line. Use regular expressions.

import re

with open("pan-tadeusz.txt", encoding="UTF-8") as f:
    txt = f.read()
    long = re.findall("[a-zA-z]{6,}", txt)

for i in long:
    print(i)