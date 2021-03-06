import math
import time
import Moo2_Savegame
import Game_Rules
import Game_Colony
import Game_Planet
import Game_Player
import Game_Star
import Game_Ship
import Data_CONST
from Data_CONST import *   # All K_xxx constants

PARSEC_LENGTH = 30

# ------------------------------------------------------------------------------
def stardate(i):
    s = str(i)
    return s[:-1] + "." + s[-1]
# ------------------------------------------------------------------------------
def debug_timing(sc, info):
    ec = time.clock()
    if sc > 0:
        print '                                         debug_timing: %7.5f .. %s' % (ec-sc, info)
    return ec
# ==============================================================================
class Game_Main(object):
# ------------------------------------------------------------------------------
    def __init__(self, d_rules, game_file = None):
        self.d_rules      = d_rules
        self.d_galaxy     = {}
        self.d_game_opts  = {}
        self.d_planets    = {}
        self.d_stars      = {}
        self.d_colonies   = {}
        self.d_heroes     = {}
        self.d_players    = {}
        self.d_ships      = {}
        if game_file:
            self.load_moo2_savegame(game_file)
# ------------------------------------------------------------------------------
    def init_game_opts(self):
        # Currently, there is no separate class so just share data.
        self.d_game_opts = self.d_load_game_opts
# ------------------------------------------------------------------------------
    def init_galaxy(self):
        # Currently, there is no separate class so just share data.
        self.d_galaxy = self.d_load_galaxy
# ------------------------------------------------------------------------------
    def init_planets(self):
        # Transfer generic loaded data into game memory object.
        for i_id, d_struct in self.d_load_planets.items():
            self.d_planets[i_id] = Game_Planet.Game_Planet(i_id)
            self.d_planets[i_id].construct(d_struct)
# ------------------------------------------------------------------------------
    def init_stars(self):
        # Transfer generic loaded data into game memory object.
        for i_id, d_struct in self.d_load_stars.items():
            self.d_stars[i_id] = Game_Star.Game_Star(i_id)
            self.d_stars[i_id].construct(d_struct)

        # Perform extra cross-indexing / info caching.
        self.d_stars_by_coords = {}
        for i_id, d_star in self.d_stars.items():
            k = "%i:%i" % (d_star.i_x, d_star.i_y)
            self.d_stars_by_coords[k] = d_star
            i_num = 0
            for i_object_id in d_star.v_object_ids:
                if self.d_planets.has_key(i_object_id):
                    i_num += 1
                    self.d_planets[i_object_id].i_position = i_num
                    self.d_planets[i_object_id].s_name = '%s %i' % (d_star.s_name, i_num)
                elif i_object_id != 0xffff:
                    print 'WARNING: init_stars -- ignoring invalid planet object id: %d' % i_object_id
# ------------------------------------------------------------------------------
    def init_colonies(self):
        # Transfer generic loaded data into game memory object.
        for i_id, d_struct in self.d_load_colonies.items():
            self.d_colonies[i_id] = Game_Colony.Game_Colony(i_id)
            self.d_colonies[i_id].construct(d_struct, self.d_players)

        # Perform extra cross-indexing / info caching.
        for i_id, d_colony in self.d_colonies.items():
            if d_colony.i_owner_id < 0xff:
                o_planet          = self.d_planets[d_colony.i_planet_id]
                d_colony.o_planet = o_planet
                d_colony.s_name   = o_planet.s_name
# ------------------------------------------------------------------------------
    def init_heroes(self):
        # Transfer generic loaded data into game memory object.
        for i_id, d_struct in self.d_load_heroes.items():
            # Currently, there is no separate class for Hero, so just share data.
            self.d_heroes[i_id] = d_struct
            #self.d_heroes[i_id] = Game_Hero.Game_Hero(i_id)
            #self.d_heroes[i_id].construct(d_struct)

        # Perform extra cross-indexing / info caching.
        self.d_players_heroes = {}
        for i_id, d_hero in self.d_heroes.items():
            i_player_id = d_hero['player']
            if i_player_id != 0xFF:
                if not self.d_players_heroes.has_key(i_player_id):
                    self.d_players_heroes[i_player_id] = {}
                self.d_players_heroes[i_player_id][d_hero['id']] = d_hero
# ------------------------------------------------------------------------------
    def init_players(self):
        # Transfer generic loaded data into game memory object.
        for i_id, d_struct in self.d_load_players.items():
            self.d_players[i_id] = Game_Player.Game_Player(i_id)
            self.d_players[i_id].construct(d_struct)

        # Perform extra cross-indexing / info caching.
        for i_player_id, o_player in self.d_players.items():
            self.determine_player_research_areas(o_player)
            for i_star_id, o_star in self.d_stars.items():
                if o_star.visited_by_player(i_player_id):
                    o_player.add_explored_star_id(i_star_id)
# ------------------------------------------------------------------------------
    def init_ships(self):
        # Transfer generic loaded data into game memory object.
        for i_id, d_struct in self.d_load_ships.items():
            self.d_ships[i_id] = Game_Ship.Game_Ship(i_id)
            self.d_ships[i_id].construct(d_struct)
# ------------------------------------------------------------------------------
    def load_moo2_savegame(self, filename):
        """
        Loads the original MOO2 savegame
        """
        savegame              = Moo2_Savegame.Moo2_Savegame(filename)
        self.d_load_game_opts = savegame.parse_game_opts()
        self.d_load_galaxy    = savegame.parse_galaxy()
        self.d_load_heroes    = savegame.parse_heroes()
        self.d_load_players   = savegame.parse_players()
        self.d_load_stars     = savegame.parse_stars()
        self.d_load_planets   = savegame.parse_planets()
        self.d_load_colonies  = savegame.parse_colonies()
        self.d_load_ships     = savegame.parse_ships()

        self.init_game_opts()
        self.init_galaxy()
        self.init_planets()
        self.init_stars()
        self.init_heroes()
        self.init_players()
        self.init_colonies()
        self.init_ships()
        self.recount()  # Establish some basic derived values.
# ------------------------------------------------------------------------------
    def list_area_tech_ids(self, i_research_area):
        v_techs = []
        for i_tech_id in self.d_rules['tech_table']:
            if self.d_rules['tech_table'][i_tech_id]['area'] == i_research_area:
                v_techs.append(i_tech_id)
        return sorted(v_techs)
# ------------------------------------------------------------------------------
    def recount_heroes(self):
        ###JWL : Does this really need to be done as a nested loop each turn???
        print "=== Recount Heroes ==="
        for i_hero_id, d_hero in self.d_heroes.items():
            d_hero['level'] = 0
            for i_level in self.d_rules['hero_levels']:
                if d_hero['experience'] >= i_level:
                    d_hero['level'] += 1
                   #print 'Hero %s leveled up to %d' % (d_hero['name'], d_hero['level'])
# ------------------------------------------------------------------------------
    def recount_colonies(self):
        print "=== Recount Colonies ==="

        # JWL: TODO Optimize with a per-player 'dirty' flag (or set player.d_allowed_production to None?)
        for i_player_id, o_player in self.d_players.items():
            o_player.determine_allowed_production(self.d_rules)

        for i_colony_id, o_colony in self.d_colonies.items():
            if o_colony.exists():
                o_colony.recount(self.d_rules, self.get_governor(i_colony_id), self.d_players)
# ------------------------------------------------------------------------------
    def colony_owned_by(self, i_colony_id, i_player_id):
        """ Returns True if the given i_colony_id belongs to the indicated player. """
        return self.d_colonies[i_colony_id].is_owned_by(i_player_id)
# ------------------------------------------------------------------------------
    def get_governor(self, i_colony_id):
        i_owner_id  = self.d_colonies[i_colony_id].i_owner_id
        i_star_star = self.d_colonies[i_colony_id].o_planet.i_star_id
        for i_hero_id in self.list_player_governors(i_owner_id):
            if self.d_heroes[i_hero_id]['location'] == i_star_id:
                return self.d_heroes[i_hero_id]
        return None
# ------------------------------------------------------------------------------
    def list_player_heroes(self, i_player_id, i_hero_type):
        d_list = {}
        if self.d_players_heroes.has_key(i_player_id):
            for i_hero_id, o_hero in self.d_players_heroes[i_player_id].items():
                if o_hero['type'] == i_hero_type:
                    d_list[i_hero_id] = o_hero
        return d_list
# ------------------------------------------------------------------------------
    def list_player_officers(self, i_player_id):
        return self.list_player_heroes(i_player_id, K_HERO_OFFICER)
# ------------------------------------------------------------------------------
    def list_player_governors(self, i_player_id):
        return self.list_player_heroes(i_player_id, K_HERO_GOVERNOR)
# ------------------------------------------------------------------------------
    def update_player_research(self, o_player):
        print("@ Game_Main::update_player_research() - cost = %d" % o_player.i_research_cost)
        if o_player.i_research_cost > 0:
            o_player.raise_research()
            if o_player.research_completed():
                print "research completed"
                print o_player.v_known_techs
                print o_player.i_research_tech_id
                o_player.add_known_technology(o_player.i_research_tech_id)
                o_player.i_research_progress = 0
                o_player.v_research_areas = None
                self.update_research(o_player.i_player_id, 0)
                self.determine_player_research_areas(o_player)
# ------------------------------------------------------------------------------
    def update_research(self, i_player_id, i_tech_id):
        print("Game_Main::update_research() ... player_id = %i, tech_id = %i" % (i_player_id, i_tech_id))
        o_player = self.d_players[i_player_id]
        o_player.i_research_tech_id     = i_tech_id
        o_player.i_research_area        = self.d_rules['tech_table'][i_tech_id]['area']
        o_player.i_research_cost        = Game_Rules.research_costs(self.d_rules['research_areas'], o_player.i_research_area, o_player.i_research)
        o_player.i_research_turns_left  = Game_Rules.research_turns(o_player.i_research_cost, o_player.i_research_progress, o_player.i_research)
        return True   # Checked by Network_Server
# ------------------------------------------------------------------------------
    def change_colonist_job(self, i_player_id, i_colony_id, i_from_job, i_from_index, i_to_job):
        if not self.d_colonies.has_key(i_colony_id):
            print 'change_colonist_job: Invalid colony id (no such colony): ' + i_colony_id
            return False

        o_colony = self.d_colonies[i_colony_id] if self.d_colonies.has_key(i_colony_id) else None
        if o_colony.i_owner_id != i_player_id:
            print 'change_colonist_job: Request from incorrect player <%d> owned by <%d>' % (i_player_id, o_colony.i_owner_id)
            return False

        print 'change_colonist_job -> from [%d] index [%d]  to [%d]' % (i_from_job, i_from_index, i_to_job)
        if i_from_job not in (K_FARMER, K_WORKER, K_SCIENTIST):
            print 'Invalid i_from_job <%d>' % i_from_job
            return False

        if i_to_job not in (K_FARMER, K_WORKER, K_SCIENTIST):
            print 'change_colonist_job: Invalid i_to_job <%d>' % i_to_job
            return False

        if i_from_job == i_to_job:
            print 'change_colonist_job: Colonists moved back to same job. Job change ignored.'
            return True

        if (i_to_job == K_FARMER) and not o_colony.allows_farming():
            print 'change_colonist_job: Cannot have farmers on this planet. Job change ignored.'
            return True

        c = len(o_colony.d_colonists[i_from_job]) - 1
        while c >= i_from_index:
            if o_colony.d_colonists[i_from_job][c].allowed_job(i_to_job):
                print 'change_colonist_job: Move colonist <%d> to new job <%d>.' % (c, i_to_job)
                o_colony.d_colonists[i_from_job][c].set_job(i_to_job)
                o_colony.d_colonists[i_to_job].append(o_colony.d_colonists[i_from_job].pop(c))
            else:
                print 'change_colonist_job: Cannot move colonist <%d> to unqualified job. Job change ignored.' % c
            c -= 1

        self.recount_colony(i_colony_id)
        self.recount_player(i_player_id)
        return True
# ------------------------------------------------------------------------------
    def determine_player_research_areas(self, o_player):
        # Determine the player's upcoming research area by checking
        # for a known tech in the progressive area of each tech
        # category until none is found.
        research_areas = {}
        for res_id in self.d_rules['research']:
            area_id = self.d_rules['research'][res_id]['start_area']
            #print "                         AREA: %s" % res_id
            #print "                         start_area = %i" % area_id
            while self.d_rules['research_areas'][area_id]['next']:
                #print "      checking area_id = %i" % area_id
                area_techs = self.list_area_tech_ids(area_id)
                #print "          area_techs = %s" % str(area_techs)
                new_area_id = 0
                for tech_id in area_techs:
                    if o_player.knows_technology(tech_id):
                        #print "known tech! ... %i .. moving to next area" % tech_id
                        new_area_id = self.d_rules['research_areas'][area_id]['next']
                        break
                if new_area_id:
                    area_id = new_area_id
                else:
                    break
            research_areas[res_id] = self.list_area_tech_ids(area_id)
        o_player.v_research_areas = research_areas
# ------------------------------------------------------------------------------
    def set_colony_build_queue(self, i_player_id, i_colony_id, v_build_queue):
        """ Sets a new build queue for a given colony_id owned by player_id

        """
        print("@ Game_Main::set_colony_build_queue()")
        print("    colony_id: %i" % i_colony_id)
        print("    build_queue: %s" % str(v_build_queue))
        if not self.colony_owned_by(i_colony_id, i_player_id):
            return False
        # TODO: <security> validate the build queue based on colony's allowed buildings
        self.d_colonies[i_colony_id].v_build_queue = v_build_queue
        return True
# ------------------------------------------------------------------------------
    def recount_colony(self, i_colony_id):
        if self.d_colonies.has_key(i_colony_id):
            self.d_colonies[i_colony_id].recount(self.d_rules, self.get_governor(i_colony_id), self.d_players)
# ------------------------------------------------------------------------------
    def recount_food_freighters(self, o_player):
        # Distribute food via frieghters if needed and able.
        i_can_ship = o_player.i_total_freighters - o_player.i_used_freighters
        if (i_can_ship <= 0):
            return
        for i_colony_id, o_colony in self.d_colonies.items():
            if not o_colony.exists() or (o_colony.i_owner_id != i_player_id):
                continue
            i_missing = o_colony.get_food_missing()
            if i_missing >= i_can_ship:
                o_colony.i_food_imported = i_can_ship
                o_player.i_used_freighters += i_can_ship
                return
            elif i_missing > 0:
                o_colony.i_food_imported = i_missing
                o_player.i_used_freighters += i_missing
        ### TODO Force player's i_food to show non-importable food shortage as a negative??
# ------------------------------------------------------------------------------
    def recount_player(self, i_player_id):
        print "=== Recount Player <%d> ===" % i_player_id

        if self.d_players.has_key(i_player_id):
            o_player = self.d_players[i_player_id]
            o_player.i_research = 0
            o_player.i_food     = 0

            for i_colony_id, o_colony in self.d_colonies.items():
                if o_colony.exists() and (o_colony.i_owner_id == i_player_id):
                    o_player.i_research += o_colony.i_research
                    o_player.i_food     += o_colony.compute_food_balance()

            if o_player.alive():
                self.recount_food_freighters(o_player)
                self.update_research(i_player_id, o_player.i_research_tech_id)
# ------------------------------------------------------------------------------
    def recount_players(self):
        print "=== Recount Players ==="
        for i_player_id in range(K_MAX_PLAYERS):
            self.recount_player(i_player_id)
# ------------------------------------------------------------------------------
    def get_stars_for_player(self, i_player_id):
        """ Returns a dictionary of all stars in galaxy.
        Stars that player doesn't know yet are listed as an Game_UnexploredStar class
        """
        d_stars  = {}
        o_player = self.d_players[i_player_id]
        for i_star_id, o_star in self.d_stars.items():
            if o_player.knows_star_id(i_star_id):
                d_stars[i_star_id] = o_star
            else:
                d_stars[i_star_id] = Game_Star.Game_UnexploredStar(i_star_id, o_star.i_x, o_star.i_y, o_star.i_size, o_star.i_pict_type, o_star.i_class)
        return d_stars
# ------------------------------------------------------------------------------
    def get_colonies_for_player(self, i_player_id):
        d_colonies = {}
        for i_colony_id, o_colony in self.d_colonies.items():
            if o_colony.i_owner_id == i_player_id:
                d_colonies[i_colony_id] = o_colony
            else:
                # JWL: Suspicious ... should not provide every enemy automatically (security issue)...
                d_colonies[i_colony_id] = Game_Colony.Game_EnemyColony(i_colony_id, o_colony.i_owner_id)
        return d_colonies
# ------------------------------------------------------------------------------
    def get_data_for_player(self, i_player_id):
        """
        this method returns data for one particular player and leave data for other players
        security reasons to prevent hacked clients to display data that player should not know
        """

         # TODO: implement status checking, to prevent asynchronous requests problems (client receives bad data)

        o_player = self.d_players[i_player_id]
        return {
            'rules':            self.d_rules,
            'me':               o_player,

            'galaxy':           self.d_galaxy,
            'players':          self.d_players,                             # insecure
            'stars':            self.get_stars_for_player(i_player_id),       # 100% secure?
            'stars_by_coords':  self.d_stars_by_coords,                    # insecure

            'governors':        self.list_player_governors(i_player_id),      # 50% secure?
            'officers':         self.list_player_officers(i_player_id),       # 50% secure?

            'planets':          self.d_planets,                             # insecure
            'colonies':         self.get_colonies_for_player(i_player_id),      # 100% secured ?
            'prototypes':       o_player.v_prototypes,                          # 100% secured?
            'ships':            self.d_ships,                               # insecure
        }
# ------------------------------------------------------------------------------
    def get_update_for_player(self, i_player_id):
        return self.d_players[i_player_id].serialize()
# ------------------------------------------------------------------------------
    def update_player(self, i_player_id, serial):
        self.d_players[i_player_id].unserialize(serial)
# ------------------------------------------------------------------------------
    def move_ships(self):
        """ Count new position af all moving or launching ships

            TODO: new start system exploration
            TODO: slowdown in nebulae
            TODO: usage of wormholes, jump gate and star gate
        """
        print("@ Game_Main::move_ships()")
        for ship_id, ship in self.d_ships.items():
            # if ship exists and is launching or already travelling
            if ship.exists() and ship.i_status in (1, 2):
                ship_x, ship_y = ship.get_coords()
                ship_speed = ship.get_travelling_speed()
                dest = ship.get_destination()
                dest_x, dest_y = self.stars[dest].get_coords()

                xx = dest_x - ship_x
                yy = dest_y - ship_y

                distance = math.sqrt(xx**2 + yy**2)

                parsecs = float(distance) / float(PARSEC_LENGTH)

                if parsecs > ship_speed:
                    # move towards ship's destination at known speed
                    parsec_x = float(xx) / parsecs
                    parsec_y = float(yy) / parsecs
                    ship_xx = int(ship_x + math.ceil(float(ship_speed) * parsec_x))
                    ship_yy = int(ship_y + math.ceil(float(ship_speed) * parsec_y))
                    ship.set_coords(ship_xx, ship_yy)
                    ship.set_travelling()
                else:
                    # ship has reached its destination
                    ship.set_coords(dest_x, dest_y)
                    ship.set_orbiting()
                    player = self.d_players[ship.i_owner_id]
                    if not player.knows_star_id(dest):
                        player.add_explored_star_id(dest)
# ------------------------------------------------------------------------------
    def colonies_production(self):
        """ Simple colony production
            Every turn, the first item from build queue is pulled and produced

            TODO: implement colony and outpost ships production
            TODO: implement regular ships production
            TODO: implement housing
            TODO: implement trade goods
            TODO: implement terraforming
            TODO: implement spies production
            TODO: implement real production cost

        """
        print("@ Game_Main::colonies_production()")
        for i_colony_id, o_colony in self.d_colonies.items():
            o_colony.raise_population(self.d_players)
            b_remove    = False
            b_recount   = False
            build_item  = o_colony.get_build_item()
            build_total = o_colony.update_industry_progress()
            if build_item:
                build_rule = self.d_rules['buildings'][build_item]
                build_cost = build_rule['cost']
                build_type = build_rule['type']
                print 'build_item (industry %d [total: %d]) ==> item %d' % (o_colony.i_industry, build_total, build_item)
                if build_total > build_cost:
                    if build_type == 'special':
                        if build_rule['name'] == 'Spy':   # JWL: TODO maybe separate special into spy/base?
                            self.d_players[o_colony.i_owner_id].i_spy_count += 1
                            b_remove = True
                        elif build_rule['name'] == 'Colony Base':
                            pass  # TODO
                            b_remove = True
                    elif build_type == 'trade':
                        pass  # TODO Confirm after BC calc finished ... No action - already used for BC calculation.
                    elif build_type == 'housing':
                        pass  # TODO Need to stop housing if colony fills.
                    elif build_type == 'xship':
                        # Transport, Outpost, Colony, Freighter
                        pass  # TODO
                        b_remove, b_recount = True, True # Might reduce Marine or Colonist count
                    elif build_type != 'building':   # 'capitol', 'proto', 'repeat'
                        print 'Ignoring invalid non-building present in queue. <%s> colony <%i>' % (build_type, i_colony_id)
                    else:
                        print 'Building completed.  Adding to colony and resetting colony industry_progress.'
                        o_colony.add_building(build_item)
                        print o_colony.v_building_ids
                        b_remove, b_recount = True, True

                    if b_remove:
# TODO JWL handle repeat -- don't remove if repeat still possible (note terraforming can repeat sometimes, but it runs out)
                        o_colony.remove_build_item(build_item)
                        o_colony.reset_industry_progress()
                    if b_recount:
                        o_colony.recount(self.d_rules, self.get_governor(i_colony_id), self.d_players)
            else:
                print 'No build_item (industry %d [total: %d]) ==> None' % (o_colony.i_industry, build_total)
# ------------------------------------------------------------------------------
    def recount(self):
        self.recount_heroes()
        self.recount_colonies()
        self.recount_players()
# ------------------------------------------------------------------------------
    def next_turn(self):
        print
        print "##"
        print "#    NEW TURN!"
        print "##"
        print
        sc = debug_timing(0, '')
        self.recount()
        sc = debug_timing(sc, 'game.recount')

        self.move_ships()
        sc = debug_timing(sc, 'game.move_ships')

        for i_player_id in range(K_MAX_PLAYERS):
            if self.d_players[i_player_id].alive():
                self.update_player_research(self.d_players[i_player_id])
                self.d_players[i_player_id].raise_bc()
        sc = debug_timing(sc, 'game.[player research/bc]')

        self.colonies_production()
        sc = debug_timing(sc, 'game.colonies_production')

        # Except in early game, some colony somewhere is likely to change its
        # population count each turn.  For simplicity, recount all players again.
        self.recount_players()
        sc = debug_timing(sc, 'game.recount_players (part 2)')
        self.d_galaxy['stardate'] += 1
# ------------------------------------------------------------------------------
    def count_players(self):
        c = 0
        for i_player_id in range(K_MAX_PLAYERS):
            if self.d_players[i_player_id].alive():
                c += 1
        return c
# ------------------------------------------------------------------------------
    def show_stars(self):
        s_txt = Data_CONST.get_text_list('STAR_SIZES')
        c_txt = Data_CONST.get_text_list('STAR_CLASSES')
        print
        print("+---------+-----------------+------------+------------+--------+-------+-------+-------+-------+-------+")
        print("| star_id | name            | coords     | class      | size   | obj 1 | obj 2 | obj 3 | obj 4 | obj 5 |")
        print("+---------+-----------------+------------+------------+--------+-------+-------+-------+-------+-------+")
        for i, s in self.d_stars.items():
            obj = s.v_object_ids
            print("| %7i | %15s | %4i, %4i | %10s | %6s | %5i | %5i | %5i | %5i | %5i |" % (i, s.s_name, s.i_x, s.i_y, c_txt[s.i_class], s_txt[s.i_size], obj[0], obj[1], obj[2], obj[3], obj[4]))
        print("+---------+-----------------+------------+------------+--------+-------+-------+-------+-------+-------+")
# ------------------------------------------------------------------------------
    def show_planets(self):
        si_txt = Data_CONST.get_text_list('PLANET_SIZES')
        ty_txt = Data_CONST.get_text_list('PLANET_TYPES')
        mi_txt = Data_CONST.get_text_list('PLANET_MINERALS')
        te_txt = Data_CONST.get_text_list('PLANET_TERRAINS')
        print
        print("+-----------+-----------------+----------+--------+---------------+------------+----------+------+---------+")
        print("| planet_id | star            | position | size   | type          | minerals   | terrain  | food | max pop |")
        print("+-----------+-----------------+----------+--------+---------------+------------+----------+------+---------+")
        for i, p in self.d_planets.items():
            print("| %9i | %15s | %8i | %6s | %13s | %10s | %8s | %4i | %7i |" % (i, self.d_stars[p.i_star_id].s_name, p.i_position, si_txt[p.i_size], ty_txt[p.i_type], mi_txt[p.i_minerals], te_txt[p.i_terrain], p.i_foodbase, p.i_max_population))
        print("+-----------+-----------------+----------+--------+---------------+------------+----------+------+---------+")
        print
# ------------------------------------------------------------------------------
    def show_players(self):
        print("NUMBER OF PLAYERS: %i" % self.count_players())
        print("+-----------+----------------------+----------------------+--------+--------+--------+----------------------+----------------------+---------+-----------+")
        print("| player_id | name                 | emperor              | food   | BC     | income | research:area        | :item                | :costs  | :progress |")
        print("+-----------+----------------------+----------------------+--------+--------+--------+----------------------+----------------------+---------+-----------+")
        for i, p in self.d_players.items():
            print("| %9i | %20s | %20s | %6i | %6i | %6i | %20s | %20s | %7i | %9i |" % (i, p.s_race_name, p.s_emperor_name, p.i_food, p.i_bc, p.i_bc_income, str(p.i_research_area), str(p.i_research_tech_id), p.i_research_cost, p.i_research_progress))
        print("+-----------+----------------------+----------------------+--------+--------+--------+----------------------+----------------------+---------+-----------+")
        print
# ------------------------------------------------------------------------------
    def show_colonies(self):
        print
        print("+-----------+-----------+-----------------+------------+------+----------+----------+-------+")
        print("| colony_id | planet_id | owner           | population | food | research | industry | BC    |")
        print("+-----------+-----------+-----------------+------------+------+----------+----------+-------+")
        for i, c in self.d_colonies.items():
            i_planet_id = c.i_planet_id
            i_owner_id  = c.i_owner_id
            if (i_planet_id < 0xFF) and (i_owner_id < 0xFF):
                o_owner = self.d_players[i_owner_id]
                print("| %9i | %9i | %15s | %10s | %4i | %8i | %8i | %5i |" % (i, i_planet_id, o_owner.s_race_name, c.i_population, c.i_food, c.i_research, c.i_industry, c.i_bc))
            else:
                print("| %9i | %9s | %15s | %10s | %4i | %8i | %8i | ----- |" % (i, "0xFF", "0xFF", c.i_population, c.i_food, c.i_research, c.i_industry))
        print("+-----------+-----------+-----------------+------------+------+----------+----------+-------+")
        print
# ------------------------------------------------------------------------------
    def show_ships(self):
        print
        print("+---------+------------------+-----------------+----------+------------+----------------------------+-------+-------+")
        print("| ship_id | name             | owner           | status   | coords     | destination                | speed | turns |")
        print("+---------+------------------+-----------------+----------+------------+----------------------------+-------+-------+")
        for i, s in self.d_ships.items():
            if s.exists():
                i_dest_id          = s.i_dest_star_id
                o_dest_star        = self.d_stars[i_dest_id]
                s_dest_name        = o_dest_star.s_name
                i_dest_x, i_dest_y = o_dest_star.get_coords()
                o_owner            = self.d_players[s.i_owner_id]
                print("| %7i | %16s | %15s | %8s | %4i, %4i | [%3i, %3i] %15s | %5i | %5i |" % (i, s.s_name, o_owner.s_race_name, s.get_status_text(), s.i_x, s.i_y, i_dest_x, i_dest_y, s_dest_name, s.i_travelling_speed, s.i_turns_left))
        print("+---------+------------------+-----------------+----------+------------+----------------------------+-------+-------+")
        print

        sp_txt = Data_CONST.get_text_list('SHIP_SPECIALS')

        for i, s in self.d_ships.items():
            d_design = s.d_design
            print("    === ship_id # %i ===" % i)
            for i_dev_id in d_design['special_devices']:
                txt = sp_txt[i_dev_id] if (i_dev_id < sp_txt.__len__()) else '<out-of-range>'
                print("        special device: %2i ... %s" % (i_dev_id, txt))
            print

# ------------------------------------------------------------------------------
# Test Code
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    GAME = Game_Main(None, 'C:\\Work\\jwl-orion2\\SAVE1.GAM')

