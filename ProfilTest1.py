import time


class Profile:
    def __init__(self):

        # les valeurs absolues pourraient être des True false, dépendament de si elles sont dans le threshold,
        # pourrais aussi être un facteur de modification pour interpréter les signaux
        # peux aussi storer les valeurs actuels en attendant qu'elles soient toute luent..
        # pourraif permettre à laisser certaines valeurs True, quand elles sont activés, pour faciliter le switch
        # ou seulement dropper directement les valeurs des signaux osc ici quand ils sont called.
        #
        # profiles[active_profile].set_eeg_values
        # def set_eeg_values(values):
            # self.eeg_value = values
        # le switch vers le prochain profile reset les valeurs.


        # Valeurs passives
        self.eeg_values = None  # (0,0,0,0,0)  all values, should assign them here
        self.eeg_value_threshold = None  # valeur du threshold utiliser un range entre 2 valeurs pour ne pas utiliser de symboles
        self.skin_humidity = None  # (valeur à déterminer)
        self.skin_humidity_threshold = None  # utliilser un range encore
        self.skin_temperature = None  # also use delta temp with air temp
        self.skin_temperature_threshold = None  # range de valeurr
        self.air_temperature = None  # to use as comparison with skin temp
        self.air_temperature_threshold = None  # range encore
        self.heart_rate = None  # devrias utilisé valeur de constance et de vitesse moyenne séparément.
        self.hearth_rate_threshold = None  # range
        self.muscle_tension = None  # une liste si plusieurs senseurs utilisés
        self.muscle_tension_threshold = None  # un range

        # environement
        self.scene_number = None  # numéro de scène ou ordre dans la séquence
        self.dmx_set = None  # dictionnaire comportant (channel, intensité, Id de lumiere ou nom)
                    # l'intensité de la lumière peux être directement une fonction callé qui donne une intensité sinusoidale basé sur le clock
        self.dmx_fade_in = None
        self.dmx_fade_out = None

        self.audio_records = None  # list ou dictionnaire d'objets étant des clip audio
        self.audio_effects = None  # list des effets audio à utiliser pendant ce profil.

        # self existance
        self.clock_initialized = time.clock()
        self.profile_name = None

        # Conditions
        self.clock_force_start = None  # clock time at wich it absolutely must switch to this profile
        self.clock_expected_start = None  # pour modifié la valeur du treshold pour switcher plus facilement quand c'Est le temps
        self.clock_force_stop = None
        self.profile_last_expected = None  # nom du dernier profil qui doit être actif avant de pouvoir switcher

        self.first_values_to_verify = None  #valeurs a verifier en premier pour accelerer la verification.


        # print this in text
        self.all_profiles_settings = {"eeg_values": (self.eeg_values),
                                      "eeg_values_threshold": self.eeg_value_threshold,
                                      "skin_humidity": self.skin_humidity,
                                      "skin_humidity_threshold": self.skin_humidity_threshold,
                                      "skin_temperature": self.skin_temperature,
                                      "skin_temperature_threshold": self.skin_temperature_threshold,
                                      "air_temperature": self.air_temperature,
                                      "air_temperature_threshold": self.air_temperature_threshold,
                                      "heart_rate": self.heart_rate,
                                      "hearth_rate_threshold": self.hearth_rate_threshold,
                                      "muscle_tension": self.muscle_tension,
                                      "muscle_tension_threshold": self.muscle_tension_threshold,
                                      "scene_number": self.scene_number,
                                      "dmx_set": self.dmx_set,
                                      "dmx_fade_in": self.dmx_fade_in,
                                      "dmx_fade_out": self.dmx_fade_out,
                                      "audio_records": self.audio_records,
                                      "audio_effects": self.audio_effects,
                                      "clock_initialized": self.clock_initialized,
                                      "profile_name": self.profile_name,
                                      "clock_force_start": self.clock_force_start,
                                      "clock_expected_start": self.clock_expected_start,
                                      "clock_force_stop": self.clock_force_stop,
                                      "profile_last_expected": self.profile_last_expected,
                                      "first_values_to_verify": self.first_values_to_verify}
        # Load this from literal eval
