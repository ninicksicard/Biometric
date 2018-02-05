from BioOscHandlers import *
from BioOscManager import OscSignalManager


Needed = [
    "A1",
    "A2",
    "A3",
    "A4",
    "A5",
    "A6",
    "A7",
    "A8",
    ("/muse/eeg", (eegdatahandler, sensorsHandler)),
    ("/sensors", sensorsHandler),
    ("/linear", linearHandler),
    ("/quaternion", quaternionHandler),
    ("/battery", batteryHandler),
    # ("/altitude", altitude.next_frame),
    ("/analogue", analoguehandler),
    ("/muse/elements/delta_absolute", eegdatahandler),
    ("/muse/elements/alpha_absolute", eegdatahandler),
    ("/muse/elements/betha_absolute", eegdatahandler),
    ("/muse/elements/theta_absolute", eegdatahandler),
    ("/muse/elements/gama_absolute", eegdatahandler),
    ("/muse/elements/acc", eegdatahandler),
    ("/muse/elements/gyro", eegdatahandler),
    ("/muse/elements/touching_forehead", eegdatahandler),
    ("/muse/elements/horseshoe", eegdatahandler),
]

last_A1_bin = ""



servers = OscSignalManager((5000,8098), Needed)
