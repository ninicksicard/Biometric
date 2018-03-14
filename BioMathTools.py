
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft

settings = None


def switch_threshold(value, threshold=0.5):
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

    if settings.data_received is False:
        return

    if len(list_to_average) < 1:

        return 0

    if avg_type is "numpy":

        return np.average(list_to_average)

    added_value = 0

    if not average_range:

        average_range = len(list_to_average)

    elif average_range > len(list_to_average):

        average_range = len(list_to_average)

    for x in range((len(list_to_average)-average_range)-1, len(list_to_average)-1):

        added_value += list_to_average[x]

    avg = added_value/average_range

    return avg


def manage_list_length(some_list, size_limit):

    while len(some_list) > size_limit:
        del some_list[0]


def quaternion_to_euler_angle(w, x, y, z):

    y_square = y * y

    t0 = +2.0 * (w * x + y * z)
    t1 = +1.0 - 2.0 * (x * x + y_square)
    x = math.degrees(math.atan2(t0, t1))

    t2 = +2.0 * (w * y - z * x)
    t2 = +1.0 if t2 > +1.0 else t2
    t2 = -1.0 if t2 < -1.0 else t2

    y = math.degrees(math.asin(t2))

    t3 = +2.0 * (w * z + x * y)
    t4 = +1.0 - 2.0 * (y_square + z * z)
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
                return [reformed_list[1]]
    return reformed_list


def get_fft(history):

    y = history

    n = len(y)

    yf = fft(y)

    # trim = 20
    #
    # t = 1.0 / 900
    #
    # xf = np.linspace(0, 1.0/(2.0*t), n//2)
    #
    # plt.plot(xf[:trim], (2.0/n * np.abs(yf[0:n//2]))[:trim])
    #
    # plt.grid()
    #
    # plt.show(block=False)

    return 2.0/n * np.abs(yf[0:n//2])


# Todo : Functions : ( remove eye movement; remove the row or low cut the pike, Find jighest frequency, create profiles based on frequencys)


""" get meditation datas and set as base
    

"""
