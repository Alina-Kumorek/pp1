# In the TV class, add support for volume adjustment in the range 0 to 10. The initial value of the volume level is 0.
# Add two methods to increase and decrease the TV volume level by one. Note that you cannot increase or decrease
# the volume beyond the specified range. Display the current volume level in the show_status() method.
# Then check the operation of the TV by adjusting and displaying its volume level.

class TVset():

    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels = []
        self.volume = 0
    
    def turn_on(self):
        self.is_on = True
    
    def turn_off(self):
        self.is_on = False

    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no

    def set_channels(self, channels_list):
        self.channels = channels_list
    
    def show_channels(self):
        print("Channel list:")
        for i in range(len(self.channels)):
            print(f"{i+1}. {self.channels[i]}")
    
    def increase_vol(self):
        if self.volume < 10:
            self.volume += 1
    
    def decrease_vol(self):
        if self.volume > 0:
            self.volume -= 1
    
    def show_status(self):
        if self.is_on:
            print("TV is on, channel", self.channel_no, end="")
            if self.channel_no in range(1, len(self.channels) + 1):
                print(f" ({self.channels[self.channel_no - 1]})", end="")
            print(", volume", self.volume)
        else:
            print("TV is off")

tv = TVset()
tv.set_channels(["TVP1", "TVP2", "Polsat", "TVN", "HBO", "Filmbox", "Discovery"])
tv.turn_on()
tv.show_status()
tv.decrease_vol()
tv.show_status()
for i in range(10):
    tv.increase_vol()
tv.show_status()
tv.increase_vol()
tv.show_status()
tv.decrease_vol()
tv.show_status()
tv.turn_off()
tv.show_status()