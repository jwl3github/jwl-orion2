import Game_SpaceObject
import Data_CONST
from Data_CONST import *   # For K_xxx constants

# ==============================================================================
class Game_Ship(Game_SpaceObject.Game_SpaceObject):

    def __init__(self, i_ship_id):
        super(Game_Ship,self).__init__(i_ship_id)
        # Derived
        self.i_key1                  = None # image key is uninitialized
        self.i_key2                  = None # image key is uninitialized
        # Loaded
        self.d_design                = None
        self.i_owner_id              = -1
        self.i_status                = 0
        self.i_dest_star_id          = 0
        self.i_x                     = 0
        self.i_y                     = 0
        self.b_group_has_navigator   = False
        self.i_travelling_speed      = 0
        self.i_turns_left            = 0
        self.i_shield_damage_percent = 0
        self.i_drive_damage_percent  = 0
        self.i_computer_damage       = 0
        self.i_crew_quality          = 0
        self.i_crew_experience       = 0
        self.i_officer_id            = 0
        self.i_special_device_damage = 0
        self.i_armor_damage          = 0
        self.i_structural_damage     = 0
        self.i_mission               = 0
        self.b_just_built            = False
# ------------------------------------------------------------------------------
    def construct(self, d_init_struct):
        self.s_name                  = d_init_struct['name']
        self.d_design                = d_init_struct['design']
        self.i_owner_id              = d_init_struct['owner_id']
        self.i_status                = d_init_struct['status']
        self.i_dest_star_id          = d_init_struct['dest_star_id']
        self.i_x                     = d_init_struct['x']
        self.i_y                     = d_init_struct['y']
        self.b_group_has_navigator   = d_init_struct['group_has_navigator']
        self.i_travelling_speed      = d_init_struct['travelling_speed']
        self.i_turns_left            = d_init_struct['turns_left']
        self.i_shield_damage_percent = d_init_struct['shield_damage_percent']
        self.i_drive_damage_percent  = d_init_struct['drive_damage_percent']
        self.i_computer_damage       = d_init_struct['computer_damage']
        self.i_crew_quality          = d_init_struct['crew_quality']
        self.i_crew_experience       = d_init_struct['crew_experience']
        self.i_officer_id            = d_init_struct['officer_id']
        self.i_special_device_damage = d_init_struct['special_device_damage']
        self.i_armor_damage          = d_init_struct['armor_damage']
        self.i_structural_damage     = d_init_struct['structural_damage']
        self.i_mission               = d_init_struct['mission']
        self.b_just_built            = d_init_struct['just_built']
# ------------------------------------------------------------------------------
    def print_debug(self, o_owner_player, stars):
        print
        print("=== ship # %i ... %s ===" % (self.i_id, o_owner_player.race_name))
        print("    status       = %i" % self.i_status)
        print("    coords       = %i, %i" % (self.i_x, self.i_y))
        print("    dest_star_id = %i" % (self.i_dest_star_id))
        print("    turns_left   = %i" % self.i_turns_left)
#	    print("    group_has_navigator = %i" % self.get_group_has_navigator())
#	    print("    mission = %i" % self.i_mission)
#       print("    star: %s" % stars[self.get_location()].get_name())
#       print("    star: %s" % stars[self.get_location_x()].get_name())
#        for star_id in stars:
#            print("star # %i ... %s" % (star_id, stars[star_id].get_name()))
#        print("/ship")
        print
# ------------------------------------------------------------------------------
    def get_picture(self):
        return self.design['picture']

    def get_shield(self):
        return self.design['shield']

    def get_computer(self):
        return self.design['computer']

    def get_size(self):
        return self.design['size']

    def exists(self):
        return self.i_status != K_SHIP_STATUS_DELETED

    def get_status_text(self):
        return Data_CONST.get_text_list('SHIP_STATUS')[self.i_status]

    def set_orbiting(self):
        self.i_status = K_SHIP_STATUS_ORBITING

    def is_orbiting(self):
        return self.i_status == K_SHIP_STATUS_ORBITING

    def set_travelling(self):
        self.i_status = K_SHIP_STATUS_TRAVEL

    def is_travelling(self):
        return self.i_status == K_SHIP_STATUS_TRAVEL

    def set_launching(self):
        self.i_status = K_SHIP_STATUS_LAUNCH

    def is_launching(self):
        return self.i_status == K_SHIP_STATUS_LAUNCH

    def has_no_image(self):
        if self.i_key1 is None and self.i_key2 is None:
            return True
        return False

    def set_image_keys(self,subkey1,subkey2):
        self.i_key1 = subkey1; # color 0..7
        self.i_key2 = subkey2; # index  0..49

    def get_image_keys(self):
        return [self.i_key1, self.i_key2];

    def determine_image_keys(self,i_color):
        """finds out the keys for the ship image from the loaded data.
        This is necessary because during savegame loading,
        there is no information on player's color,
        so the correct image can't be assigned"""
        i_pict = self.design['picture']
        self.set_image_keys(i_color, i_pict)

