import OSC
import time
import random
c = OSC.OSCClient()
c.connect(('192.168.1.9', 8087))   # localhost, port 57120


oscmsg = OSC.OSCMessage()
oscmsg.setAddress("/A1")
number = random.randrange(0, 10)
oscmsg.append(number*0.1)
c.send(oscmsg)
oscmsg.clear()
time.sleep(0.001)
print("sent")




