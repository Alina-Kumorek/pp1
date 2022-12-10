# Create an array with 5 dictionaries, each containing a country and its population. Then, using ‘while’ loop, display the array contents.

countries = [
    {"country": "Poland", "population": 38036118},
    {"country": "Germany", "population": 83695430},
    {"country": "France", "population": 67897000},
    {"country": "Spain", "population": 47163418},
    {"country": "Italy", "population": 58853482}
    ]

# for i in countries:
#     for k, v in i.items():
#         print(f"{k}: {v}")

while countries: #Nie lubi nie używać konkretnego warunku
    x = countries.pop(0)
    for k, v in x.items():
        print(f"{k}: {v}")