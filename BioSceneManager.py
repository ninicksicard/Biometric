import BioIntOptions
import BioDataMain
import time


settings = None


class SceneManager:

    def __init__(self):

        BioIntOptions.BioOscHandlers.scene_manager = self

        self.scenes = [self.Scene01(),
                       self.Scene02(),
                       self.Scene03(),
                       self.Scene04()
                       ]

        self.live_scene = self.scenes[settings.first_scene]

    def change_live_scene(self, scene_number):

        self.live_scene = self.scenes[scene_number]

    class Scene01:

        def __init__(self):
            self.timed = time.clock()
            self.laps = 0
            self.steps = [BioDataMain.store_data,
                          BioIntOptions.save_history,
                          BioIntOptions.head_position_normalized,
                          BioIntOptions.fade_in_light,
                          BioIntOptions.BioDataOut.send_all,
                          ]

        def run_scene(self):

            while self.laps < len(self.steps):
                self.steps[self.laps]()

                self.laps += 1
            self.laps = 0

    class Scene02:

        def __init__(self):
            self.laps = 0
            self.steps = [BioDataMain.store_data,
                          BioIntOptions.save_history,
                          BioIntOptions.eeg_activity_1,
                          BioIntOptions.eeg_activity_2,
                          BioIntOptions.eeg_activity_3,
                          BioIntOptions.purple_light,
                          BioIntOptions.BioDataOut.send_all,
                          ]

        def run_scene(self):

            while self.laps < len(self.steps):
                self.steps[self.laps]()

                self.laps += 1
            self.laps = 0

    class Scene03:

        def __init__(self):
            self.laps = 0
            self.steps = [BioDataMain.store_data,
                          BioIntOptions.save_history,
                          BioIntOptions.eeg_activity_1,
                          BioIntOptions.eeg_activity_2,
                          BioIntOptions.eeg_activity_3,
                          BioIntOptions.purple_light,
                          BioIntOptions.BioDataOut.send_all,
                          ]

        def run_scene(self):

            while self.laps < len(self.steps):
                self.steps[self.laps]()

                self.laps += 1
            self.laps = 0

    class Scene04:

        def __init__(self):
            self.laps = 0
            self.steps = [BioDataMain.store_data,
                          BioIntOptions.save_history,
                          BioIntOptions.eeg_activity_1,
                          BioIntOptions.eeg_activity_2,
                          BioIntOptions.eeg_activity_3,
                          BioIntOptions.purple_light,
                          BioIntOptions.BioDataOut.send_all,
                          ]

        def run_scene(self):

            while self.laps < len(self.steps):
                self.steps[self.laps]()

                self.laps += 1
            self.laps = 0
