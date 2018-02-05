
from osc4py3.as_eventloop import *
import Graphdata

DataStacker = None

eeg1graph = Graphdata.Graphic()

def sensorsHandler(s, x, y):
    DataStacker.DataStack.update({"sensorsHandler": (s, x, y)})

def quaternionHandler(s, x, y, x1):
    DataStacker.DataStack.update({"quaternionHandler": (s, x, y, x1)})

def batteryHandler(s, x, y):
    DataStacker.DataStack.update({"batteryHandler": (s, x, y)})

def linearHandler(s, x, y):

    DataStacker.DataStack.update({"linearHandler": (s, x, y)})

def altitudehandler(s):
    DataStacker.DataStack.update({"altitudehandler": (s)})


def eegdatahandler(A1=None, A2=None, A3=None, A4=None, A5=None, A6=None, A7=None, A8=None):
    DataStacker.DataStack.update({"eegdatahandler": (A1, A2, A3, A4, A5, A6, A7, A8)})

def analoguehandler(A1, A2, A3, A4, A5, A6, A7, A8):
    print("received")
    DataStacker.DataStack.update({"analoguehandler": (A1, A2, A3, A4, A5, A6, A7, A8)})


class OscSignalManager:
    def __init__(self, ports, needed):

        global DataStacker
        DataStacker = self
        self.DataStack = {}

        self.Needed = needed
        osc_startup()

        self.firstserver = 0
        self.localip = '192.168.1.15'
        self.addresses = []

        for p in ports:
            self.addresses.append((self.localip, p))

        self.startservers()
        self.sethandlers()
        self.loop_osc_process()

    def loop_osc_process(self):
        finished = False
        while not finished:
            print(self.DataStack)
            osc_process()

    def startservers(self):
        thisserver = str(self.firstserver)
        for adress, port in self.addresses:
            osc_udp_server(adress, port, str("Server"+thisserver))
            thisserver = str(int(thisserver)+1)

    def sethandlers(self):
        for path, handler in self.Needed:
            if path[:1] == "/":
                print(type(handler))
                if type(handler) is tuple:
                    for h in handler:
                        print(path, (40-len(path))*' ', str(h)[9:-22])
                        osc_method(path, h)
                elif str(type(handler)) == "<class 'function'>":
                    osc_method(path, handler)
                    print(path, (40-len(path))*' ', str(handler)[9:-22])
                else:
                    print("verify handler's name and format. should be function 'handler' or tuple '(handler1, handler2)'")

