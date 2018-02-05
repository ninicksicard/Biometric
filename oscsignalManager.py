from osc4py3.as_eventloop import *
import handlers

class OscSignalManager:
    def __init__(self, ports, Needed):
        osc_startup()
        handlers.Needed = Needed
        handlers.DataStacker = self

        self.DataStack = {}

        self.firstserver = 0
        self.localip = '192.168.1.15'
        self.addresses = []
        for p in ports:  self.addresses.append((self.localip, p))
        self.Needed = Needed
        self.startservers()
        self.sethandlers()
        self.loop_osc_process()

    def loop_osc_process(self):
        finished = False
        while not finished:
            print(self.DataStack)
            osc_process()

    def startservers(self):
        thisserver = str(self.firstserver)
        for adress, port in self.addresses:
            osc_udp_server(adress, port, str("Server"+thisserver))
            thisserver = str(int(thisserver)+1)

    def sethandlers(self):
        for path, handler in self.Needed:
            if path[:1] == "/":
                if type(handler) is tuple:
                    for h in handler:
                        print(path, (40-len(path))*' ', str(h)[9:-22])
                        osc_method(path, h)
                elif str(type(handler)) == "<class 'function'>":
                    osc_method(path, handler)
                    print(path, (40-len(path))*' ', str(handler)[9:-22])
                else:
                    print("verify handler's name and format. should be function 'handler' or tuple '(handler1, handler2)'")
