# Using the website https://mockaroo.com, generate a list of 500 students, containing the following data:
# name, surname, student ID, gender, age, year of study, email. Write the data to the students.json file.
# Then write a program that creates a limited.json file with the copy of the list of students, limited to data:
# first name, last name, student id.

import json

with open("students.json") as f1:
    s = json.load(f1)

keys1 = ["name", "surname", "student_id"]
keys2 = ["first_name", "last_name", "student_id"]
l = []

for i in s:
    x = {}
    for j in range(len(keys1)):
        x[keys2[j]] = i[keys1[j]]
    l.append(x)

with open("limited.json", "w") as f2:
    json.dump(l, f2, indent=4)