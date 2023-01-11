# Create a dictionary that describes your favourite book or film with at least five key-value pairs.
# Then create a program that writes the dictionary data to the favourite.json file. Use the dump() method.
# Note the formatting of the data in the json file. Use the 'indent' parameter in the dump() method.

import json

book = {
    "title": "Harrow the Ninth",
    "author": "Tamsyn Muir",
    "series": "The Locked Tomb Series",
    "# in series": 2,
    "year": 2020
    }

with open("favourite.json", "w") as f:
    json.dump(book, f, indent=4)