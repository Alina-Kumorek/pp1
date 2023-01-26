# In the TV class, add the channels attribute containing a list of available TV channel names (array).
# Initially, the array should be empty (TV not programmed, no available channels).
# Add set_channels(channels_list) and show_channels() methods in the TV class,
# which allows you to set channels on the TV and display the list of available channels.
# Sample list of available channels:

# Channel list:
# 1. TVP1
# 2. TVP2
# 3. Polsat
# 4. TVN
# 5. Filmbox
# 6. Discovery

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
            print("TV is on, channel", self.channel_no)
        else:
            print("TV is off")

# Then try using the TV set:
# a.	Create a TV set
tv = TVset()
# b.	Show TV status
tv.show_status()
# c.	Turn TV on
tv.turn_on()
# d.	Show TV status
tv.show_status()
# e.	Display the list of available channels
tv.show_channels()
# f.	Set TV channels: TVP1, TVP2, Polsat, TVN, Filmbox, Discovery
tv.set_channels(["TVP1", "TVP2", "Polsat", "TVN", "Filmbox", "Discovery"])
# g.	Display the list of available channels
tv.show_channels()
# h.	Show TV status
tv.show_status()
# i.	Turn TV offs
tv.turn_off()