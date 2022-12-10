# Find any JSON file on the Internet and download it to your computer.
# Open the file in any character editor and read its contents.
# Then write a program that displays the contents of the JSON file. Use the program code below.

import json

with open("countries.json") as file:
    data = json.load(file)

for i in data:
    for k,v in i.items():
        print(k,":",v)
