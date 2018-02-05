# example
import pysimpledmx.pysimpledmx as pysimpledmx

mydmx = pysimpledmx.DMXConnection(3)

mydmx.setChannel(1, 255) # set DMX channel 1 to full
mydmx.setChannel(2, 128) # set DMX channel 2 to 128
mydmx.setChannel(3, 0)   # set DMX channel 3 to 0
mydmx.render()   # render all of the above changes onto the DMX network

mydmx.setChannel(4, 255, autorender=True) # set channel 4 to full and render to the network



## this should be a dmx configuration to call... like a profile. 
# to include : lights, channels, values, transition type, functions call for switching colors. 
class scene:
    class light:
        def __init__(self, name, channels, values):
            self.name = None
            self.channels_and_values = []
            if len(channels) == len(values):
                num = 0
                while num < len(channels):
                    self.channels_and_values.append((channels[num], values[num]))
                    num += 1

    def __init__(self):
        self.lights = {"lightname1": self.light("lightname1", [0,1,2,3], [255,255,30,cycle_sin])}
