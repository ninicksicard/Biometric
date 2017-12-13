# Import needed modules from osc4py3
from osc4py3.as_eventloop import *
from osc4py3 import oscbuildparse
from random import randrange
import time


osc_startup()

osc_udp_client('192.168.1.16', 8097, "aclientname")
msg = oscbuildparse.OSCMessage("/altitude", None, ["text", 672, 8.871])
osc_send(msg, "aclientname")

while True:
    value = (randrange(0, 100)*0.01)
    for i in range(500, 0, -1):
        msg = oscbuildparse.OSCMessage("/analogue", None,  ([value*0.8, 0, 0, 0, 0, 0, 0, 0]))
        osc_send(msg, "aclientname")
        print(msg)
        osc_process()
        time.sleep(0.005)