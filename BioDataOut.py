from osc4py3.as_eventloop import *
from osc4py3 import oscbuildparse
import time

settings = None


def debug(name, *args):
    show_or_not = settings.debug
    if show_or_not is True:
        print(name, " " * (30-len(name)), *args)


def set_client():

    if settings.data_received is False:
        return

    timed = time.clock()

    osc_udp_client(settings.ip_to_reach, settings.port_to_reach, "output_server")

    debug("set_client", (time.clock() - timed)*1000)


def add_message(path="/exemple/path", format_type=",fff", message="['example', 'of', 'values']"):

    if settings.data_received is False:
        return

    timed = time.clock()

    settings.to_send.append(oscbuildparse.OSCMessage(path, format_type, message))

    debug("add_message", (time.clock() - timed)*1000)


def send_all():

    if settings.data_received is False:
        return

    timed = time.clock()

    if len(settings.to_send):

        for thing in settings.to_send:

            osc_send(thing, "output_server")

            print(settings.to_send)

    settings.to_send = []

    debug("send_all", (time.clock() - timed)*1000)
