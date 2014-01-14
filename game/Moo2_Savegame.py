import os
import re
import struct
import Data_TECH
import Data_CONST
from Data_CONST import *   # for K_XXX constants

# ------------------------------------------------------------------------------
def to_bool_list(bytes_array):
    """
        returns a list of booleans from bit-values of given bytearray
    """
    ba = []
    index = 1
    for byte in bytes_array:
        for bit in range(7):
            if byte & 1 << bit:
                ba.append(index)
            index += 1
    return ba
# ==============================================================================
class Moo2_Savegame(object):
    """

    """
# ------------------------------------------------------------------------------
    def __init__(self, filename):
        """
        Loads the original MOO2 savegame
        """
        filesize    = os.path.getsize(filename)
        savefile    = open(filename, 'rb')
        self.file_data = savefile.read(filesize)
        savefile.close()
# ------------------------------------------------------------------------------
    def unpack_from(self, v_struct_table, v_data, i_offset = 0):
        ''' Wrapper for struct.unpack_from to apply a STRUCT_TABLE to name/size the fields. '''
        ##JWL-debug## print '------------- next unpack_from 0x%x --------------' % i_offset
        d_struct = {}
        i_rel_offset = 0
        for v_entry in v_struct_table:
            s_name, s_fmt = v_entry[0], v_entry[1]
            t_fields  = struct.unpack_from(s_fmt, v_data, i_offset+i_rel_offset)
            if s_name != '':
                if s_fmt.endswith('s'):
                    d_struct[s_name] = t_fields[0].split('\0')[0].rstrip()
                elif len(s_fmt) == 1:  # No preceding count.
                    d_struct[s_name] = t_fields[0]
                else:
                    d_struct[s_name] = list(t_fields)
                ##JWL-debug## print '   unpack_from: [0x%04x]   %30s = %s' % (i_rel_offset, s_name, d_struct[s_name])
            i_rel_offset += struct.calcsize(s_fmt)
        return d_struct
# ------------------------------------------------------------------------------
    def parse_game_opts(self):
        STRUCT_TABLE = [
            [ '',                                '4x'  ],
            [ 'name',                            '32s' ],  # is this 32???
            [ '',                                '10x' ],
            [ 'end_of_turn_summary',             'B'   ],
            [ 'end_of_turn_wait',                'B'   ],
            [ 'random_events',                   'B'   ],
            [ 'enemy_moves',                     'B'   ],
            [ 'expanding_help',                  'B'   ],
            [ 'auto_select_ships',               'B'   ],
            [ 'animations',                      'B'   ],
            [ 'auto_select_colony',              'B'   ],
            [ 'show_relocation_lines',           'B'   ],
            [ 'show_gnn_report',                 'B'   ],
            [ 'auto_delete_trade_good_housing',  'B'   ],
            [ 'auto_save_game',                  'B'   ],
            [ 'show_only_serious_turn_summary',  'B'   ],
            [ 'ship_initiative',                 'B'   ],
        ]
        d_game_opts         = self.unpack_from(STRUCT_TABLE, self.file_data)
        d_game_opts['name'] = d_game_opts['name'].lstrip(chr(0) + chr(1) + chr(2) + chr(3))
        return d_game_opts
# ------------------------------------------------------------------------------
    def parse_galaxy(self):
        STARDATE_DATA_OFFSET = 0x29
        STARDATE_STRUCT_TABLE = [
            [ 'stardate',       'H' ],
        ]
        d_stardate = self.unpack_from(STARDATE_STRUCT_TABLE, self.file_data, STARDATE_DATA_OFFSET)

        GALAXY_DATA_OFFSET = 0x31be4
        STRUCT_TABLE = [
            [ 'size_factor',    'B' ],
            [ '',               '4x' ],
            [ 'width',          'H' ],
            [ 'height',         'H' ],
        ]
        d_galaxy = self.unpack_from(STRUCT_TABLE, self.file_data, GALAXY_DATA_OFFSET)
        d_galaxy['stardate'] = d_stardate['stardate']
        return d_galaxy
# ------------------------------------------------------------------------------
    def parse_hero_skills(self, d_hero_struct):
        COMMON_SKILL_MAP = {
                1:           [ 'assassin',          2   ],  # bit  0 = Assassin
                2:           [ 'assassin',          3   ],  # bit  1 = Assassin*
                4:           [ 'commando',          2   ],  # bit  2 = Commando
                8:           [ 'commando',          3   ],  # bit  3 = Commando*
                16:          [ 'diplomat',          10  ],  # bit  4 = Diplomat
                32:          [ 'diplomat',          15  ],  # bit  5 = Diplomat*
                64:          [ 'famous',            60  ],  # bit  6 = Famous
                128:         [ 'famous',            90  ],  # bit  7 = Famous*
                256:         [ 'megawealth',        10  ],  # bit  8 = Megawealth
                512:         [ 'megawealth',        15  ],  # bit  9 = Megawealth*
                1024:        [ 'operations',        2   ],  # bit 10 = Operations
                2048:        [ 'operations',        3   ],  # bit 11 = Operations*
                4096:        [ 'researcher',        5   ],  # bit 12 = Researcher
                8192:        [ 'researcher',        7.5 ],  # bit 13 = Researcher*
                16384:       [ 'spy_master',        2   ],  # bit 14 = Spy Master
                32768:       [ 'spy_master',        3   ],  # bit 15 = Spy Master*
                65536:       [ 'telepath',          2   ],  # bit 16 = Telepath
                131072:      [ 'telepath',          3   ],  # bit 17 = Telepath*
                262144:      [ 'trader',            10  ],  # bit 18 = Trader
                524288:      [ 'trader',            15  ],  # bit 19 = Trader*
        }
        SPECIAL_SKILL_MAP = {
                1:           [ 'pollution_bonus',   10  ],  # bit  0 = Environmentalist
                2:           [ 'pollution_bonus',   15  ],  # bit  1 = Environmentalist*
                4:           [ 'food_bonus',        10  ],  # bit  2 = Farming Leader
                8:           [ 'food_bonus',        15  ],  # bit  3 = Farming Leader*
                16:          [ 'bc_bonus',          10  ],  # bit  4 = Financial Leader
                32:          [ 'bc_bonus',          15  ],  # bit  5 = Financial Leader*
                64:          [ 'instructor',        0.7 ],  # bit  6 = Instructor
                128:         [ 'instructor',        1.1 ],  # bit  7 = Instructor*
                256:         [ 'industry_bonus',    10  ],  # bit  8 = Labor Leader
                512:         [ 'industry_bonus',    15  ],  # bit  9 = Labor Leader*
                1024:        [ 'medicine',          10  ],  # bit 10 = Medicine
                2048:        [ 'medicine',          15  ],  # bit 11 = Medicine*
                4096:        [ 'research_bonus',    10  ],  # bit 12 = Science Leader
                8192:        [ 'research_bonus',    15  ],  # bit 13 = Science Leader*
                16384:       [ 'morale_bonus',      0   ],  # bit 14 = Spiritual Leader
                32768:       [ 'morale_bonus',      7.5 ],  # bit 15 = Spiritual Leader*
                65536:       [ 'tactics',           6   ],  # bit 16 = Tactics
                131072:      [ 'tactics',           9   ],  # bit 17 = Tactics*
        }

        d_skills = {}
        i_common_skills = d_hero_struct['common_skills']
        for k, v in COMMON_SKILL_MAP.iteritems():
            if i_common_skills & k:
                d_skills[v[0]] = v[1]

        if d_hero_struct['type'] == 1:
            i_special_skills = d_hero_struct['special_skills']
            for k, v in SPECIAL_SKILL_MAP.iteritems():
                if i_special_skills & k:
                    d_skills[v[0]] = v[1]

        return d_skills
# ------------------------------------------------------------------------------
    def parse_heroes(self):
        HEROES_DATA_OFFSET  = 0x19a9b
        HERO_RECORD_SIZE    = 0x3b         # = 59
        STRUCT_TABLE = [
            [ 'name',             '15s' ],
            [ 'title',            '20s' ],
            [ 'type',             'B'   ],
            [ 'experience',       'I'   ],
            [ '',                 '6x'  ],
            [ 'tech1',            'B'   ],
            [ 'tech2',            'B'   ],
            [ 'tech3',            'B'   ],
            [ 'picture',          'B'   ],
            [ 'skill_value',      'H'   ],
            [ 'level',            'B'   ],
            [ 'location',         'H'   ],
            [ 'eta',              'B'   ],
            [ 'level_up',         'B'   ],
            [ 'status',           'B'   ],
            [ 'player',           'B'   ],
            [ 'common_skills',    'L'   ],
            [ 'special_skills',   'L'   ],
        ]
        d_heroes     = {}
        i_num_heroes = 67
        for i_hero_id in range(i_num_heroes):
            i_offset                      = HEROES_DATA_OFFSET + (HERO_RECORD_SIZE * i_hero_id)
            d_heroes[i_hero_id]           = self.unpack_from(STRUCT_TABLE, self.file_data, i_offset)
            d_heroes[i_hero_id]['id']     = i_hero_id
            d_heroes[i_hero_id]['skills'] = self.parse_hero_skills(d_heroes[i_hero_id])
        return d_heroes
# ------------------------------------------------------------------------------
    def parse_known_techs(self, offset):
        v_known_techs = []
        for i in range(203):               # original moo2 mas 203 usable technologies
            i_tech_status = struct.unpack_from('B', self.file_data, offset + i)[0]
            if i_tech_status == Data_TECH.TECH_KNOWN:
                v_known_techs.append(i + 1)
        return v_known_techs
# ------------------------------------------------------------------------------
    def add_npc_player(self, STRUCT_TABLE, d_players, i_player_id, s_emperor_name, s_race_name):
        ''' Manufacture a basic NPC player for special races like Antarans, etc. '''
        o_player = {}
        for v_field in STRUCT_TABLE:
            s_name, s_type_abbr = v_field[0], v_field[1]
            if s_type_abbr.endswith('s') or s_type_abbr.endswith('c'):
                o_player[s_name] = ''
            elif s_name != '':
                o_player[s_name] = 0
        o_player['emperor_name']   = s_emperor_name
        o_player['race_name']      = s_race_name
        o_player['known_techs']    = []
        o_player['prototypes']     = []
        o_player['tributes']       = []
        d_players[i_player_id]     = o_player
# ------------------------------------------------------------------------------
    def parse_players(self):
        PLAYERS_DATA_OFFSET = 0x01aa0f
        PLAYER_RECORD_SIZE  = 3753
        STRUCT_TABLE = [
            [ 'emperor_name',              '20s'   ],
            [ 'race_name',                 '16s'   ],
            [ 'picture',                   'B'     ],
            [ 'color',                     'B'     ],
            [ 'personality',               'B'     ],
            [ 'objective',                 'B'     ],
            [ 'tax_rate',                  'B'     ],
            [ 'bc',                        'I'     ],
            [ 'total_frighters',           'H'     ],
            [ 'used_frighters',            'H'     ],
            [ 'total_command',             'H'     ],
            [ '',                          '112x'  ],
            [ 'industry',                  'H'     ],
            [ 'research',                  'H'     ],
            [ 'food',                      'H'     ],
            [ 'bc_income',                 'h'     ],
            [ '',                          '313x'  ] , # 0x1ea - 0xb1
            [ 'research_progress',         'H'     ],
            [ '',                          '310x'  ],  # 0x320 - 0x1ea
            [ 'research_area',             'B'     ],
            [ 'research_tech_id',          'B'     ],
            [ '',                          '1405x' ], # 0x89E - 0x321
            [ 'race_goverment',            'B'     ],
            [ 'race_population',           'b'     ],
            [ 'race_farming',              'b'     ],
            [ 'race_industry',             'b'     ],
            [ 'race_science',              'b'     ],
            [ 'race_money',                'b'     ],
            [ 'race_ship_defense',         'b'     ],
            [ 'race_ship_attack',          'b'     ],
            [ 'race_ground_combat',        'b'     ],
            [ 'race_spying',               'b'     ],
            [ 'race_low_g',                'B'     ],
            [ 'race_high_g',               'B'     ],
            [ 'race_aquatic',              'B'     ],
            [ 'race_subterranean',         'B'     ],
            [ 'race_large_home_world',     'B'     ],
            [ 'race_rich_home_world',      'B'     ],
              # where is poor_home_world?
            [ 'race_artifacts_home_world', 'B'     ],
            [ 'race_cybernetic',           'B'     ],
            [ 'race_lithovore',            'B'     ],
            [ 'race_repulsive',            'B'     ],
            [ 'race_charismatic',          'B'     ],
            [ 'race_uncreative',           'B'     ],
            [ 'race_creative',             'B'     ],
            [ 'race_tolerant',             'B'     ],
            [ 'race_fantastic_traders',    'B'     ],
            [ 'race_telepathic',           'B'     ],
            [ 'race_lucky',                'B'     ],
            [ 'race_omniscience',          'B'     ],
            [ 'race_stealthy_ships',       'B'     ],
            [ 'race_trans_dimensional',    'B'     ],
            [ 'race_warlord',              'B'     ],
        ]
        d_players     = {}
        i_num_players = 8
        for i_player_id in range(i_num_players):
            i_offset                   = PLAYERS_DATA_OFFSET + (PLAYER_RECORD_SIZE * i_player_id)
            o_player                   = self.unpack_from(STRUCT_TABLE, self.file_data, i_offset)
            o_player['known_techs']    = self.parse_known_techs(i_offset + 0x117)
            o_player['prototypes']     = []
            o_player['tributes']       = []

            i_num_prototypes = 6
            for ii in range(i_num_prototypes):
                i_offset2 = i_offset + 0x325 + (ii * 0x63)
                o_player['prototypes'].append(self.parse_ship_design(i_offset2))

            i_num_tributes = 7
            for ii in range(i_num_tributes):
                i_offset2 = i_offset + 0x649 + (ii)
                o_player['tributes'].append(struct.unpack_from('B', self.file_data, i_offset2)[0])

            d_players[i_player_id] = o_player

        self.add_npc_player(STRUCT_TABLE, d_players, K_RACE_ANTARAN,  'Antarans',      'Antaran')
        self.add_npc_player(STRUCT_TABLE, d_players, K_RACE_ORION,    'Orion',         'Loknar')
        self.add_npc_player(STRUCT_TABLE, d_players, K_RACE_AMOEBA,   'Space Amoeba',  'Amoeba')
        self.add_npc_player(STRUCT_TABLE, d_players, K_RACE_CRYSTAL,  'Space Crystal', 'Crystal')
        self.add_npc_player(STRUCT_TABLE, d_players, K_RACE_DRAGON,   'Space Dragon',  'Dragon')
        self.add_npc_player(STRUCT_TABLE, d_players, K_RACE_EEL,      'Space Eel',     'Eel')
        self.add_npc_player(STRUCT_TABLE, d_players, K_RACE_HYDRA,    'Space Hydra',   'Hydra')
        return d_players
# ------------------------------------------------------------------------------
    def parse_stars(self):
        #       http://www.spheriumnorth.com/orion-forum/nfphpbb/viewtopic.php?p=149
        SOLAR_SYSTEMS_COUNT_OFFSET  = 0x17ad1
        SOLAR_SYSTEMS_DATA_OFFSET   = 0x17ad3
        SOLAR_SYSTEM_RECORD_SIZE    = 0x71
        STRUCT_TABLE = [
                [ 'name',                       '15s' ],
                [ 'x',                          'H'   ],
                [ 'y',                          'H'   ],
                [ 'size',                       'B'   ],
                [ 'owner',                      'B'   ],  # primary owner
                [ 'pict_type',                  'B'   ],
                [ 'class',                      'B'   ],
                [ 'last_planet_selected',       '8B'  ],
                [ '',                           '9x'  ],
                [ 'special',                    'B'   ],
                [ 'wormhole',                   'B'   ],
                [ 'blockaded_players',          'B'   ],
                [ 'blockaded_by_bitmask',       '8B'  ],
                [ 'visited',                    'B'   ],  # bitmask as booleans for each player
                [ 'just_visited_bitmask',       'B'   ],  # players bitmask to track first visit of this star -> user should get report
                [ 'ignore_colony_ship_bitmask', 'B'   ],  # players bitmask to track if player chose to not use a colony ship, cleared on every new colony ship here?
                [ 'ignore_combat_bitmask',      'B'   ],  # players bitmask to track if player chose to ignore combat ships = perform blockade only do not fight here?
                [ 'colonize_player',            'B'   ],  # 0..7 or -1
                [ 'colonies_bitmask',           'B'   ],  # has colony / players bitmask / redundant info?
                [ 'interdictors_bitmask',       'B'   ],  # has warp interdictor / players bitmask
                [ 'next_wfi_in_list',           'B'   ],  # bookeeping ???
                [ 'tachyon_com_bitmask',        'B'   ],  # has tachyon communicator / players bitmask
                [ 'subspace_com_bitmask',       'B'   ],  # has subspace communicator / players bitmask
                [ 'stargates_bitmask',          'B'   ],  # has stargate / players bitmask
                [ 'jumpgates_bitmask',          'B'   ],  # has jumpgate / players bitmask
                [ 'artemis_bitmask',            'B'   ],  # has artemis net players bitmask
                [ 'portals_bitmask',            'B'   ],  # has dimension portal / players bitmask
                [ 'stagepoint_bitmask',         'B'   ],  # bitvector tells whether star is stagepoint for each AI
                [ 'players_officers',           '8B'  ],
                [ 'object_ids',                 '5H'  ],
                [ '',                           '20x' ],
                [ 'surrender_to',               '8B'  ],
                [ 'is_in_nebula',               'B'   ],
        ]
        d_stars     = {}
        i_num_stars = struct.unpack_from('B', self.file_data, SOLAR_SYSTEMS_COUNT_OFFSET)[0]
        for i_star_id in range(i_num_stars):
            i_offset                    = SOLAR_SYSTEMS_DATA_OFFSET + (SOLAR_SYSTEM_RECORD_SIZE * i_star_id)
            o_star                      = self.unpack_from(STRUCT_TABLE, self.file_data, i_offset)
            #o_star['blockaded_players'] = bitmask_to_player_id_list(o_star['blockaded_players'])
            o_star['star_id']           = i_star_id
            o_star['is_in_nebula']      = (o_star['is_in_nebula'] == 1)
            d_stars[i_star_id]          = o_star
        return d_stars
# ------------------------------------------------------------------------------
    def parse_planets(self):
        PLANETS_COUNT_OFFSET    = 0x162e7
        PLANETS_DATA_OFFSET     = 0x162e9
        PLANET_RECORD_SIZE      = 0x11
        STRUCT_TABLE = [
                [ 'colony_id',        'H', 0x00 ],   # 0xffff = no colony here
                [ 'star_id',          'B', 0x02 ],
                [ 'position',         'B', 0x03 ],
                [ 'type',             'B', 0x04 ],
                [ 'size',             'B', 0x05 ],
                [ 'gravity',          'B', 0x06 ],
                [ 'group',            'B', 0x07 ],   # not used ?
                [ 'terrain',          'B', 0x08 ],
                [ 'picture',          'B', 0x09 ],   # Background image on colony screen (0-5=image in planets.lbx)
                [ 'minerals',         'B', 0x0a ],
                [ 'foodbase',         'B', 0x0b ],
                [ 'terraformations',  'B', 0x0c ],
                [ 'max_farms',        'B', 0x0d ],   # unknown (Initial value is based on Planet Size but changes if colonized), 2=tiny, 4=small, 5=med, 7=large, A=huge
                [ 'max_population',   'B', 0x0e ],
                [ 'special',          'B', 0x0f ],
                [ 'flags',            'B', 0x10 ],   # (bit 2 = Soil Enrichment)
        ]
        d_planets     = {}
        i_num_planets = struct.unpack_from('H', self.file_data, PLANETS_COUNT_OFFSET)[0]
        for i_planet_id in range(i_num_planets):
            i_offset               = PLANETS_DATA_OFFSET + (PLANET_RECORD_SIZE * i_planet_id)
            d_planets[i_planet_id] = self.unpack_from(STRUCT_TABLE, self.file_data, i_offset)
        return d_planets
# ------------------------------------------------------------------------------
    def parse_colony_pop(self, data, i_rec_offset, i_population):
        d_colony_pop = {K_FARMER: [], K_WORKER: [], K_SCIENTIST: []}
        STRUCT_TABLE = [ ['a','B'], ['b','B'],['c','B'],['d','B'] ]
        for i in range(i_population):
            i_offset          = i_rec_offset + 0x0C + (4 * i)
            type_1, type_2    = struct.unpack_from('BB', data, i_offset)
            i_type            = (type_1 & 0x80) + (type_2 & 3)
            d_pop_rec         = self.unpack_from(STRUCT_TABLE, data, i_offset)
            d_pop_rec['r1']   = (d_pop_rec['a'] & 0x70) >> 4
            d_pop_rec['race'] = (d_pop_rec['a'] & 0x07)
            d_colony_pop[i_type].append(d_pop_rec)
        return d_colony_pop
# ------------------------------------------------------------------------------
    def parse_colonies(self):
        COLONIES_DATA_OFFSET = 0x0025d
        COLONY_RECORD_SIZE   = 361
        STRUCT_TABLE = [
                [ 'owner_id',               'B'    ],
                [ 'allocated_to',           'B'    ],
                [ 'planet_id',              'B'    ],
                [ '',                       '1x'   ],
                [ 'officer_id',             'H'    ],
                [ 'is_outpost',             'B'    ],
                [ 'morale',                 'B'    ],
                [ 'pollution',              'H'    ],
                [ 'population',             'B'    ],
                [ 'assignment',             'B'    ],
                [ '',                       '168x' ], # contains the info for parse_colony_pop()
                [ 'pop_raised',             '10H'  ], # 8 races, androids, natives
                [ 'pop_grow',               '10H'  ], # 8 races, androids, natives
                [ 'num_turns_existed',      'B'    ], # bookkeeping
                [ 'food2_per_farmer',       'B'    ], # Food per farmer in half-units of food
                [ 'industry_per_worker',    'B'    ],
                [ 'research_per_scientist', 'B'    ],
                [ 'max_farms',              'B'    ],
                [ 'max_population',         'B'    ], # not used?
                [ 'climate',                'B'    ],
                [ 'ground_strength',        'H'    ], # calculated for ai
                [ 'space_strength',         'H'    ], # calculated for ai
                [ 'food',                   'H'    ], # total food = food - population
                [ 'industry',               'H'    ],
                [ 'research',               'H'    ],
                [ '',                       '69x'  ], # 0x130 - 0x0EB
                [ 'num_marines',            'B'    ],
                [ 'num_armors',             'B'    ],
        ]
        d_colonies     = {}
        i_num_colonies = struct.unpack_from('H', self.file_data, 0x25b)[0]
        for i_colony_id in range(i_num_colonies):
            i_offset                 = COLONIES_DATA_OFFSET + (COLONY_RECORD_SIZE * i_colony_id)
            o_colony                 = self.unpack_from(STRUCT_TABLE, self.file_data, i_offset)
            o_colony['colony_id']    = i_colony_id
            o_colony['morale']      *= 5 # Morale value is stored as divided by 5
            o_colony['colonists']    = self.parse_colony_pop(self.file_data, i_offset, o_colony['population'])
            o_colony['build_queue']  = []
            o_colony['building_ids'] = []

            for i_queue_id in range(0, K_MAX_BUILD_QUEUE-1):
                i_production_id    = struct.unpack_from('B', self.file_data, 0x115 + i_queue_id*2)[0]
                i_production_flags = struct.unpack_from('B', self.file_data, 0x115 + i_queue_id*2 + 1)[0]
                if i_production_id < 0xFF:
                    o_colony['build_queue'].append(i_production_id)
                    # JWL: TODO What do 'flags' mean?  Ignored for now...

            for i_building_id in range(1, 49):
                i_building_state = struct.unpack_from('B', self.file_data, 0x136 + i_building_id)[0]
                if i_building_state != 0:
                    o_colony['building_ids'].append(i_building_id)

            d_colonies[i_colony_id]  = o_colony
        return d_colonies
# ------------------------------------------------------------------------------
    def parse_ship_design(self, i_offset):
        WPN_STRUCT_TABLE = [
                [ 'weapon',        'B' ],
                [ 'count',         'B' ],
                [ 'current_count', 'B' ],
                [ 'arc',           'B' ],
                [ 'beam_mods',     'B' ],
                [ 'missile_mods',  'B' ],
                [ 'ammo',          'B' ],
        ]
        STRUCT_TABLE = [
                [ 'name',            '16s' ],
                [ 'size',            'B'   ],
                [ 'type',            'B'   ],
                [ 'shield',          'B'   ],
                [ 'drive',           'B'   ],
                [ 'speed',           'B'   ],
                [ 'computer',        'B'   ],
                [ 'armor',           'B'   ],
                [ 'special_devices', '6B'  ], # char  special_device_flags[(MAX_SPECIALS+7)/8];
                [ 'picture',         'B'   ],
                [ 'builder',         'B'   ], # or previous owner?
                [ 'cost',            'H'   ],
                [ 'combat_speed',    'B'   ],
                [ 'build_date',      'H'   ],
        ]
        v_weapons = []
        for i in range(K_MAX_WEAPONS_PER_SHIP):
            i_offset2 = i_offset + 0x1C + (8 * i)
            d_weapon  = self.unpack_from(WPN_STRUCT_TABLE, self.file_data, i_offset2)
            if d_weapon['weapon'] > 0:
                v_weapons.append(d_weapon)

        d_design                    = self.unpack_from(STRUCT_TABLE, self.file_data, i_offset)
        d_design['weapons']         = v_weapons
        d_design['special_devices'] = to_bool_list(bytearray(d_design['special_devices']))
        return d_design
# ------------------------------------------------------------------------------
    def parse_ships(self):
        SAVE_SHIP_COUNT_OFFSET = 0x21f56
        SAVE_SHIPS_OFFSET      = 0x21f58
        SAVE_SHIP_RECORD_SIZE  = 0x81        # = 129
        STRUCT_TABLE = [
                [ '',                       '99x' ],
                [ 'owner_id',               'B'   ],
                [ 'status',                 'B'   ],
                [ 'dest_star_id',           'H'   ],
                [ 'x',                      'H'   ],
                [ 'y',                      'H'   ],
                [ 'group_has_navigator',    'B'   ],
                [ 'travelling_speed',       'B'   ], # possibly less than ftl_type
                [ 'turns_left',             'B'   ], # until arrival
                [ 'shield_damage_percent',  'B'   ],
                [ 'drive_damage_percent',   'B'   ],
                [ 'computer_damage',        'B'   ],
                [ 'crew_quality',           'B'   ],
                [ 'crew_experience',        'H'   ],
                [ 'officer_id',             'H'   ],
                [ 'special_device_damage',  '6B'  ], # bit flag array
                [ 'armor_damage',           'H'   ],
                [ 'structural_damage',      'H'   ],
                [ 'mission',                'B'   ], # used for AI
                [ 'just_built',             'B'   ],
        ]
        d_ships     = {}
        i_num_ships = struct.unpack_from('H', self.file_data, SAVE_SHIP_COUNT_OFFSET)[0]
        for i_ship_id in range(i_num_ships):
            i_offset                = SAVE_SHIPS_OFFSET + (SAVE_SHIP_RECORD_SIZE * i_ship_id)
            o_ship                  = self.unpack_from(STRUCT_TABLE, self.file_data, i_offset)
            o_ship['dest_star_id'] %= 500
            o_ship['design']        = self.parse_ship_design(i_offset)
            o_ship['name']          = o_ship['design']['name']
            d_ships[i_ship_id]      = o_ship
        return d_ships

# ------------------------------------------------------------------------------
# Test Code
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    moo2 = Moo2_Savegame('C:\\Work\\jwl-orion2\\SAVE1.GAM')
    #a1 = moo2.parse_game_opts()
    #a2 = moo2.parse_galaxy()
    #a4 = moo2.parse_heroes()
    #a5 = moo2.parse_players()
    a6 = moo2.parse_stars()
    #a7 = moo2.parse_planets()
    #a8 = moo2.parse_ships()
    #a9 = moo2.parse_colonies()
