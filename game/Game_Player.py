import Game_Object
import re

# ==============================================================================
class Game_Player(Game_Object.Game_Object):

    def __init__(self, i_player_id):
        super(Game_Player,self).__init__(i_player_id)
        # Loaded
        self.i_player_id            = i_player_id
        self.s_emperor_name         = ''
        self.s_race_name            = ''
        self.i_picture              = 0
        self.i_color                = 0
        self.i_personality          = 0
        self.i_objective            = 0
        self.i_tax_rate             = 0
        self.i_bc                   = 0
        self.i_bc_income            = 0
        self.i_total_frighters      = 0
        self.i_used_frighters       = 0
        self.i_total_command        = 0
        self.i_industry             = 0
        self.i_research             = 0
        self.i_food                 = 0
        self.i_research_progress    = 0
        self.i_research_area        = 0
        self.i_research_tech_id     = 0
        self.v_known_techs          = []
        self.v_prototypes           = []
        self.v_tributes             = []
        self.d_racepicks            = {}
        # Derived
        self.i_used_command         = 0
        self.v_research_areas       = []
        self.i_research_cost        = 0
        self.i_research_turns_left  = 0
        self.v_explored_star_ids    = []
# ------------------------------------------------------------------------------
    def construct(self, d_init_struct):
        self.s_emperor_name         = d_init_struct['emperor_name']
        self.s_race_name            = d_init_struct['race_name']
        self.i_picture              = d_init_struct['picture']
        self.i_color                = d_init_struct['color']
        self.i_personality          = d_init_struct['personality']
        self.i_objective            = d_init_struct['objective']
        self.i_tax_rate             = d_init_struct['tax_rate']
        self.i_bc                   = d_init_struct['bc']
        self.i_bc_income            = d_init_struct['bc_income']
        self.i_total_frighters      = d_init_struct['total_frighters']
        self.i_used_frighters       = d_init_struct['used_frighters']
        self.i_total_command        = d_init_struct['total_command']
        self.i_industry             = d_init_struct['industry']
        self.i_research             = d_init_struct['research']
        self.i_food                 = d_init_struct['food']
        self.i_research_progress    = d_init_struct['research_progress']
        self.i_research_area        = d_init_struct['research_area']
        self.i_research_tech_id     = d_init_struct['research_tech_id']
        self.v_known_techs          = d_init_struct['known_techs']
        self.v_prototypes           = d_init_struct['prototypes']
        self.v_tributes             = d_init_struct['tributes']

        self.d_racepicks['goverment']                = d_init_struct['race_goverment']
        self.d_racepicks['population']               = d_init_struct['race_population']
        self.d_racepicks['farming']                  = d_init_struct['race_farming']
        self.d_racepicks['industry']                 = d_init_struct['race_industry']
        self.d_racepicks['science']                  = d_init_struct['race_science']
        self.d_racepicks['money']                    = d_init_struct['race_money']
        self.d_racepicks['ship_defense']             = d_init_struct['race_ship_defense']
        self.d_racepicks['ship_attack']              = d_init_struct['race_ship_attack']
        self.d_racepicks['ground_combat']            = d_init_struct['race_ground_combat']
        self.d_racepicks['spying']                   = d_init_struct['race_spying']
        self.d_racepicks['low_g']                    = d_init_struct['race_low_g']
        self.d_racepicks['high_g']                   = d_init_struct['race_high_g']
        self.d_racepicks['aquatic']                  = d_init_struct['race_aquatic']
        self.d_racepicks['subterranean']             = d_init_struct['race_subterranean']
        self.d_racepicks['large_home_world']         = d_init_struct['race_large_home_world']
        self.d_racepicks['rich_home_world']          = d_init_struct['race_rich_home_world']
        #self.d_racepicks['poor_home_world']         = d_init_struct['race_poor_home_world']
        self.d_racepicks['artifacts_home_world']     = d_init_struct['race_artifacts_home_world']
        self.d_racepicks['cybernetic']               = d_init_struct['race_cybernetic']
        self.d_racepicks['lithovore']                = d_init_struct['race_lithovore']
        self.d_racepicks['repulsive']                = d_init_struct['race_repulsive']
        self.d_racepicks['charismatic']              = d_init_struct['race_charismatic']
        self.d_racepicks['uncreative']               = d_init_struct['race_uncreative']
        self.d_racepicks['creative']                 = d_init_struct['race_creative']
        self.d_racepicks['tolerant']                 = d_init_struct['race_tolerant']
        self.d_racepicks['fantastic_traders']        = d_init_struct['race_fantastic_traders']
        self.d_racepicks['telepathic']               = d_init_struct['race_telepathic']
        self.d_racepicks['lucky']                    = d_init_struct['race_lucky']
        self.d_racepicks['omniscience']              = d_init_struct['race_omniscience']
        self.d_racepicks['stealthy_ships']           = d_init_struct['race_stealthy_ships']
        self.d_racepicks['trans_dimensional']        = d_init_struct['race_trans_dimensional']
        self.d_racepicks['warlord']                  = d_init_struct['race_warlord']
# ------------------------------------------------------------------------------
    def __setattr__(self,  attr, value):
        self.__dict__[attr] = value
# ------------------------------------------------------------------------------
    def alive(self):
        return self.s_emperor_name != ''
# ------------------------------------------------------------------------------
    def get_racepick_item(self, s_item):
        return self.d_racepicks[s_item]
# ------------------------------------------------------------------------------
    def raise_bc(self):
        self.i_bc += self.i_bc_income
# ------------------------------------------------------------------------------
    def add_food(self, i_food):
        self.i_food += i_food
# ------------------------------------------------------------------------------
    def add_research(self, i_research):
        self.i_research += i_research
# ------------------------------------------------------------------------------
    def raise_research(self):
        self.i_research_progress += self.i_research
# ------------------------------------------------------------------------------
    def research_completed(self):
        return self.i_research_progress >= self.i_research_cost
# ------------------------------------------------------------------------------
    def set_research_turns_left(self, i_research_turns_left):
        if (i_research_turns_left) < 0:
            self.i_research_turns_left = 0
        else:
            self.i_research_turns_left = i_research_turns_left
# ------------------------------------------------------------------------------
    def add_known_technology(self, i_tech_id):
        self.v_known_techs.append(i_tech_id)
# ------------------------------------------------------------------------------
    def knows_technology(self, i_tech_id):
        return i_tech_id in self.v_known_techs
# ------------------------------------------------------------------------------
    def add_prototype(self, d_prototype):
        self.v_prototypes.append(d_prototype)
# ------------------------------------------------------------------------------
    def add_tribute(self, d_tribute):
        self.v_tributes.append(d_tribute)
# ------------------------------------------------------------------------------
    def update_research_areas(self, v_research_areas):
        self.v_research_areas = v_research_areas
# ------------------------------------------------------------------------------
    def knows_star_id(self, i_star_id):
        return i_star_id in self.v_explored_star_ids
# ------------------------------------------------------------------------------
    def add_explored_star_id(self, i_star_id):
        if i_star_id and not self.knows_star_id(i_star_id):
            self.v_explored_star_ids.append(i_star_id)
# ------------------------------------------------------------------------------
    def print_debug(self):
        print
        print("=== player_id = %i ===" % self.i_id)
        print(self.serialize())
# ------------------------------------------------------------------------------
    def print_research_debug(self):
        print("research_tech_id = %i, research_area = %i, research_progress = %i, " % (self.i_research_tech_id, self.i_research_area, self.i_research_progress))
# ------------------------------------------------------------------------------
    def as_str(self, x):
        return "'" + x + "'"
# ------------------------------------------------------------------------------
    def serialize(self):
        ''' Minimal-exchange highly trusted updater; avoiding pickle since player object contains so much static data. '''
        # Static values that are light weight and useful to include for debugging.
        s_fixed  = '\nself.i_id                  = ' + str(self.i_id)                   +  \
                   '\nself.i_player_id           = ' + str(self.i_player_id)            +  \
                   '\nself.s_emperor_name        = ' + self.as_str(self.s_emperor_name) +  \
                   '\nself.s_race_name           = ' + self.as_str(self.s_race_name)    +  \
                   '\nself.i_picture             = ' + str(self.i_picture)              +  \
                   '\nself.i_color               = ' + str(self.i_color)                +  \
                   '\nself.i_personality         = ' + str(self.i_personality)          +  \
                   '\nself.i_objective           = ' + str(self.i_objective)

        # Values that change often and transmit every turn.
        s_often  = '\nself.i_tax_rate            = ' + str(self.i_tax_rate)             +  \
                   '\nself.i_bc                  = ' + str(self.i_bc)                   +  \
                   '\nself.i_bc_income           = ' + str(self.i_bc_income)            +  \
                   '\nself.i_total_frighters     = ' + str(self.i_total_frighters)      +  \
                   '\nself.i_used_frighters      = ' + str(self.i_used_frighters)       +  \
                   '\nself.i_total_command       = ' + str(self.i_total_command)        +  \
                   '\nself.i_used_command        = ' + str(self.i_used_command)         +  \
                   '\nself.i_industry            = ' + str(self.i_industry)             +  \
                   '\nself.i_research            = ' + str(self.i_research)             +  \
                   '\nself.i_food                = ' + str(self.i_food)                 +  \
                   '\nself.i_research_progress   = ' + str(self.i_research_progress)    +  \
                   '\nself.v_research_areas      = ' + str(self.v_research_areas)       +  \
                   '\nself.i_research_area       = ' + str(self.i_research_area)        +  \
                   '\nself.i_research_tech_id    = ' + str(self.i_research_tech_id)     +  \
                   '\nself.i_research_cost       = ' + str(self.i_research_cost)        +  \
                   '\nself.i_research_turns_left = ' + str(self.i_research_turns_left)

        # Large/complex data types that rarely change and should be tracked
        # via a 'dirty_XXX' flag.
        s_rare   = '\nself.v_known_techs         = ' + str(self.v_known_techs)          +  \
                   '\nself.v_prototypes          = ' + str(self.v_prototypes)           +  \
                   '\nself.v_tributes            = ' + str(self.v_tributes)             +  \
                   '\nself.d_racepicks           = ' + str(self.d_racepicks)
        s_serial = s_fixed + s_often # + s_rare
        #print s_serial
        return s_serial
# ------------------------------------------------------------------------------
    def unserialize(self, s_serial):
        try:
            exec(s_serial)
        except Exception as ex:
            print ("unserialize: exception: " + str(ex))
# ------------------------------------------------------------------------------
