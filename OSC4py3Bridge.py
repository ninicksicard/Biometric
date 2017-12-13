from osc4py3.as_eventloop import *
from osc4py3 import oscbuildparse
import matplotlib.pyplot as plt
import numpy as np
import pyaudio
from scipy.fftpack import fft
import time
import threading
import AudioTools

Needed = ["A1"]

last_A1_bin = ""
recthis = "future recording name"


class Graphic(object):
    def __init__(self):

        # stream constants
        self.CHUNK = 100
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 41000
        self.pause = False
        self.data_list = []
        # stream object


        self.init_plots()
        self.start_plot()

    def init_plots(self):

        # x variables for plotting
        x = np.arange(0, self.CHUNK)
        xf = np.linspace(0, self.RATE, self.CHUNK)
        print(xf)
        # create matplotlib figure and axes
        self.fig, (ax1, self.ax2) = plt.subplots(2, figsize=(15, 7))
        self.fig.canvas.mpl_connect('button_press_event', self.onClick)

        # create a line object with random data
        self.line, = ax1.plot(x, np.random.rand(self.CHUNK), '-', lw=2)

        # create semilogx line for spectrum
        self.line_fft, = self.ax2.semilogx(xf, np.random.rand(self.CHUNK), '-', lw=2)

        # format waveform axes
        ax1.set_title('AUDIO WAVEFORM')
        ax1.set_xlabel('samples')
        ax1.set_ylabel('volume')
        ax1.set_ylim(0, 255)
        ax1.set_xlim(0, self.CHUNK)
        plt.setp(ax1, yticks=[0, 128, 255], xticks=[0, self.CHUNK, self.CHUNK],)
        plt.setp(self.ax2, yticks=[0, 1],)

        # format spectrum axes
        self.ax2.set_xlim(1000, self.RATE)

        # show axes
        thismanager = plt.get_current_fig_manager()
        # thismanager.window.setGeometry(5, 120, 720, 260)
        plt.show(block=False)

    def start_plot(self):

        print('stream started')
        self.frame_count = 0
        self.start_time = time.time()

    def next_frame(self, data_int):
        self.data_list.append(data_int)
        print(len(self.data_list))
        # compute FFT and update line
        while len(self.data_list) > self.CHUNK:
            self.data_list.pop(0)
        if len(self.data_list) == self.CHUNK:
            data_np = np.array(self.data_list, dtype='b') + 128
            yf = fft(self.data_list)

            self.line.set_ydata(data_np)
            self.line_fft.set_ydata(np.abs(yf[0:self.CHUNK]) / (7 * self.CHUNK))
            # update figure canvas
            self.fig.canvas.draw()
            self.fig.canvas.flush_events()

    def exit_app(self):
        print('stream closed')


    def onClick(self, event):
        self.pause = True


def SwitchThreshold(value, threshold=0.5):
    if value <= threshold:
        return 0
    else:
        return 1

def sensorsHandler(s, x, y):
    # print(s, x, y)
    pass

def quaternionHandler(s, x, y, x1):
    pass
    # print("received")
    # print(s, x, y)


def batteryHandler(s, x, y):
    pass
    # print(s, x, y)


def linearHandler(s, x, y):
    A1 = s
    A1_Bin = SwitchThreshold(A1)
    A1_msg = oscbuildparse.OSCMessage("/altitude", None, [A1_Bin])
    osc_send(A1_msg, "to maxmsp")
    print(A1_Bin)


def altitudehandler(s, x, y):
    pass
    # print(s, x, y)


def analoguehandler(A1, A2, A3, A4, A5, A6, A7, A8):
    if "A1" in Needed:
        global last_A1_bin
        global recthis
        A1_Bin = SwitchThreshold(A1)
        if A1_Bin == 1:
            if last_A1_bin == 0:
                try:recthis.StopStream()
                except:pass
                recthis = AudioTools.RecordStream()
                recthis.SetStream()
            elif last_A1_bin == 1:
                recthis.RecordAFrame()

        elif A1_Bin == 0:
            if last_A1_bin == 1:
                try:recthis.StopStream()
                except:pass
                recthis.SetTrackToLastRecord()

            elif last_A1_bin == 0:
                recthis.PlayNextChunkOfTrack()

        last_A1_bin = A1_Bin

        A1_msg = oscbuildparse.OSCMessage("/A1", None, [A1_Bin])
        osc_send(A1_msg, "to maxmsp")

    if "A2" in Needed:
        A2_Bin = SwitchThreshold(A2)
        A2_msg = oscbuildparse.OSCMessage("/A2", None, [A2_Bin])
        osc_send(A2_msg, "to maxmsp")

    if "A3" in Needed:
        A3_Bin = SwitchThreshold(A3)
        A3_msg = oscbuildparse.OSCMessage("/A3", None, [A3_Bin])
        osc_send(A3_msg, "to maxmsp")

    if "A4" in Needed:
        A4_Bin = SwitchThreshold(A4)
        A4_msg = oscbuildparse.OSCMessage("/A4", None, [A4_Bin])
        osc_send(A4_msg, "to maxmsp")

    if "A5" in Needed:
        A5_Bin = SwitchThreshold(A5)
        A5_msg = oscbuildparse.OSCMessage("/A5", None, [A5_Bin])
        osc_send(A5_msg, "to maxmsp")

    if "A6" in Needed:
        A6_Bin = SwitchThreshold(A6)
        A6_msg = oscbuildparse.OSCMessage("/A6", None, [A6_Bin])
        osc_send(A6_msg, "to maxmsp")

    if "A7" in Needed:
        A7_Bin = SwitchThreshold(A7)
        A7_msg = oscbuildparse.OSCMessage("/A7", None, [A7_Bin])
        osc_send(A7_msg, "to maxmsp")

    if "A8" in Needed:
        A8_Bin = SwitchThreshold(A8)
        A8_msg = oscbuildparse.OSCMessage("/A8", None, [A8_Bin])
        osc_send(A8_msg, "to maxmsp")

altitude = Graphic()

osc_startup()
osc_udp_server('192.168.1.16', 8097, "Input from Microcontrollers")
osc_udp_client('192.168.1.16', 9000, "to maxmsp")
osc_method("/sensors", sensorsHandler)
osc_method("/linear", linearHandler)
osc_method("/quaternion", quaternionHandler)
osc_method("/battery", batteryHandler)
osc_method("/altitude", altitude.next_frame)
osc_method("/analogue", analoguehandler)


finished = False
while not finished:
    osc_process()
osc_terminate()





