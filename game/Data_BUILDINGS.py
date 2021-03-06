# JWL: These buildings are so specialized that direct checks for them are currently used...
B_CLONING_CENTER    = 10
B_GRAVITY_GENERATOR = 25
B_REPEAT            = 249
B_NONE              = 255
B_HOUSING           = 253
B_TRADE_GOODS       = 254

# ------------------------------------------------------------------------------
BUILDINGS = {

# Missing Android Farmer, Worker, Scientist @ cost = 50
      0: {
        'name':                     '',
        'tech':                     255,
      },

      1: {
        'name':                     "Alien Control Center",
        'tech':                     5,
        'cost':                     111,
        'maint':                    -1,
      },

      2: {
        'name':                     "Armor Barracks",
        'tech':                     14,
        'cost':                     150,
        'maint':                    -2,
        'morale_bonus_gov':         [20, 20, 20, 20, 0, 0, 0], # percent
      },

      3: {
        'name':                     "Artemis System Net",
        'tech':                     15,
        'cost':                     1000,
        'maint':                    -5,
      },

      4: {
        'name':                     "Astro University",
        'tech':                     18,
        'cost':                     200,
        'maint':                    -4,
        'food_per_farmer':          +1,
        'industry_per_worker':      +1,
        'research_per_scientist':   +1,
      },

      5: {
        'name':                     "Atmosphere Renewer",
        'tech':                     19,
        'cost':                     150,
        'maint':                    -3,
        'industry_pollution_ratio': 0.50,
      },

      6: {
        'name':                     "Autolab",
        'tech':                     21,
        'cost':                     200,
        'maint':                    -3,
        'research_prod':            +30,
      },

      7: {
        'name':                     "Automated Factory",
        'tech':                     22,
        'cost':                     60,
        'maint':                    -1,
        'industry_per_worker':      +1,
        'industry_per_colony':      +5,
      },

      8: {
        'name':                     "Battlestation",
        'tech':                     27,
        'cost':                     600,
        'maint':                    -3,
        'replaces':                 [40],
      },

      9: {
        'name':                     "Capitol",
        'tech':                     32,
        'type':                     "capitol"
      },

     10: {
        'name':                     "Cloning Center",
        'tech':                     39,
        'cost':                     100,
        'maint':                    -2,
      },

     11: {
        'name':                     "Colony Base",
        'tech':                     40,
        'cost':                     200,
        'maint':                    -1,
        'type':                     "special"
      },

     12: {
        'name':                     "Deep Core Mine",
        'tech':                     49,
        'cost':                     250,
        'maint':                    -3,
        'industry_per_worker':      +3,
        'industry_per_colony':      +15,
      },

     13: {
        'name':                     "Core Waste Dump",
        'tech':                     50,
        'cost':                     200,
        'maint':                    -8,
        'replaces':                 [5, 32],
        'industry_pollution_ratio': 0.0
      },

     14: {
        'name':                     "Dimensional Portal",
        'cost':                     500,
        'maint':                    -2,
        'tech':                     52,
      },

     15: {
        'name':                     "Biospheres",
        'cost':                     60,
        'maint':                    -1,
        'tech':                     61,
        'pop_bonus':                +2,
      },

     16: {
        'name':                     "Food Replicators",
        'cost':                     200,
        'maint':                    -10,
        'tech':                     68,
      },

     17: {
        'name':                     "Gaia Transformation",
        'cost':                     500,
        'tech':                     74,
      },

     18: {
        'name':                     "Currency Exchange",
        'cost':                     111,
        'maint':                    -1,
        'tech':                     75,
      },

     19: {
        'name':                     "Galactic Cybernet",
        'cost':                     250,
        'maint':                    -3,
        'tech':                     76,
        'research_prod':           +15,
      },

     20: {
        'name':                     "Holo Simulator",
        'cost':                     120,
        'maint':                    -1,
        'tech':                     86,
        'morale_bonus':             20, # percent
      },

     21: {
        'name':                     "Hydroponic Farm",
        'cost':                     60,
        'maint':                    -2,
        'tech':                     87,
        'food_per_colony':          +2,
      },

     22: {
        'name':                     "Marine Barracks",
        'tech':                     103,
        'cost':                     60,
        'maint':                    -1,
        'morale_bonus_gov':         [20, 20, 20, 20, 0, 0, 0], # percent
      },

     23: {
        'name':                     "Barrier Shield",
        'tech':                     129,
        'cost':                     420,
        'maint':                    -5,
        'replaces':                 [28, 24],
      },

     24: {
        'name':                     "Flux Shield",
        'tech':                     130,
        'cost':                     120,
        'maint':                    -3,
        'replaces':                 [28]
      },

     25: {
        'name':                     "Gravity Generator",
        'tech':                     131,
        'cost':                     120,
        'maint':                    -2,
      },

     26: {
        'name':                     "Missile Base",
        'tech':                     132,
        'cost':                     120,
        'maint':                    -2,
      },

     27: {
        'name':                     "Ground Batteries",
        'tech':                     133,
        'cost':                     200,
        'maint':                    -2,
      },

     28: {
        'name':                     "Radiation Shield",
        'tech':                     134,
        'cost':                     80,
        'maint':                    -1,
      },

     29: {
        'name':                     "Stock Exchange",
        'tech':                     135,
        'cost':                     150,
        'maint':                    -2,
      },

     30: {
        'name':                     "Supercomputer",
        'tech':                     136,
        'cost':                     150,
        'maint':                    -2,
        'scientist_bonus':          +2,
        'research_prod':            +10,
      },

     31: {
        'name':                     "Pleasure Dome",
        'tech':                     141,
        'cost':                     250,
        'maint':                    -3,
        'morale_bonus':             30, # percent
      },

     32: {
        'name':                     "Pollution Processor",
        'tech':                     142,
        'cost':                     80,
        'maint':                    -1,
        'industry_pollution_ratio': 0.50,
      },

     33: {
        'name':                     "Recyclotron",
        'tech':                     152,
        'cost':                     200,
        'maint':                    -3,
        'industry_per_colonist':    +1
      },

     34: {
        'name':                     "Robotic Factory",
        'tech':                     154,
        'cost':                     200,
        'maint':                    -3,
        'industry_by_minerals':     [5, 8, 10, 15, 20],
      },

     35: {
        'name':                     "Research Lab",
        'tech':                     155,
        'cost':                     60,
        'maint':                    -1,
        'scientist_bonus':          +1,
        'research_prod':            +5,
      },

     36: {
        'name':                     "Robo Miner Plant",
        'tech':                     156,
        'cost':                     150,
        'maint':                    -2,
        'industry_per_worker':      +2,
        'industry_per_colony':      +10,
      },

     37: {
        'name':                     "Soil Enrichment",
        'tech':                     162,
        'cost':                     120,
        'maint':                    0,
      },

     38: {
        'name':                     "Space Academy",
        'tech':                     163,
        'cost':                     100,
        'maint':                    -2,
      },

     39: {
        'name':                     "Spaceport",
        'tech':                     164,
        'cost':                     80,
        'maint':                    -1,
      },

     40: {
        'name':                     "Star Base",
        'tech':                     168,
        'cost':                     400,
        'maint':                    -2,
      },

     41: {
        'name':                     "Star Fortress",
        'tech':                     169,
        'cost':                     1500,
        'maint':                    -4,
        'replaces':                 [40, 8],
      },

     42: {
        'name':                     "Stellar Converter",
        'tech':                     174,
        'cost':                     1000,
        'maint':                    -6,
      },

     43: {
        'name':                     "Subterranean Farms",
        'tech':                     178,
        'cost':                     150,
        'maint':                    -4,
        'food_per_colony':          +4,
      },

     44: {
        'name':                     "Terraforming",
        'tech':                     183,
        'cost':                     250,
      },

     45: {
        'name':                     "Warp Interdictor",
        'tech':                     197,
        'cost':                     300,
        'maint':                    -3,
      },

     46: {
        'name':                     "Weather Controller",
        'tech':                     198,
        'cost':                     200,
        'maint':                    -3,
        'food_per_farmer':          +2,
      },

     47: {
        'name':                     "Fighter Garrison",
        'tech':                     67,
        'cost':                     150,
        'maint':                    -2,
      },

     48: {
        'name':                     "Artificial Planet",
        'tech':                     16,
        'cost':                     1111,
      },

    90: {
        'name':                     "? BUILDING 90 ?",
        'tech':                     255
      },

    96: {
        'name':                     "? BUILDING 96 ?",
        'tech':                     255
      },

    105: {
        'name':                     "? BUILDING 105 ?",
        'tech':                     255
      },

    106: {
        'name':                     "? BUILDING 106 ?",
        'tech':                     255
      },

    107: {
        'name':                     "? BUILDING 107 ?",
        'tech':                     255
      },

    108: {
        'name':                     "? BUILDING 108 ?",
        'tech':                     255
      },

    112: {
        'name':                     "? BUILDING 112 ?",
        'tech':                     255
      },

    116: {
        'name':                     "? BUILDING 116 ?",
        'tech':                     255
      },

    117: {
        'name':                     "? BUILDING 117 ?",
        'tech':                     255
      },

    123: {
        'name':                     "? BUILDING 123 ?",
        'tech':                     255
      },

    124: {
        'name':                     "? BUILDING 124 ?",
        'tech':                     255
      },

    128: {
        'name':                     "? BUILDING 128 ?",
        'tech':                     255
      },

    141: {
        'name':                     "Transport Ship",
        'tech':                     189,
        'cost':                     100,
        'maint':                    -1,
        'type':                     "xship"
      },

    142: {
        'name':                     "Outpost Ship",
        'tech':                     109,
        'cost':                     100,
        'type':                     "xship"
      },

    143: {
        'name':                     "Colony Ship",
        'tech':                     41,
        'cost':                     500,
        'type':                     "xship"
      },

    144: {
        'name':                     "ship design # 4",
        'type':                     "proto"
      },

    145: {
        'name':                     "ship design # 3",
        'type':                     "proto"
      },

    146: {
        'name':                     "? production_id 146 ?",
        'tech':                     255
      },

    147: {
        'name':                     "ship design # 2",
        'type':                     "proto"
      },

    148: {
        'name':                     "ship design # 1",
        'type':                     "proto"
      },

    149: {
        'name':                     "? production_id 149 ?",
        'tech':                     255
      },

    150: {
        'name':                     "ship design # 0",
        'type':                     "proto"
      },

    151: {
        'name':                     "? production_id 151 ?",
        'tech':                     255
      },

    152: {
        'name':                     "? production_id 152 ?",
        'tech':                     255
      },

    153: {
        'name':                     "ship design # X",
        'type':                     "proto"
      },

    214: {
        'name':                     "Freighter Fleet",
        'tech':                     69,
        'cost':                     50,
        'maint':                    -1,
        'type':                     "xship"
      },

    241: {
        'name':                     "? BUILDING 241 ?",
        'tech':                     255
      },

    246: {
        'name':                     "Spy",
        'tech':                     166,
        'cost':                     100,
        'maint':                    -1,
        'type':                     "special"
      },

    249: {
        'name':                     "^ Repeat ^",
        'type':                    "repeat"
      },

    253: {
        'name':                     "Housing",
        'type':                     "housing"
      },

    254: {
        'name':                     "Trade Goods",
        'type':                     "trade"
      },
}

# ------------------------------------------------------------------------------
def apply_building_key_default(building_id, key, value):
    if not BUILDINGS[building_id].has_key(key):
        BUILDINGS[building_id][key] = value
# ------------------------------------------------------------------------------
def regularize_building_keys():
    ''' Makes sure that the base key set is present to avoid a lot of extraneous has_key() calls. '''
    for building_id in BUILDINGS.keys():
        apply_building_key_default(building_id, 'type',                     'building')
        apply_building_key_default(building_id, 'tech',                     0)
        apply_building_key_default(building_id, 'cost',                     0)
        apply_building_key_default(building_id, 'maint',                    0)
        apply_building_key_default(building_id, 'pop_bonus',                0)
        apply_building_key_default(building_id, 'morale_bonus_gov',         [0, 0, 0, 0, 0, 0, 0])
        apply_building_key_default(building_id, 'morale_bonus',             0)
        apply_building_key_default(building_id, 'food_per_farmer',          0)
        apply_building_key_default(building_id, 'food_per_colony',          0)
        apply_building_key_default(building_id, 'industry_per_worker',      0)
        apply_building_key_default(building_id, 'industry_per_colony',      0)
        apply_building_key_default(building_id, 'industry_per_colonist',    0)
        apply_building_key_default(building_id, 'industry_by_minerals',     [0, 0, 0, 0, 0])
        apply_building_key_default(building_id, 'industry_pollution_ratio', 1.0)
        apply_building_key_default(building_id, 'research_per_scientist',   0)
        apply_building_key_default(building_id, 'research_per_colony',      0)
        apply_building_key_default(building_id, 'replaces',                 [])
