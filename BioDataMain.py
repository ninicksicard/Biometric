import BioOscManager
import time
settings = None


def debug(name, *args):
    show_or_not = settings.debug
    if show_or_not is True:
        print(name, " " * (30-len(name)), *args)


def set_server():

    timed = time.clock()

    settings.servers = BioOscManager.OscSignalManager(settings.my_ip_address, settings.my_receiving_osc_port, settings.needed_values)

    debug("set_server", (time.clock() - timed)*1000)


def store_data():

    timed = time.clock()

    settings.data_received = False
    BioOscManager.osc_process()
    if settings.data_received is False:
        return

    debug("store_data", (time.clock() - timed)*1000)
