
class Interface:

    def __init__(self):

        import BioSceneManager
        import BioDataCapture
        BioSceneManager.settings = self

        BioSceneManager.BioIntOptions.settings = self
        BioSceneManager.BioIntOptions.BioOscHandlers.settings = self
        BioSceneManager.BioIntOptions.BioDataOut.settings = self
        BioSceneManager.BioIntOptions.BioMathTools.settings = self

        BioSceneManager.BioDataMain.settings = self
        BioSceneManager.BioDataMain.BioOscManager.settings = self

        # self.start_show
        self.allowed = True

        # BioSceneManager
        self.first_scene = 1
        self.scene_manager = BioSceneManager.SceneManager()

        # BioDataMain
        self.my_ip_address = '192.168.1.6'
        self.my_receiving_osc_port = [8019]
        self.late = 0
        self.needed_values = [
            ("/muse/eeg",                           BioSceneManager.BioIntOptions.BioOscHandlers.eeg_raw_data_handler),
            ("/linear",                             BioSceneManager.BioIntOptions.BioOscHandlers.linear_handler),             # Acceleration of the module in different direction (xYz) from -5 to 5. seem precize, could be used to create movements of spotlights
            ("/quaternion",                         BioSceneManager.BioIntOptions.BioOscHandlers.quaternion_handler),
            ("/matrix",                             BioSceneManager.BioIntOptions.BioOscHandlers.rotation_matrix),
            ("/analogue",                           BioSceneManager.BioIntOptions.BioOscHandlers.analogue_handler),         # valeur analogue sur 3 ou 5 volts. très utilisable, bouton,
            ("/battery",                            BioSceneManager.BioIntOptions.BioOscHandlers.battery_handler),
            ("/sensors",                            BioSceneManager.BioIntOptions.BioOscHandlers.sensors_handler),
            ("/altitude",                           BioSceneManager.BioIntOptions.BioOscHandlers.altitude_handler),
            ("/muse/elements/delta_absolute",       BioSceneManager.BioIntOptions.BioOscHandlers.eeg_delta_handler),
            ("/muse/elements/alpha_absolute",       BioSceneManager.BioIntOptions.BioOscHandlers.eeg_alpha_handler),
            ("/muse/elements/beta_absolute",        BioSceneManager.BioIntOptions.BioOscHandlers.eeg_beta_handler),
            ("/muse/elements/theta_absolute",       BioSceneManager.BioIntOptions.BioOscHandlers.eeg_theta_handler),
            ("/muse/elements/gama_absolute",        BioSceneManager.BioIntOptions.BioOscHandlers.eeg_gamma_handler),
            ("/muse/elements/acc",                  BioSceneManager.BioIntOptions.BioOscHandlers.eeg_accelerometer_handler),
            ("/muse/elements/gyro",                 BioSceneManager.BioIntOptions.BioOscHandlers.eeg_gyro_handler),
            ("/muse/elements/touching_forehead",    BioSceneManager.BioIntOptions.BioOscHandlers.eeg_touching_forehead_handler),
            ("/muse/elements/horseshoe",            BioSceneManager.BioIntOptions.BioOscHandlers.eeg_horseshoe_handler),
            ("/maxmsp/sceneselection",              BioSceneManager.BioIntOptions.BioOscHandlers.set_scene)
        ]


        # BioDataOut

        self.ip_to_reach = "192.168.255.255"
        self.port_to_reach = "50005"
        self.output_server_name = "output_server"
        self.to_send = []
        # BioOscHandler

        BioSceneManager.BioIntOptions.BioOscHandlers.scene_manager = None
        BioSceneManager.BioIntOptions.BioOscHandlers.timeout = 100
        BioSceneManager.BioIntOptions.BioOscHandlers.delay = 0
        BioSceneManager.BioIntOptions.BioOscHandlers.data_received = False

        # BioIntOptions
        self.debug = BioSceneManager.BioIntOptions.debug

        self.debug = False
        self.sticky_dmx = 0

        self.data_received = False

        # fade_in_light
        self.head_position_history = None
        self.head_position_average = None
        self.head_position_quaternion = []

        # purple_light
        self.eeg_activity_history = None
        self.eeg_activity_average = None
        self.eeg_activity_simplified = None

        self.fft_of_history = []

        # scene 02 settings

        self.purple_light_high = 7000
        self.purple_light_low = 1
        self.how_sticky = 0

        self.data_holder = BioDataCapture.DataHolder()
        BioSceneManager.BioIntOptions.BioDataOut.set_client()
        BioSceneManager.BioDataMain.set_server()

    def start_show(self):
        while True:
            self.scene_manager.live_scene.run_scene()


yo = Interface()

yo.start_show()
