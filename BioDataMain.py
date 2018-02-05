# one part that will build the main. this start the osc server and generate the datastacker object

from BioDataCapture import *


Needed = [
    ("/muse/eeg", eegdatahandler),          # valeurs des electrodes en mv pas certain de l<ordre (pourrais [etre utilis/ sur un spectateur, mais pas sur la comédienne.)
    ("/linear", linearHandler),             # Acceleration of the module in different direction (xYz) from -5 to 5. seem precize, could be used to create movements of spotlights
    ("/quaternion", quaternionHandler),     # values of the gyroscope, 4 values because of the transition including several gyroscopes avoiding gimbal lock*?
    ("/analogue", analoguehandler),         # valeur analogue sur 3 ou 5 volts. très utilisable, boutons,

    # ("/battery", batteryHandler),
    # ("/sensors", sensorsHandler),
    # ("/altitude", altitude.next_frame),
    # ("/muse/elements/delta_absolute", eegdatahandler),
    # ("/muse/elements/alpha_absolute", eegdatahandler),
    # ("/muse/elements/betha_absolute", eegdatahandler),
    # ("/muse/elements/theta_absolute", eegdatahandler),
    # ("/muse/elements/gama_absolute", eegdatahandler),
    # ("/muse/elements/acc", eegdatahandler),
    # ("/muse/elements/gyro", eegdatahandler),
    # ("/muse/elements/touching_forehead", eegdatahandler),
    # ("/muse/elements/horseshoe", eegdatahandler),
]


last_A1_bin = ""



servers = OscSignalManager((5000,8098), Needed)
