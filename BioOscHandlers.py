import time

settings = None


def debug(name, *args):
    show_or_not = False
    if show_or_not is True:
        print(name, " " * (30-len(name)), *args)


timeout = 100
delay = 0
data_received = False


def set_scene(scene_number):
    settings.scene_manager.live_scene = settings.scene_manager.scenes[scene_number]


def sensors_handler(s, x, y):
    settings.data_received = True
    settings.data_holder.update_data("sensors_handler", (s, x, y))


def quaternion_handler(value01=None, value02=None, value03=None, value04=None):
    settings.data_received = True
    settings.data_holder.update_data("quaternion01", value01)
    settings.data_holder.update_data("quaternion02", value02)
    settings.data_holder.update_data("quaternion03", value03)
    settings.data_holder.update_data("quaternion04", value04)


def rotation_matrix(x=None, y=None, z=None, rot_x=None, rot_y=None, rot_z=None, vx=None, vy=None, vz=None, *args):
    # print("x : ", x, "y : ", y, "z : ", z, "rot_x : ", rot_x, "rot_y : ", rot_y, "rot_z : ", rot_z, "vxx : ", vx, "vy : ", vy, "vz : ", vz, "args : ", *args)
    settings.data_received = True
    timed = time.clock()
    settings.data_holder.update_data("matrix1", x)
    settings.data_holder.update_data("matrix2", y)
    settings.data_holder.update_data("matrix3", z)
    settings.data_holder.update_data("matrix4", rot_x)
    settings.data_holder.update_data("matrix5", rot_y)
    settings.data_holder.update_data("matrix6", rot_z)
    settings.data_holder.update_data("matrix7", vx)
    settings.data_holder.update_data("matrix8", vy)
    settings.data_holder.update_data("matrix9", vz)
    debug("rotation_matrix_handler", (time.clock() - timed)*1000)


def battery_handler(s, x, y):

    settings.data_holder.update_data("batteryHandler", (s, x, y))


def linear_handler(s, x, y):
    settings.data_holder.update_data("linear_handler", (s, x, y))


def altitude_handler(s):
    settings.data_holder.update_data("altitude_handler", s)


def eeg_raw_data_handler(a1=None, a2=None, a3=None, a4=None, a5=None,):

    settings.data_received = True
    if time.clock()-delay > timeout:
        return
    settings.data_holder.update_data("eeg_raw_data", (a1, a2, a3, a4, a5))


def analogue_handler(a1, a2, a3, a4, a5, a6, a7, a8):
    if time.clock()-delay > timeout:
        return
    settings.data_holder.update_data("analogue_01", a1)
    settings.data_holder.update_data("analogue_02", a2)
    settings.data_holder.update_data("analogue_03", a3)
    settings.data_holder.update_data("analogue_04", a4)
    settings.data_holder.update_data("analogue_05", a5)
    settings.data_holder.update_data("analogue_06", a6)
    settings.data_holder.update_data("analogue_07", a7)
    settings.data_holder.update_data("analogue_08", a8)


def eeg_delta_handler(value):
    if time.clock()-delay > timeout:
        return
    settings.data_holder.update_data("eeg_delta", value)


def eeg_alpha_handler(value):
    if time.clock()-delay > timeout:
        return
    settings.data_holder.update_data("eeg_alpha", value)


def eeg_beta_handler(value):
    if time.clock()-delay > timeout:
        return
    settings.data_holder.update_data("eeg_beta", value)


def eeg_theta_handler(value):
    if time.clock()-delay > timeout:
        return
    settings.data_holder.update_data("eeg_theta", value)


def eeg_gamma_handler(value):
    if time.clock()-delay > timeout:
        return
    settings.data_holder.update_data("eeg_gamma", value)


def eeg_accelerometer_handler(value):
    if time.clock()-delay > timeout:
        return
    settings.data_holder.update_data("muse_accelerometer", value)


def eeg_gyro_handler(value):
    if time.clock()-delay > timeout:
        return
    settings.data_holder.update_data("muse_gyro", value)


def eeg_touching_forehead_handler(value):
    if time.clock()-delay > timeout:
        return
    settings.data_holder.update_data("muse_touching_forehead", value)


def eeg_horseshoe_handler(value):
    if time.clock()-delay > timeout:
        return
    settings.data_holder.update_data("muse_horseshoe", value)
