from osc4py3.as_eventloop import *
from osc4py3 import oscmethod as osm
import random
import socket
import warnings
import matplotlib
import scipy.signal as signal


warnings.filterwarnings("ignore", category=matplotlib.cbook.mplDeprecation)


dlist = []
avlist = []

def normnumpy(hz,intensity,  dlist):

    B, A = signal.butter(intensity, hz, output='ba')

# Second, apply the filter
    tempf = signal.filtfilt(B,A, dlist)
    print(tempf, "tempf")
    return(tempf)

def SwitchThreshold(value, threshold=0.5):
    if value <= threshold:
        return 0
    else:
        return 1

def Average(drange, dlist):
    dtot = 0
    if len(dlist) < 1:
        return dlist[:-1]
    if drange > len(dlist):
        drange = len(dlist)
    for x in range((len(dlist)-drange)-1, len(dlist)-1):
        dtot += dlist[x]
    avg = dtot/drange
    return avg

def managelistlenght(list, sizelimit):
    while len(list) > sizelimit:
        del list[0]




class NGIMULNK():
    def __init__(self):
        self.sensors = [Average(50, 100, "/analogue"),
                        Average(10, 100, "/quaternion"),
                        Average(1, 100, "/battery"),
                        Average(50, 100, "/linear"),
                        Average(50, 100, "/altitude"),
                        ]

        self.send_address = '192.168.1.97', 9000
        self.receive_address = '192.168.1.187', 8097

        self.c = OSC.OSCClient()
        self.c.connect(self.send_address)
        self.msg = OSC.OSCMessage()
        self.msg.setAddress('/wifi/send/ip')
        self.msg.append(str(socket.gethostbyname(socket.gethostname())))
        self.c.send(self.msg)
        self.c.close()

        self.s = OSC.OSCServer(self.receive_address)

        self.s.addDefaultHandlers()
        self.s.addMsgHandler("/sensors", self.sensorsHandler)
        self.s.addMsgHandler("/quaternion", self.quaternionHandler)
        self.s.addMsgHandler("/battery", self.batteryHandler)
        self.s.addMsgHandler("/linear", self.linearHandler)
        self.s.addMsgHandler("/altitude", self.altitudehandler)
        self.s.addMsgHandler("/analogue", self.analogueHandler)
        self.s.addMsgHandler("/wifi/send/ip", self.dontdo)
        self.s.addMsgHandler("/error", self.errorhandler)



    def RandomNewData(self):
        number = random.randrange(0,10)
        self.analogueHandler(args=[(number*0.1),"_"])

    def sensorsHandler(self, add, tags, args, source):
        pass

    def quaternionHandler(self, add, tags, args, source):
        pass
        # self.sensors[1].newInput(args[0])

    def batteryHandler(self, add, tags, args, source):
        pass

    def linearHandler(self, add, tags, args, source):
        pass
        # self.sensors[3].newInput(args[0])

    def altitudehandler(self, add, tags, args, source):
        pass
        # self.sensors[4].newInput(args[0])

    def analogueHandler(self, add, tags, args, source):
        self.sensors[0].newInput(args[0])

    def errorhandler(self, add, tags, args, source):
        pass

    def dontdo(self, add, tags, args, source):
        pass




# Todo : Fonctions : ( remove eye movement; remove the row or low cut the pike, Find jighest frequency, create profiles based on frequencys)


""" get meditation datas and set as base
    




"""
