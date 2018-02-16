from osc4py3.as_eventloop import *


class OscSignalManager:

    def __init__(self, ip, ports, needed):

        osc_startup()

        self.first_server = 0
        self.local_ip = ip
        self.addresses = []

        for p in ports:

            self.addresses.append((self.local_ip, p))

        self.needed = needed

        self.start_servers()
        self.set_handlers()

    def start_servers(self):

        this_server = str(self.first_server)

        for address, port in self.addresses:

            osc_udp_server(address, port, str("Server" + this_server))
            this_server = str(int(this_server)+1)

    def set_handlers(self):

        for path, handler in self.needed:

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

