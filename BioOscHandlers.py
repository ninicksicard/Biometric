from BioMathTools import *
from osc4py3 import oscbuildparse
from osc4py3.as_eventloop import *


Needed = []

DataStacker = None


class ValueHolder:
    def __init__(self):
        self.value = None
    def setvalue(self, value):
        self.value = value
    def getvalue(self):
        return self.value

def sensorsHandler(s, x, y):
    DataStacker.DataStack.update({"sensorsHandler": (s, x, y)})

def quaternionHandler(s, x, y, x1):
    DataStacker.DataStack.update({"quaternionHandler": (s, x, y, x1)})

def batteryHandler(s, x, y):
    DataStacker.DataStack.update({"batteryHandler": (s, x, y)})

def linearHandler(s, x, y):
    DataStacker.DataStack.update({"linearHandler": (s, x, y)})
    # A1 = s
    # A1_Bin = SwitchThreshold(A1)
    # A1_msg = oscbuildparse.OSCMessage("/altitude", None, [A1_Bin])
    # osc_send(A1_msg, "to maxmsp")

def altitudehandler(s):
    DataStacker.DataStack.update({"altitudehandler": (s)})


def eegdatahandler(A1=None, A2=None, A3=None, A4=None, A5=None, A6=None, A7=None, A8=None):
    DataStacker.DataStack.update({"eegdatahandler": (A1, A2, A3, A4, A5, A6, A7, A8)})
    # eeg1graph.next_frame(A1)
    # pass


def analoguehandler(A1, A2, A3, A4, A5, A6, A7, A8):
    DataStacker.DataStack.update({"analoguehandler": (A1, A2, A3, A4, A5, A6, A7, A8)})
    # global Needed
    # if "A1" in Needed:
    #     global last_A1_bin
    #     global recthis
    #     A1_Bin = SwitchThreshold(A1)
    #     if A1_Bin == 1:
    #         if last_A1_bin == 0:
    #             try:recthis.StopStream()
    #             except:pass
    #             recthis = AudioTools.RecordStream()
    #             recthis.SetStream()
    #         elif last_A1_bin == 1:
    #             recthis.RecordAFrame()
    #
    #     elif A1_Bin == 0:
    #         if last_A1_bin == 1:
    #             try:recthis.StopStream()
    #             except:pass
    #             recthis.SetTrackToLastRecord()
    #
    #         elif last_A1_bin == 0:
    #             recthis.PlayNextChunkOfTrack()
    #
    #     last_A1_bin = A1_Bin
    #
    #     A1_msg = oscbuildparse.OSCMessage("/A1", None, [A1_Bin])
    #     osc_send(A1_msg, "to maxmsp")
    #
    # if "A2" in Needed:
    #     A2_Bin = SwitchThreshold(A2)
    #     A2_msg = oscbuildparse.OSCMessage("/A2", None, [A2_Bin])
    #     osc_send(A2_msg, "to maxmsp")
    #
    # if "A3" in Needed:
    #     A3_Bin = SwitchThreshold(A3)
    #     A3_msg = oscbuildparse.OSCMessage("/A3", None, [A3_Bin])
    #     osc_send(A3_msg, "to maxmsp")
    #
    # if "A4" in Needed:
    #     A4_Bin = SwitchThreshold(A4)
    #     A4_msg = oscbuildparse.OSCMessage("/A4", None, [A4_Bin])
    #     osc_send(A4_msg, "to maxmsp")
    #
    # if "A5" in Needed:
    #     A5_Bin = SwitchThreshold(A5)
    #     A5_msg = oscbuildparse.OSCMessage("/A5", None, [A5_Bin])
    #     osc_send(A5_msg, "to maxmsp")
    #
    # if "A6" in Needed:
    #     A6_Bin = SwitchThreshold(A6)
    #     A6_msg = oscbuildparse.OSCMessage("/A6", None, [A6_Bin])
    #     osc_send(A6_msg, "to maxmsp")
    #
    # if "A7" in Needed:
    #     A7_Bin = SwitchThreshold(A7)
    #     A7_msg = oscbuildparse.OSCMessage("/A7", None, [A7_Bin])
    #     osc_send(A7_msg, "to maxmsp")
    #
    # if "A8" in Needed:
    #     A8_Bin = SwitchThreshold(A8)
    #     A8_msg = oscbuildparse.OSCMessage("/A8", None, [A8_Bin])
    #     osc_send(A8_msg, "to maxmsp")
