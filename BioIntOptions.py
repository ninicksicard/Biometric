from BioDataOut import *
import BioMathTools
import time
import BioOscHandlers
from BioDataMain import store_data

def debug(name, *args):
    show_or_not = False
    if show_or_not is True:
        print(name, " " * (30-len(name)), *args)

# global variables

data = None
fft_of_history = []


head_position_history = None
head_position_average = None
head_position_quaternion = []

eeg_activity_history = None
eeg_activity_average = None
eeg_activity_simplified = None

data_received = False

sticky_dmx = 0


#scene 02 settings

purple_light_high = 1000
purple_light_low = 200
how_sticky = 100


def fade_in_light():

    timed = time.clock()

    global head_position_average

    pos1 = head_position_average

    pos1_expected_low = 0.7

    pos1_expected_high = 0.9

    if pos1 < 0:
        pos1 = - pos1

    pos1_full_range = pos1_expected_high - pos1_expected_low

    relative_pos1 = ((pos1 - pos1_expected_low)/pos1_full_range) * 255

    dmx_value = BioMathTools.dmx_inverted_exponential_max(relative_pos1)

    add_message("/lx/sub/01", ",f", dmx_value)

    print("purple =", dmx_value, "position = ", pos1)

    debug("purple Light", (time.clock() - timed)*1000)


def purple_light():
    if BioOscHandlers.data_received is False:
        return
    timed = time.clock()

    global eeg_activity_average
    global sticky_dmx
    if eeg_activity_average is None:
        return
    pos1 = eeg_activity_simplified

    pos1_expected_low = purple_light_low

    pos1_expected_high = purple_light_high

    if pos1 < 0:
        pos1 = - pos1

    if pos1 < pos1_expected_low:
        pos1 = pos1_expected_low

    if pos1 > pos1_expected_high:
        pos1 = pos1_expected_high

    pos1_full_range = pos1_expected_high - pos1_expected_low

    relative_pos1 = ((pos1 - pos1_expected_low)/pos1_full_range) * 255

    dmx_value = BioMathTools.dmx_inverted_exponential_max(relative_pos1)

    sticky_dmx = int(((sticky_dmx*(how_sticky-1))+dmx_value)/how_sticky)
    if sticky_dmx <= 0:
        sticky_dmx = 1

    add_message("/lx/sub/01", ",f", sticky_dmx)
    if BioOscHandlers.data_received:
        print("purple =", sticky_dmx, " "*(40-len( str(sticky_dmx))),"position = ", pos1, " "*sticky_dmx, "YOO")

    debug("purple Light", (time.clock() - timed)*1000)


def store_data_pass():

    timed = time.clock()

    global data_received

    store_data()

    # debug("osc_process", (time.clock() - timed)*1000)

    return


def save_history():
    if BioOscHandlers.data_received is False:
        return
    timed = time.clock()

    BioOscHandlers.data_holder.save_history()

    debug("save history", (time.clock() - timed)*1000)

    return


def get_datas():

    timed = time.clock()

    global data

    data = BioOscHandlers.data_holder

    debug("get data", (time.clock() - timed)*1000)

    return data


def head_position_normalized():

    timed = time.clock()

    global data
    global head_position_history
    global head_position_average

    head_position_history = data.get_an_history("matrix7", size=10)

    head_position_average = BioMathTools.average(head_position_history, "numpy")

    debug("average head", (time.clock() - timed)*1000)

    return head_position_average


def eeg_activity_1():
    if BioOscHandlers.data_received is False:
        return
    timed = time.clock()

    global data
    global eeg_activity_history

    eeg_activity_history = data.get_an_history("eeg_raw_data", size=50)    # list of ((a1,a2,a3,a4,a5) , (a1,a2,a3,a4,a5))

    debug("eeg_activity_1", (time.clock() - timed)*1000)


def eeg_activity_2():
    if BioOscHandlers.data_received is False:
        return
    timed = time.clock()

    global eeg_activity_history
    global fft_of_history

    fft_of_history = []

    ordered_history = BioMathTools.my_zip(eeg_activity_history)

    for hists in ordered_history:
        fft_of_history.append(BioMathTools.get_fft(hists))

    debug("eeg_activity_2", (time.clock() - timed)*1000)


def eeg_activity_3():

    if BioOscHandlers.data_received is False:
        return
    timed = time.clock()

    global eeg_activity_average
    global fft_of_history

    for ffts in fft_of_history:

        eeg_activity_average = BioMathTools.average(ffts, "numpy")*1000


    debug("eeg_activity_3", (time.clock() - timed)*1000, str(eeg_activity_average)[1:8])

    global eeg_activity_simplified

    if eeg_activity_average is not None:

        eeg_activity_simplified = int(float(str(eeg_activity_average)[1:5].replace("-", "").replace("+", "")))

        return int(float(str(eeg_activity_average)[1:5 ].replace("-", "").replace("+", "")))


def wait_loop():

    global data_received

    if data_received is False:
        data_received = None

    if data_received is True:

        data_received = False
        return

    return







