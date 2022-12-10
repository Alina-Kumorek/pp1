# Create a dictionary as in the example below. Note the structure of the dictionary (key-value) and the value types in the example below.
# What type of value was used in each of the six key-value pairs?

person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming","excursions"],
    "married": True,
    "phone":{"landline":"123444321","mobile":"777888999"}
}

#     Then, create a program and do the following tasks:
#     a.	Display contents of the dictionary
print(person)

#     b.	Display name
print(person["name"])

#     c.	Display hobby
print(person["hobby"])

#     d.	Change surname to Nowak
person["surname"] = "Nowak"

#     e.	Change person's marriage status
person["married"] = False

#     f.	Add gender: male
person["gender"] = "male"

#     g.	Add a new hobby: bicycle
person["hobby"].append("bicycle")

#     h.	Add work phone to existing phones: 313131444
person["phone"]["work"] = "313131444"

print(person)