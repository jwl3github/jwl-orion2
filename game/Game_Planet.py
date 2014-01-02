from Data_CONST import *
import Data_CONST
import Game_Object

class Game_Planet(Game_Object.Game_Object):

    def __init__(self, i_planet_id):
        super(Game_Planet,self).__init__(i_planet_id)
        self.i_colony_id        = 0
        self.i_star_id          = 0
        self.i_position         = 0
        self.i_type             = 0
        self.i_size             = 0
        self.i_gravity          = 0
        self.i_group            = 0
        self.i_terrain          = 0
        self.i_picture          = 0
        self.i_minerals         = 0
        self.i_foodbase         = 0
        self.i_terraformations  = 0
        self.i_max_farms        = 0
        self.i_max_population   = 0
        self.i_special          = 0
        self.i_flags            = 0

    def construct(self, d_init_struct):
        self.i_colony_id        = d_init_struct['colony_id']
        self.i_star_id          = d_init_struct['star_id']
        self.i_position         = d_init_struct['position']
        self.i_type             = d_init_struct['type']
        self.i_size             = d_init_struct['size']
        self.i_gravity          = d_init_struct['gravity']
        self.i_group            = d_init_struct['group']
        self.i_terrain          = d_init_struct['terrain']
        self.i_picture          = d_init_struct['picture']
        self.i_minerals         = d_init_struct['minerals']
        self.i_foodbase         = d_init_struct['foodbase']
        self.i_terraformations  = d_init_struct['terraformations']
        self.i_max_farms        = d_init_struct['max_farms']
        self.i_max_population   = d_init_struct['max_population']
        self.i_special          = d_init_struct['special']
        self.i_flags            = d_init_struct['flags']

    def has_gold(self):
        return self.i_special == K_SPECIAL_GOLD

    def has_artifacts(self):
        return self.i_special == K_SPECIAL_ARTIFACTS

    def get_size_text(self):
        return Data_CONST.get_planet_size_text(self.i_size)

    def get_terrain_text(self):
        return Data_CONST.get_planet_terrain_text(self.i_terrain)

    def get_minerals_text(self):
        return Data_CONST.get_planet_minerals_text(self.i_minerals)

    def is_asteroid_belt(self):
        return self.i_type == K_PLANET_ASTEROID

    def is_gas_giant(self):
        return self.i_type == K_PLANET_GAS_GIANT

    def is_planet(self):
        return self.i_type == K_PLANET_HABITABLE

    def get_gravity_text(self):
        return Data_CONST.get_planet_gravity_text(self.i_gravity)

    def is_low_g(self):
        return (self.i_gravity == K_PLANET_LOW_G)

    def is_normal_g(self):
        return (self.i_gravity == K_PLANET_NORMAL_G)

    def is_high_g(self):
        return (self.i_gravity == K_PLANET_HIGH_G)

