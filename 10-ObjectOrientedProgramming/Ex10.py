# Add the set_channel(new_channel_no) method in the TV class to set the TV channel number.
# Then try using the TV set.

class TVset():

    def __init__(self):
        self.is_on = False
        self.channel_no = 1
    
    def turn_on(self):
        self.is_on = True
    
    def turn_off(self):
        self.is_on = False

    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no
    
    def show_status(self):
        if self.is_on:
            print("TV is on, channel", self.channel_no)
        else:
            print("TV is off")

# a.	Create a TV set
tv = TVset()
# b.	Show TV status
tv.show_status()
# c.	Turn TV on
tv.turn_on()
# d.	Show TV status
tv.show_status()
# e.	Change TV channel to 5
tv.set_channel(5)
# f.	Show TV status
tv.show_status()
# g.	Turn TV off
tv.turn_off()
# h.	Show TV status 
tv.show_status()