from osc4py3.as_eventloop import *
from osc4py3 import oscbuildparse
import time
# from BioIntOptions import debug
ip_to_reach = "192.168.255.255"
port_to_reach = "50005"

osc_udp_client(ip_to_reach, port_to_reach, "output_server")

to_send = []


def add_message(path="/exemple/path", format_type=",fff", message="['example', 'of', 'values']"):
    # print(path, format_type, message)
    to_send.append(oscbuildparse.OSCMessage(path, format_type, message))


def send_all():

    timed = time.clock()

    global to_send

    if len(to_send):

        for thing in to_send:

            # debug("sending osc", (time.clock() - timed)*1000, "\n")

            osc_send(thing, "output_server")

    to_send = []
