# Write a program where you create a dictionary containing student data.
# Try to describe a student in detail, using different data types that can be used in the dictionary.
# Then save the data about student in the file student.json, in a readable form.

import json

student = {
    "name": "John Doe",
    "birth_year": 1998,
    "grades": [3.0, 3.0, 4.0, 3.5, 5.0],
    "adress": {
        "city": "Cracow",
        "street": "Rakowicka",
        "building_number": 43,
        "apartment_number": 12
        }
    }

with open("student.json", "w") as f:
    json.dump(student, f, indent=4)