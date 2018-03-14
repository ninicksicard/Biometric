import pyaudio
import matplotlib.pyplot as plt
import BioMathTools
import numpy as np
import time
from scipy.fftpack import fft

settings = None


class Graphic(object):

    def __init__(self):

        self.graphs = ()
        self.frame_count = None
        self.start_time = None
        self.line_fft = None
        self.line = None
        self.fig = None
        self.ax2 = None

        # stream constants
        self.CHUNK = 2048
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 41000
        self.data_list = []

        # x variables for plotting
        x = np.arange(0, self.CHUNK)
        xf = np.linspace(0, self.RATE, self.CHUNK)

        # create matplotlib figure and axes
        self.fig, (ax1, self.ax2) = plt.subplots(2, figsize=(15, 7))

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

        plt.show(block=False)

        self.frame_count = 0

        self.start_time = time.time()

        self.last_frame_time = time.clock()

    def next_frame(self, data_int=None, data_tuple=None, force_show=False, average=False, frame_rate=25, type_of_data="inv_prop"):

        if data_tuple is not None:
            self.data_list = list(data_tuple)

        if data_int is not None:

            if data_int == 1.0 or data_int < 2:
                return

            if type_of_data == "mv":

                data_int = data_int/800*255

            if type_of_data == "inv_prop":

                data_int = 1/(data_int*data_int)

            self.data_list.append(data_int)

        if time.clock() >= self.last_frame_time+(1/frame_rate):

            force_show = True

        if average:

            print(self.data_list[0])

            self.data_list[0] = BioMathTools.average(8, self.data_list)

            print(self.data_list[0], "After")

        if len(self.data_list) >= self.CHUNK:

            data_np = np.array(self.data_list[-self.CHUNK:], dtype='b') + 128

            if len(self.data_list)-len(self.data_list[-self.CHUNK:]) != 0:

                print("missed first", len(self.data_list)-len(self.data_list[-self.CHUNK:]), "values. data_tuple dont match Chunk Size")

            yf = fft(self.data_list)

            self.data_list.pop(0)

            if force_show:

                self.line.set_ydata(data_np)

                self.line_fft.set_ydata(np.abs(yf[0:self.CHUNK]) / (8 * self.CHUNK))

                # update figure canvas

                self.fig.canvas.draw()

                self.fig.canvas.flush_events()

                self.last_frame_time = time.clock()


# Todo: multiple grraphics(stack fft into spectrometer, fftNormalized, fftDirrenense from normal(multiply the diff by itself^2), form lines from what is seen(high pass filter), )


# for spectrometer, get instant value, set it as a row, switch each from values to rgb, or hsl(might be better to then give the value as HUE and the rest to 100%, thend append to the image or pixelmap and remove the first one.
