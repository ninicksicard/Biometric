from BioDataMain import *
import BioMathTools
from BioIntOptions import *
import time

allowed = True


class SceneManager:

    def __init__(self):

        BioOscHandlers.scene_manager = self

        self.scenes = [#self.Scene01(),
                       self.Scene02(),
                       self.Scene03(),
                       self.Scene04()
                       ]

        self.live_scene = self.scenes[0]

    def change_live_scene(self, scene_number):

        self.live_scene = self.scenes[scene_number]

    class Scene01:

        def __init__(self):
            self.laps = 0
            self.data = None
            self.waiting_laps = 50000
            self.head_position_history = None
            self.head_position_average = None
            self.data_received = None
            self.steps = [store_data_pass,
                          save_history,
                          get_datas,
                          head_position_normalized,
                          fade_in_light,
                          send_all,
                          ]

        def run_scene(self):

            while self.laps < len(self.steps):
                self.steps[self.laps]()

                self.laps += 1
            self.laps = 0

    class Scene02:

        def __init__(self):
            self.laps = 0
            self.data = None
            self.waiting_laps = 50000
            self.head_position_history = None
            self.head_position_average = None
            self.data_received = None
            get_datas()
            self.steps = [store_data_pass,
                          save_history,

                          eeg_activity_1,
                          eeg_activity_2,
                          eeg_activity_3,
                          purple_light,
                          send_all,
                          ]

        def run_scene(self):

            while self.laps < len(self.steps):
                self.steps[self.laps]()

                self.laps += 1
            self.laps = 0

    class Scene03:

        def run_scene(self):

            while self.laps < len(self.steps):
                self.steps[self.laps]()

                self.laps += 1
            self.laps = 0

    class Scene04:

        def run_scene(self):

            while self.laps < len(self.steps):
                self.steps[self.laps]()

                self.laps += 1
            self.laps = 0


scene_manager = SceneManager()

while allowed:

    scene_manager.live_scene.run_scene()

