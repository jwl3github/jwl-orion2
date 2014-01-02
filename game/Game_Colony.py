import math
import time

import Data_BUILDINGS
import Game_Colonist
import Game_Object
import Game_Rules

from Data_CONST import *

# ==============================================================================
class Game_Colony(Game_Object.Game_Object):
    def __init__(self, i_colony_id):
        super(Game_Colony,self).__init__(i_colony_id)
        # Derived:
        self.o_planet                   = None
        self.i_industry_progress        = 0
        self.i_bc                       = 0
        self.d_colonists                = {K_FARMER: [], K_WORKER: [], K_SCIENTIST: []}
        self.v_build_queue              = []
        self.v_build_queue_ids          = []
        self.v_available_production     = []
        self.v_max_populations          = []
        # Loaded:
        self.i_colony_id                = i_colony_id
        self.i_owner_id                 = 0
        self.i_allocated_to             = 0
        self.i_planet_id                = 0
        self.i_officer_id               = 0
        self.b_is_outpost               = False
        self.i_morale                   = 0
        self.i_pollution                = 0
        self.i_population               = 0
        self.i_assignment               = 0
        self.v_pop_raised               = []
        self.v_pop_grow                 = []
        self.i_num_turns_existed        = 0
        self.i_food2_per_farmer         = 0
        self.i_industry_per_worker      = 0
        self.i_research_per_scientist   = 0
        self.i_max_farms                = 0
        self.i_max_population           = 0
        self.i_climate                  = 0
        self.i_ground_strength          = 0
        self.i_space_strength           = 0
        self.i_food                     = 0
        self.i_industry                 = 0
        self.i_research                 = 0
        self.i_num_marines              = 0
        self.i_num_armors               = 0
        self.v_building_ids             = []
# ------------------------------------------------------------------------------
    def construct(self, d_init_struct, PLAYERS):
        self.i_colony_id                = d_init_struct['colony_id']
        self.i_owner_id                 = d_init_struct['owner_id']
        self.i_allocated_to             = d_init_struct['allocated_to']
        self.i_planet_id                = d_init_struct['planet_id']
        self.i_officer_id               = d_init_struct['officer_id']
        self.b_is_outpost               = d_init_struct['is_outpost']
        self.i_morale                   = d_init_struct['morale']
        self.i_pollution                = d_init_struct['pollution']
        self.i_population               = d_init_struct['population']
        self.i_assignment               = d_init_struct['assignment']
        self.v_pop_raised               = d_init_struct['pop_raised']
        self.v_pop_grow                 = d_init_struct['pop_grow']
        self.i_num_turns_existed        = d_init_struct['num_turns_existed']
        self.i_food2_per_farmer         = d_init_struct['food2_per_farmer']
        self.i_industry_per_worker      = d_init_struct['industry_per_worker']
        self.i_research_per_scientist   = d_init_struct['research_per_scientist']
        self.i_max_farms                = d_init_struct['max_farms']
        self.i_max_population           = d_init_struct['max_population']
        self.i_climate                  = d_init_struct['climate']
        self.i_ground_strength          = d_init_struct['ground_strength']
        self.i_space_strength           = d_init_struct['space_strength']
        self.i_food                     = d_init_struct['food']
        self.i_industry                 = d_init_struct['industry']
        self.i_research                 = d_init_struct['research']
        self.i_num_marines              = d_init_struct['num_marines']
        self.i_num_armors               = d_init_struct['num_armors']
        self.v_building_ids             = d_init_struct['building_ids']
        for i_type, v_colonists in d_init_struct['colonists'].items():
            for d_colonist in v_colonists:
                o_colonist        = Game_Colonist.Game_Colonist(d_colonist['r1'], d_colonist['race'], PLAYERS)
                o_colonist.a      = d_colonist['a']
                o_colonist.b      = d_colonist['b']
                o_colonist.c      = d_colonist['c']
                o_colonist.d      = d_colonist['d']
                self.d_colonists[i_type].append(o_colonist)
# ------------------------------------------------------------------------------
    def print_info(self):
        print "  owner_id: %i" % self.i_owner_id
# ------------------------------------------------------------------------------
    def has_building(self, b_id):
        return b_id in self.v_building_ids
# ------------------------------------------------------------------------------
    def add_building(self, building_id):
        if not self.has_building(building_id):
            self.v_building_ids.append(building_id)
# ------------------------------------------------------------------------------
    def init_available_production(self, rules, players):
        """returns a dict of production id lists"""

        rules_buildings = rules['buildings']
        known_techs     = players[self.i_owner_id].v_known_techs
        replaced        = []

        for production_id in self.v_building_ids:
            if rules_buildings[production_id].has_key('replaces'):
                for replaces_id in rules_buildings[production_id]['replaces']:
                    replaced.append(replaces_id)

        available = {'building': [], 'xship': [], 'special': [], 'capitol': []}
        for production_id, production in rules_buildings.items():
            if production['tech']:
                if (production['tech'] in known_techs) and (not self.has_building(production_id)) and (not production_id in replaced):
                    # knows required technology and not built
                    available_item = "%s:%i" % (production['name'], production_id)
                    if production.has_key('type'):
                        available[production['type']].append(available_item)
                    else:
                        available['building'].append(available_item)

        for group_id in available:
            available[group_id].sort()
            for i in range(len(available[group_id])):
                available[group_id][i] = int(available[group_id][i].split(":")[1])

# TODO: check for gravity and colonists, if the gravity generator is not needed here remove it from the list
# TODO: check for colonists if the alien management center is needed, otherwise remove it from the list

        self.v_available_production = available
# ------------------------------------------------------------------------------
    def get_available_production(self):
        return self.v_available_production
# ------------------------------------------------------------------------------
    def display_summary(self, title, foot, summary):
        v_summary = []
        total = rules.count_summary_result(summary)
        print("+----------------------------------------------------+")
        print("+ %s +" % title.ljust(50))
        print("+ ================================================== +")
        for k in summary:
            if summary[k]:
                print("+ %s ... %s +" % (str(summary[k]).rjust(6), k.ljust(39)))
                v_summary.append("%s   %s" % (str(summary[k]).rjust(6), k.ljust(39)))
        print("+                                                    +")
        print("+ % 6i ... %s +" % (total, foot.ljust(39)))
        print("+----------------------------------------------------+")
        v_summary.append(' ')
        v_summary.append("% 6i ... %s" % (total, foot.ljust(39)))
        return v_summary
# ------------------------------------------------------------------------------
    def print_morale_summary(self):
        return self.display_summary("Morale Summary", "Total", self.morale_summary)
# ------------------------------------------------------------------------------
    def print_bc_summary(self):
        return self.display_summary("BC Summary", "Total Income", self.bc_summary)
# ------------------------------------------------------------------------------
    def print_food_summary(self):
        return self.display_summary("Food Summary", "Total Food Produced", self.food_summary)
# ------------------------------------------------------------------------------
    def print_industry_summary(self):
        return self.display_summary("Industry Summary", "Total Industry Produced", self.industry_summary)
# ------------------------------------------------------------------------------
    def print_research_summary(self):
        return self.display_summary("Research Summary", "Research Industry Produced", self.research_summary)
# ------------------------------------------------------------------------------
    def exists(self):
        return self.i_owner_id < 0xff
# ------------------------------------------------------------------------------
    def is_owned_by(self, player_id):
        return self.exists() and self.i_owner_id == player_id
# ------------------------------------------------------------------------------
    def is_outpost(self):
        return self.exists() and self.b_is_outpost
# ------------------------------------------------------------------------------
    def is_colony(self):
        return self.exists() and not self.is_outpost()
# ------------------------------------------------------------------------------
    def update_industry_progress(self):
        # Amount of industry accumulated for the current build item.
        self.i_industry_progress += self.i_industry
        return self.i_industry_progress
# ------------------------------------------------------------------------------
    def reset_industry_progress(self):
        self.i_industry_progress = 0
# ------------------------------------------------------------------------------
    def get_build_queue_ids(self):
        id_list = []
        for item in self.v_build_queue:
            id_list.append(item['production_id'])
        return id_list
# ------------------------------------------------------------------------------
    def add_build_item(self, production_id, flags = 0):
        if len(self.v_build_queue) < 7:
           self.v_build_queue.append({'production_id': production_id, 'flags': flags})
# ------------------------------------------------------------------------------
    def remove_build_item(self, production_id):
        build_queue_ids = self.v_build_queue_ids
        if production_id in build_queue_ids:
            self.v_build_queue.pop(build_queue_ids.index(production_id))
# ------------------------------------------------------------------------------
    def get_build_item(self):
        if len(self.v_build_queue) < 1:
            return None
        elif self.v_build_queue[0]['production_id'] == 0xFF:
            return None
        elif self.v_build_queue[0]['production_id'] == 249:  # repeat
            return self.v_build_queue[1]
        else:
            return self.v_build_queue[0]
# ------------------------------------------------------------------------------
    def in_build_queue(self, production_id):
        return production_id in self.v_build_queue_ids
# ------------------------------------------------------------------------------
    def get_aggregated_populations(self):
        pops    = [0, 0, 0, 0, 0, 0, 0, 0]
        for t in [K_FARMER, K_WORKER, K_SCIENTIST]:
            for colonist in self.d_colonists[t]:
                pops[colonist.race] += 1
        return pops
# ------------------------------------------------------------------------------
    def raise_population(self, PLAYERS):
        """
        raise the population
        """
        if self.i_owner_id == 0xff:
            print "owner is 0xff"
            return

        v_max_populations = self.v_max_populations
        for i_race in range(K_MAX_PLAYERS):
            self.v_pop_raised[i_race] += self.v_pop_grow[i_race]
            if self.v_pop_raised[i_race] > 999:
                # the race that turns over 999 in v_pop_raised gets a new farmer
                colonist = Game_Colonist(self.i_owner_id, i_race, PLAYERS)
                self.d_colonists[K_FARMER].append(colonist)
                self.v_pop_raised[i_race] -= 1000
                self.i_population += 1
# ------------------------------------------------------------------------------
    def total_population(self):
        return len(self.d_colonists[K_FARMER]) + len(self.d_colonists[K_WORKER]) + len(self.d_colonists[K_SCIENTIST])
# ------------------------------------------------------------------------------
    def summary_result(self, summary):
        res = 0.0
        for k, v in summary.iterkeys():
            res += float(v)
        return res
# ------------------------------------------------------------------------------
    def recount_outpost(self):
#       print "this is outpost"
        self.i_population     = 0
        self.i_pollution      = 0
        self.i_industry       = 0
        self.i_research       = 0
#       self.food_summary     = {}
#       self.industry_summary = {}
#       self.research_summary = {}

# ------------------------------------------------------------------------------
    def recount(self, RULES, colony_leader, PLAYERS):
        """
        recounts colony values, should be called after any change
        """
        print "$$$ colony::recount() ... colony_id = %i" % self.i_id
        start_clock = time.clock()

        self.i_bc = 0

        if not self.exists():
            self.i_population      = 0
            self.v_max_populations = Game_Rules.get_empty_max_populations()
            return

        if self.is_outpost():
            self.recount_outpost()
            self.v_max_populations = Game_Rules.get_empty_max_populations()
            return

        self.d_prod_summary      = Game_Rules.compose_prod_summary(RULES, self, colony_leader, PLAYERS)
        self.i_morale            = self.d_prod_summary['morale_total']
        self.i_food              = self.d_prod_summary['food_total']
        self.i_industry          = self.d_prod_summary['industry_total']
        self.i_pollution         = self.d_prod_summary['industry_pollution']
        self.i_research          = self.d_prod_summary['research_total']
        #self.i_bc                = self.d_prod_summary['bc_total']
        self.v_max_populations   = Game_Rules.compose_max_populations(RULES, self, PLAYERS)
        self.v_pop_grow          = Game_Rules.compose_pop_growth(RULES, self, colony_leader, PLAYERS)
        self.i_max_population    = max(self.v_max_populations)

        self.init_available_production(RULES, PLAYERS)

        end_clock = time.clock()
        print "$$$ colony::recount() ... clock elapsed = %f" % (end_clock-start_clock)
# ------------------------------------------------------------------------------
    def debug_production(self, rules):
        print("    @ colony::debug_production()... colony_id = %i" % self.i_id)
        print("    @ colony::debug_production()... colony_id = %i" % self.i_colony_id)
        for build_item in self.v_build_queue:
            production_id = build_item['production_id']
            if rules['buildings'][production_id].has_key('type'):
                type = rules['buildings'][production_id]['type']
            else:
                type = "building"
            print("        production_id: %3i ... flags: %3i ... type: %10s ... %s" % (production_id, build_item['flags'], type, rules['buildings'][production_id]['name']))
        print
# ==============================================================================
class Game_EnemyColony(Game_Colony):

    def __init__(self, colony_id, player_id):
        super(Game_EnemyColony,self).__init__(colony_id)
        self.i_owner_id = player_id

    def is_outpost(self):
        return False
