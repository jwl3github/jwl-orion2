import Game_Object
from Data_CONST import *

# ==============================================================================
class Game_Colonist(Game_Object.Game_Object):
    def __init__(self, i_owner_id, i_race, PLAYERS):
        super(Game_Colonist,self).__init__(i_owner_id)
        # Derived (as indicated in prior Game_Colony.raise_population code):
        self.r1           = i_owner_id
        self.a            = (i_owner_id << 4) | i_race
        self.b            = K_FARMER
        self.c            = 0x00
        self.d            = 0x00
        self.race         = i_race
        self.android      = False
        self.native       = False
        self.rioting      = False

        if PLAYERS[i_race].get_racepick_item('low_g'):
            self.v_gravity_penalty = [0.0, -0.2, -0.4]
        elif PLAYERS[i_race].get_racepick_item('high_g'):
            # Original MOO2 is not symmetric; high_g is relatively better.
            self.v_gravity_penalty = [0.0, 0.0, -0.2]
        else:  # Normal
            self.v_gravity_penalty = [-0.2, 0.0, -0.2]
# ------------------------------------------------------------------------------
    def get_gravity_penalty(self, o_planet, b_has_gravity_gen):
        if b_has_gravity_gen:
            return 0.0
        if self.android:
            return 0.0
        return self.v_gravity_penalty[o_planet.i_gravity]
