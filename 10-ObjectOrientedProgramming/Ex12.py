# In the TV class, make changes to the show_status() method so that it displays not only the selected channel number
# but also its name. When the selected channel number exceeds the list of available channels, the channel name is not displayed.

# TV is on, channel 4 (TVN)

# Then try using the TV. Set at least 7 channels (seven TV stations), change channel numbers and display TV status every time.

class TVset():

    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels = []
    
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
    
    def show_status(self):
        if self.is_on:
            if self.channel_no in range(1, len(self.channels) + 1):
                print("TV is on, channel", self.channel_no, f"({self.channels[self.channel_no - 1]})")
            else:
                print("TV is on, channel", self.channel_no)
        else:
            print("TV is off")

tv = TVset()
tv.set_channels(["TVP1", "TVP2", "Polsat", "TVN", "HBO", "Filmbox", "Discovery"])
tv.turn_on()
tv.show_status()
tv.set_channel(7)
tv.show_status()
tv.set_channel(10)
tv.show_status()
tv.turn_off()