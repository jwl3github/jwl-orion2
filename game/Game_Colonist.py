import Game_Object
from Data_CONST import *

# ==============================================================================
class Game_Colonist(Game_Object.Game_Object):
    def __init__(self, i_owner_id, i_race):
        super(Game_Colonist,self).__init__(i_owner_id)
        # Derived (as indicated in prior Game_Colony.raise_population code):
        self.r1           = i_owner_id
        self.a            = (i_owner_id << 4) | i_race  # JWL: a/b/c/d are named per original game; maybe change?
        self.b            = K_FARMER
        self.c            = 0x00
        self.d            = 0x00
        self.race         = i_race
        self.b_rioting    = False
        self.b_low_g      = False
        self.b_high_g     = False
# ------------------------------------------------------------------------------
    def init(self, PLAYERS):
        ''' Init used during start up and population growth. '''
        if self.race not in (K_RACE_NATIVE, K_RACE_ANDROID_FARMER, K_RACE_ANDROID_WORKER, K_RACE_ANDROID_SCIENTIST):
            self.b_low_g        = PLAYERS[self.race].get_racepick_item('low_g')
            self.b_high_g       = PLAYERS[self.race].get_racepick_item('high_g')
        self.setup_gravity_penalty()
# ------------------------------------------------------------------------------
    def init_unserialized(self, i_job_type, b_rioting, b_low_g, b_high_g):
        ''' Init used during colonist job change. '''
        self.set_job(i_job_type)
        self.b_rioting      = b_rioting
        self.b_low_g        = b_low_g
        self.b_high_g       = b_high_g
        self.setup_gravity_penalty()
# ------------------------------------------------------------------------------
    def setup_gravity_penalty(self):
        if self.b_low_g:
            self.v_gravity_penalty = [0.0, -0.2, -0.4]
        elif self.b_high_g:
            # Original MOO2 is not symmetric; high_g is relatively better.
            self.v_gravity_penalty = [0.0, 0.0, -0.2]
        else:  # Normal
            self.v_gravity_penalty = [-0.2, 0.0, -0.2]
# ------------------------------------------------------------------------------
    def allowed_job(self, i_job_type):
        if i_job_type == K_FARMER:
            if self.race in (K_RACE_ANDROID_WORKER, K_RACE_ANDROID_SCIENTIST):
                return False
            return True
        # Worker or Scientist:
        if self.is_native() or self.is_rioting():
            return False
        if i_job_type == K_WORKER and self.race in (K_RACE_ANDROID_FARMER, K_RACE_ANDROID_SCIENTIST):
            return False
        if i_job_type == K_SCIENTIST and self.race in (K_RACE_ANDROID_FARMER, K_RACE_ANDROID_WORKER):
            return False
        return True
# ------------------------------------------------------------------------------
    def is_rioting(self):
        return self.b_rioting
# ------------------------------------------------------------------------------
    def is_native(self):
        return (self.race == K_RACE_NATIVE)
# ------------------------------------------------------------------------------
    def is_android(self):
        return (self.race in (K_RACE_ANDROID_FARMER, K_RACE_ANDROID_WORKER, K_RACE_ANDROID_SCIENTIST))
# ------------------------------------------------------------------------------
    def set_job(self, i_job_type):
        self.b = i_job_type
# ------------------------------------------------------------------------------
    def get_gravity_penalty(self, o_planet, b_has_gravity_gen):
        if b_has_gravity_gen:
            return 0.0
        if self.is_android():
            return 0.0
        return self.v_gravity_penalty[o_planet.i_gravity]
