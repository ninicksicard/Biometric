from BioDataMain import *
import BioMathTools
from BioIntOptions import *
import time
allowed = True


class SceneManager:

    def __init__(self):

        BioOscHandlers.scene_manager = self

        self.scenes = [self.Scene01(),
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
                          purple_light,
                          send_all,
                          ]

        def run_scene(self):

            # def purple_light(data_source):
            #
            # def store_data():
            #
            # def save_history():
            #
            # def get_datas():
            #
            # def head_position_normalized():
            #
            # def send_all():
            #
            # def wait_loop():
            #
            # def end():
            while self.laps < 5:
                self.steps[self.laps]()

                self.laps += 1
            self.laps = 0

            # if self.laps == 0:
            #     self.data_received = store_data()
            #     self.laps += 1
            #
            #     debug("osc_process", (time.clock() - timed)*1000)
            #
            #     return
            #
            # elif self.laps == 1:
            #     if self.data_received is False:
            #         BioOscHandlers.data_holder.save_history()
            #         debug("save history", (time.clock() - timed)*1000)
            #     self.laps += 1
            #     return
            #
            # elif self.laps == 2:
            #     if self.data_received is False:
            #         self.data = BioOscHandlers.data_holder
            #         debug("get data", (time.clock() - timed)*1000)
            #     self.laps += 1
            #     return
            #
            # elif self.laps == 3:
            #     if self.data_received is False:
            #         self.head_position_history = self.data.get_an_history("quaternion01", size=10)
            #
            #         self.head_position_average = BioMathTools.average(self.head_position_history)
            #         debug("average ", (time.clock() - timed)*1000)
            #     self.laps += 1
            #     return
            #
            # elif self.laps == 4:
            #     if self.data_received is False:
            #         purple_light(self.head_position_average)
            #         debug("purple Light", (time.clock() - timed)*1000)
            #     self.laps += 1
            #     return
            #
            # elif self.laps == 5:
            #     if len(to_send):
            #
            #         send_all()
            #     self.laps += 1
            #     debug("sending osc", (time.clock() - timed)*1000, "\n")
            #     return
            #
            # elif self.laps < self.waiting_laps:
            #     if self.data_received is False:
            #         self.data_received = None
            #
            #     if self.data_received is True:
            #         self.laps = 0
            #         self.data_received = False
            #         return
            #     self.laps += 1
            #
            #     return
            #
            # else:
            #     self.laps = 0
            #     return




    class Scene02:

        def run_scene(self):

            BioMathTools.average(1, BioOscHandlers.data_holder.get_an_history('sensors_handler', 1))

    class Scene03:

        def run_scene(self):

            BioMathTools.average(1, BioOscHandlers.data_holder.get_an_history('sensors_handler', 1))

    class Scene04:

        def run_scene(self):

            BioMathTools.average(1, BioOscHandlers.data_holder.get_an_history('sensors_handler', 1))


scene_manager = SceneManager()

while allowed:

    scene_manager.live_scene.run_scene()

