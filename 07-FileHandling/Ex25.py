# Write a program that computes the number of words in the following text. Use regular expressions.
#     To be, or not to be, that is the question

import re

txt = "To be, or not to be, that is the question"
words = re.findall("[a-zA-Z]+", txt)
num = len(words)
print(num)