# Create a class that represents pieces of music. Define a class constructor that allows you
# to set the initial values of the music piece (artist, track title, album, year) when the object is created.
# Complete the class with the __str__ method returning the song data as a string, in the format as below (4 lines).

#     Performer: Ed Sheeran
#     Song:      Hearts Don't Break Around Here
#     Album:     Divide
#     Year:      2017

# Then create three objects that represent three different pieces of music. Display these objects.

class MusicTrack():

    def __init__(self, artist, track_title, album, year):
        self.artist = artist
        self.track_title = track_title
        self.album = album
        self.year = year
    
    def __str__(self):
        x =  f"Performer:\t{self.artist}\n"
        x += f"Song:\t\t{self.track_title}\n"
        x += f"Album:\t\t{self.album}\n"
        x += f"Year:\t\t{self.year}"
        return x
    
song1 = MusicTrack("Ed Sheeran", "Hearts Don't Break Around Here", "Divide", 2017)
song2 = MusicTrack("My Chemical Romance", "Welcome to the Black Parade", "The Black Parade", 2006)
song3 = MusicTrack("Florence + the Machine", "King", "Dance Fever", 2022)

print(song1)
print()
print(song2)
print()
print(song3)