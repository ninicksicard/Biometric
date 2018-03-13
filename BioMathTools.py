from osc4py3.as_eventloop import *
from osc4py3 import oscmethod as osm
import random
import socket
import warnings
import matplotlib
import scipy.signal as signal
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, rfft, fftfreq, rfftfreq
from scipy.signal import blackman

warnings.filterwarnings("ignore", category=matplotlib.cbook.mplDeprecation)
dlist = []
avlist = []

# def normnumpy(hz,intensity,  dlist):
#
#     B = signal.butter(intensity, hz, output='ba')
#
# # Second, apply the filter
#     tempf = signal.filtfilt(B, A, dlist)
#     print(tempf, "tempf")
#     return(tempf)


def SwitchThreshold(value, threshold=0.5):
    if value <= threshold:
        return 0
    else:
        return 1


def dmx_inverted_exponential_half_max(value):

    dmx = -((32 * 10 * value)-16) ^ 2+255

    if dmx >= 255:

        return 255

    if dmx <= 0:

        return 0

    return dmx


def dmx_inverted_exponential_max(value):

    dmx = 255-(((value/16)-16)*((value/16)-16))

    if dmx >= 255:

        return 255

    if dmx <= 0:

        return 0

    return dmx


def dmx_exponential_half_max(value):

    dmx = (32 * value) ^ 2

    if dmx >= 255:

        return 255

    if dmx <= 0:

        return 0

    return dmx


def dmx_exponential_max(value):

    dmx = (16 * value) ^ 2

    if dmx >= 255:

        return 255

    if dmx <= 0:

        return 0

    return dmx


def average(list_to_average, avg_type="mine", average_range=None):
    if avg_type is "numpy":
        return np.average(list_to_average)
    added_value = 0

    if len(list_to_average) < 1:

        return 0

    if not average_range:

        average_range = len(list_to_average)

    elif average_range > len(list_to_average):

        average_range = len(list_to_average)

    for x in range((len(list_to_average)-average_range)-1, len(list_to_average)-1):

        added_value += list_to_average[x]

    avg = added_value/average_range

    return avg


def managelistlenght(list, sizelimit):
    while len(list) > sizelimit:
        del list[0]


def quaternion_to_euler_angle(w, x, y, z):
    ysqr = y * y

    t0 = +2.0 * (w * x + y * z)
    t1 = +1.0 - 2.0 * (x * x + ysqr)
    x = math.degrees(math.atan2(t0, t1))

    t2 = +2.0 * (w * y - z * x)
    t2 = +1.0 if t2 > +1.0 else t2
    t2 = -1.0 if t2 < -1.0 else t2

    y = math.degrees(math.asin(t2))

    t3 = +2.0 * (w * z + x * y)
    t4 = +1.0 - 2.0 * (ysqr + z * z)
    z = math.degrees(math.atan2(t3, t4))

    return x, y, z


def my_zip(history):
    histories = []
    list_of_histories = []
    reformed_list = []
    if type(history) is list:
        if len(history):
            if type(history[0]) is list or tuple:
                sub_item = 0

                while sub_item < len(history[0]):
                    item = 0
                    while item < len(history):
                        if sub_item != 2:
                            histories.append(history[item][sub_item])
                        item += 1

                    list_of_histories.append(histories)
                    histories = []
                    sub_item += 1
            reformed_list = [np.subtract(list_of_histories[0], list_of_histories[2]),
                             np.subtract(list_of_histories[1], list_of_histories[2]),
                             np.subtract(list_of_histories[3], list_of_histories[2]),
                             np.subtract(list_of_histories[4], list_of_histories[2])
                             ]
    return reformed_list


def get_fft(history):

    y = history
    N = len(y)
    yf = fft(y)[5:]

    # trim = 20
    # T = 1.0 /900
    # xf = np.linspace(0, 1.0/(2.0*T), N//2)
    #
    # plt.plot(xf[:trim], (2.0/N * np.abs(yf[0:N//2]))[:trim])
    # plt.grid()
    #
    # plt.show()
    return (2.0/N * np.abs(yf[0:N//2]))

class NGIMULNK():
    def __init__(self):
        self.sensors = [average(50, 100, "/analogue"),
                        average(10, 100, "/quaternion"),
                        average(1, 100, "/battery"),
                        average(50, 100, "/linear"),
                        average(50, 100, "/altitude"),
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
