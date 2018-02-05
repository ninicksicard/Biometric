# hold all profiles
# save/load profiles
# handle profile list and horder
import ProfilTest1


class ProfileHolder:
    def __init__(self):
        self.profile_list = [ProfilTest1.Profile()]
        self.order = (self.profile_list[0],
                      self.profile_list[3],
                      self.profile_list[4],
                      self.profile_list[2],
                      self.profile_list[6],
                      self.profile_list[4],
                      self.profile_list[3],
                      self.profile_list[2],
                      self.profile_list[9],
                      self.profile_list[8]
                      )

holder = ProfileHolder()


def load_settings():
    pass
    # for files in a folder, create a profile. for each value of the dict, literal eval "self."+dict[key]+ "= dict[value]"   .......ca s'ecrit pas comme ca...


def save_settings():
    for settings in holder.profile_list:
        print(settings.all_profiles_settings)


def create_profile():  # fill and run once to create new file with profile settings
    #juste imprimer un dictionnaire similaire dans un fichier similaire.
    pass

# for quick calls
profile0 = holder.order[0]
profile1 = holder.order[1]
profile2 = holder.order[2]
profile3 = holder.order[3]
profile4 = holder.order[4]
profile5 = holder.order[5]
profile6 = holder.order[6]
profile7 = holder.order[7]
