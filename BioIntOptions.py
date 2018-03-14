import BioDataOut
import BioMathTools
import time
import BioOscHandlers

settings = None


def debug(name, *args):
    show_or_not = settings.debug
    if show_or_not is True:
        print(name, " " * (30-len(name)), *args)


def fade_in_light():

    if settings.data_received is False:
        return

    if settings.head_position_average is None:
        return

    timed = time.clock()

    pos1 = settings.head_position_average

    pos1_expected_low = 0.7

    pos1_expected_high = 0.9

    if pos1 < 0:
        pos1 = - pos1

    if pos1 < pos1_expected_low:

        pos1 = pos1_expected_low

    if pos1 > pos1_expected_high:

        pos1 = pos1_expected_high

    pos1_full_range = pos1_expected_high - pos1_expected_low

    relative_pos1 = ((pos1 - pos1_expected_low)/pos1_full_range) * 255

    dmx_value = BioMathTools.dmx_inverted_exponential_max(relative_pos1)

    if settings.how_sticky == 0:
        BioDataOut.add_message("/lx/sub/01", ",f", int(dmx_value))
        return

    settings.sticky_dmx = int(((settings.sticky_dmx*(settings.how_sticky-1))+dmx_value)/settings.how_sticky)

    if settings.sticky_dmx <= 0:
        settings.sticky_dmx = 1


    BioDataOut.add_message("/lx/sub/01", ",f", settings.sticky_dmx)

    debug("fade_in_Light", (time.clock() - timed)*1000)


def purple_light():

    if settings.data_received is False:
        return

    if settings.eeg_activity_simplified is None:
        return

    timed = time.clock()

    pos1 = settings.eeg_activity_simplified

    pos1_expected_low = settings.purple_light_low

    pos1_expected_high = settings.purple_light_high

    if pos1 < 0:
        pos1 = - pos1

    if pos1 < pos1_expected_low:
        pos1 = pos1_expected_low

    if pos1 > pos1_expected_high:
        pos1 = pos1_expected_high

    pos1_full_range = pos1_expected_high - pos1_expected_low

    relative_pos1 = ((pos1 - pos1_expected_low)/pos1_full_range) * 255

    dmx_value = BioMathTools.dmx_inverted_exponential_max(relative_pos1)

    settings.sticky_dmx = int(((settings.sticky_dmx*(settings.how_sticky-1))+dmx_value)/settings.how_sticky)

    if settings.sticky_dmx <= 0:
        settings.sticky_dmx = 1

    BioDataOut.add_message("/lx/sub/02", ",f", settings.sticky_dmx)

    debug("purple Light", (time.clock() - timed)*1000)

    return


def save_history():

    if settings.data_received is False:
        return

    timed = time.clock()

    settings.data_holder.save_history()

    debug("save history", (time.clock() - timed)*1000)

    return


def head_position_normalized():

    if settings.data_received is False:
        return

    timed = time.clock()

    settings.head_position_history = settings.data_holder.get_an_history("matrix7", size=5)
    settings.head_position_average = BioMathTools.average(settings.head_position_history, "numpy")

    debug("average head", (time.clock() - timed)*1000, "         ", settings.head_position_average)

    return


def eeg_activity_1():

    if settings.data_received is False:
        return

    timed = time.clock()

    try:
        settings.eeg_activity_history = settings.data_holder.get_an_history("eeg_raw_data", size=25)    # list of ((a1,a2,a3,a4,a5) , (a1,a2,a3,a4,a5))
    except Exception as e:
        print("BioIntOptions.eeg_activity_1, line140", e)
    debug("eeg_activity_1", (time.clock() - timed)*1000)

    return


def eeg_activity_2():

    if settings.data_received is False:
        return

    timed = time.clock()

    settings.fft_of_history = []

    ordered_history = BioMathTools.my_zip(settings.eeg_activity_history)

    for hists in ordered_history:
        settings.fft_of_history.append(BioMathTools.get_fft(hists))

    debug("eeg_activity_2", (time.clock() - timed)*1000)

    return


def eeg_activity_3():

    if settings.data_received is False:
        return

    timed = time.clock()

    for fft_item in settings.fft_of_history:

        settings.eeg_activity_average = BioMathTools.average(fft_item, "numpy")*1000

    if settings.eeg_activity_simplified is not None:

        settings.eeg_activity_simplified = int(float(str(settings.eeg_activity_average)[1:5].replace("-", "").replace("+", "")))

        return int(float(str(settings.eeg_activity_average)[1:5].replace("-", "").replace("+", "")))

    debug("eeg_activity_3", (time.clock() - timed)*1000, str(settings.eeg_activity_average)[1:8])

    return


def wait_loop():

    if settings.data_received is False:
        settings.data_received = None

    if settings.data_received is True:

        settings.data_received = False
        return

    return
