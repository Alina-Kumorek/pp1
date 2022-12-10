# An array film_titles contains any five film titles. Write a program that writes the film titles to a text file, each title on a separate line.

film_titles = ["Titanic", "Shrek", "Mission Impossible", "Godfather", "Lord of the Rings"]

file = open("films.txt","w")

for i in film_titles:
    file.write(i + "\n") #There is a way to make it with print

file.close()