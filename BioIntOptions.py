from BioDataOut import *
import BioMathTools
import time
import BioOscHandlers
from BioDataMain import store_data

def debug(*args):
    show_or_not = False
    if show_or_not is True:
        print(*args)


# global variables

data = None
head_position_history = None
head_position_average = None
head_position_quaternion = []
data_received = False


def purple_light():

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


def store_data_pass():

    timed = time.clock()

    global data_received

    data_received = store_data()

    debug("osc_process", (time.clock() - timed)*1000)

    return data_received


def save_history():

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

    head_position_average = BioMathTools.average(head_position_history)

    debug("average ", (time.clock() - timed)*1000)

    return head_position_average


def send_all():
    timed = time.clock()

    if len(to_send):

        send_all()

    debug("sending osc", (time.clock() - timed)*1000, "\n")

    return


def wait_loop():

    global data_received

    if data_received is False:
        data_received = None

    if data_received is True:

        data_received = False
        return


    return


def end():
    self.laps = 0
    return






