# The grades.txt file contains student’s grades. Create the file in any text editor.

#     Name: Peter
#     Grades: 3.5, 4.0, 5.0, 4.5, 3.5, 3.0, 5.0

# Then create a program that calculates the arithmetic mean of student’s grades.

import re

with open("grades.txt") as f:
    txt = f.read()

grades = re.findall("\d\.\d", txt)

grades.sort()
mean = grades[len(grades) // 2]

print(mean)