# one part that will build the main. this start the osc server and generate the datastacker object

from BioOscManager import *
import BioOscHandlers
import time


my_ip_address = '192.168.1.15'
my_receiving_osc_port = [8019]
late = 0

needed_values = [
    ("/muse/eeg", BioOscHandlers.eeg_raw_data_handler),     # valeurs des electrodes en mv pas certain de l<ordre (pourrais [etre utilis/ sur un spectateur, mais pas sur la comédienne.)
    ("/linear", BioOscHandlers.linear_handler),             # Acceleration of the module in different direction (xYz) from -5 to 5. seem precize, could be used to create movements of spotlights
    ("/quaternion", BioOscHandlers.quaternion_handler),     # values of the gyroscope, 4 values because of the transition including several gyroscopes avoiding gimbal lock*?
    ("/matrix", BioOscHandlers.rotation_matrix),
    ("/analogue", BioOscHandlers.analogue_handler),         # valeur analogue sur 3 ou 5 volts. très utilisable, bouton,
    ("/battery", BioOscHandlers.battery_handler),
    ("/sensors", BioOscHandlers.sensors_handler),
    ("/altitude", BioOscHandlers.altitude_handler),
    ("/muse/elements/delta_absolute", BioOscHandlers.eeg_delta_handler),
    ("/muse/elements/alpha_absolute", BioOscHandlers.eeg_alpha_handler),
    ("/muse/elements/beta_absolute", BioOscHandlers.eeg_beta_handler),
    ("/muse/elements/theta_absolute", BioOscHandlers.eeg_theta_handler),
    ("/muse/elements/gama_absolute", BioOscHandlers.eeg_gamma_handler),
    ("/muse/elements/acc", BioOscHandlers.eeg_accelerometer_handler),
    ("/muse/elements/gyro", BioOscHandlers.eeg_gyro_handler),
    ("/muse/elements/touching_forehead", BioOscHandlers.eeg_touching_forehead_handler),
    ("/muse/elements/horseshoe", BioOscHandlers.eeg_horseshoe_handler),
    ("/maxmsp/sceneselection", BioOscHandlers.set_scene)
]

servers = OscSignalManager(my_ip_address, my_receiving_osc_port, needed_values)


def store_data():

    osc_process()

    if BioOscHandlers.data_received is True:
        BioOscHandlers.data_received = False
        return True

    elif BioOscHandlers.data_received is False:
        return False
