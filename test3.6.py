from osc4py3.as_eventloop import *
from osc4py3 import oscmethod as osm

def handlerfunction(s, x, y):
    # Will receive message data unpacked in s, x, y
    print(1)
    print(s, x, y)
    pass

def handlerfunction2(address, s, x, y):
    print(1)
    print(address, s, x, y)

osc_startup()
osc_udp_server('192.168.1.9', 8087, "Input from Microcontrollers")
osc_method("/A1", handlerfunction2, argscheme=osm.OSCARG_ADDRESS + osm.OSCARG_DATAUNPACK)

finished = False
while not finished:
    osc_process()
osc_terminate()
