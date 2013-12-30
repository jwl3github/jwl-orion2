B_ATMOSPHERE_RENEWER		=  5
B_CORE_WASTE_DUMP		= 13
B_BIOSPHERES			= 15
#B_HOLO_SIMULATOR		= 20
#B_MARINE_BARRACKS		= 22
B_GRAVITY_GENERATOR		= 25
B_STOCK_EXCHANGE		= 29
B_RECYCLOTRON			= 33
B_ROBOTIC_FACTORY		= 34
B_SPACEPORT			= 39


"""
B_NO_BUILDING			=  0
B_ALIEN_CONTROL_CENTER		=  1
B_ARMOR_BARRACKS		=  2
B_ARTEMIS_SYSTEM_NET		=  3
B_ASTRO_UNIVERSITY		=  4
B_AUTOLAB			=  6
B_AUTOMATED_FACTORY		=  7
B_BATTLESTATION			=  8
B_CAPITOL			=  9
B_CLONING_CENTER		= 10
B_COLONY_BASE			= 11
B_DEEP_CORE_MINE		= 12
B_DIMENSIONAL_PORTAL		= 14
B_FOOD_REPLICATORS		= 16
B_GAIA_TRANSFORMATION		= 17
B_CURRENCY_EXCHANGE		= 18
B_GALACTIC_CYBERNET		= 19
B_HYDROPONIC_FARM		= 21
B_BARRIER_SHIELD		= 23
B_FLUX_SHIELD			= 24
B_MISSILE_BASE			= 26
B_GROUND_BATTERIES		= 27
B_RADIATION_SHIELD		= 28
B_SUPERCOMPUTER			= 30
B_PLEASURE_DOME			= 31
B_POLLUTION_PROCESSOR		= 32
B_RESEARCH_LAB			= 35
B_ROBO_MINER_PLANT		= 36
B_SOIL_ENRICHMENT		= 37
B_SPACE_ACADEMY			= 38
B_STAR_BASE			= 40
B_STAR_FORTRESS			= 41
B_STELLAR_CONVERTER		= 42
B_SUBTERRANEAN_FARMS		= 43
B_TERRAFORMING			= 44
B_WARP_INTERDICTOR		= 45
B_WEATHER_CONTROLLER		= 46
B_FIGHTER_GARRISON		= 47
B_ARTIFICIAL_PLANET		= 48
"""

BUILDINGS = {

# Missing Android Farmer, Worker, Scientist @ cost = 50
      0: {
        'name':     		"",
        'tech':     		0,
        'cost':     		0,
        'maint':    		0,
      },

      1: {
        'name':     		"Alien Control Center",
        'tech':     		5,
        'cost':     		111,
        'maint':    		-1,
      },

      2: {
        'name':     		"Armor Barracks",
        'tech':     		14,
        'cost':     		150,
        'maint':    		-2,
      },

      3: {
        'name':     		"Artemis System Net",
        'tech':     		15,
        'cost':     		1000,
        'maint':    		-5,
      },

      4: {
        'name':     		"Astro University",
        'tech':     		18,
        'cost':     		200,
        'maint':    		-4,
        'farmer_bonus':		+1,
        'worker_bonus':		+1,
        'scientist_bonus':	+1,
      },

      5: {
        'name':     		"Atmosphere Renewer",
        'tech':     		19,
        'cost':     		150,
        'maint':    		-3,
      },

      6: {
        'name':     		"Autolab",
        'tech':     		21,
        'cost':     		200,
        'maint':    		-3,
        'research':		+30,
      },

      7: {
        'name':     		"Automated Factory",
        'tech':     		22,
        'cost':     		60,
        'maint':    		-1,
        'worker_bonus':		+1,
        'industry':		+5,
      },

      8: {
        'name':     		"Battlestation",
        'tech':     		27,
        'cost':     		600,
        'maint':    		-3,
        'replaces':             (-1, 40),
      },

      9: {
        'name':     		"Capitol",
        'tech':     		32,
        'cost':     		0,
        'maint':    		0,
        'type':                 "capitol"
      },

     10: {
        'name':     		"Cloning Center",
        'tech':     		39,
        'cost':     		100,
        'maint':    		-2,
      },

     11: {
        'name':     		"Colony Base",
        'tech':     		40,
        'cost':     		200,
        'maint':    		-1,
        'type':                 "special"
      },

     12: {
        'name':     		"Deep Core Mine",
        'tech':     		49,
        'cost':     		250,
        'maint':    		-3,
        'worker_bonus':		+3,
        'industry':		+15,
      },

     13: {
        'name':     		"Core Waste Dump",
        'tech':     		50,
        'cost':     		200,
        'maint':    		-8,
        'replaces':             (5, 32)
      },

     14: {
        'name':     		"Dimensional Portal",
        'cost':     		500,
        'maint':    		-2,
        'tech':     		52,
      },

     15: {
        'name':     		"Biospheres",
        'cost':     		60,
        'maint':    		-1,
        'tech':     		61,
      },

     16: {
        'name':     		"Food Replicators",
        'cost':     		200,
        'maint':    		-10,
        'tech':     		68,
      },

     17: {
        'name':                 "Gaia Transformation",
        'cost':     		500,
        'maint':    		0,
        'tech':                 74,
      },

     18: {
        'name':                 "Currency Exchange",
        'cost':     		111,
        'maint':    		-1,
        'tech':                 75,
      },

     19: {
        'name':                 "Galactic Cybernet",
        'cost':     		250,
        'maint':    		-3,
        'tech':                 76,
        'research':             +15,
      },

     20: {
        'name':                 "Holo Simulator",
        'cost':     		120,
        'maint':    		-1,
        'tech':                 86,
        'morale_bonus':         20, # percent
      },

     21: {
        'name':     		"Hydroponic Farm",
        'cost':     		60,
        'maint':    		-2,
        'tech':     		87,
        'food_production':	+2,
      },

     22: {
        'name':                             "Marine Barracks",
        'tech':                             103,
        'cost':     		60,
        'maint':    		-1,
        'government_morale_bonus':          [20, 20, 20, 20, 0, 0, 0], # percent
      },

     23: {
        'name':                 "Barrier Shield",
        'tech':                 129,
        'cost':     		420,
        'maint':    		-5,
        'replaces':             (-1, 28, 24),
      },

     24: {
        'name':                 "Flux Shield",
        'tech':                 130,
        'cost':     		120,
        'maint':    		-3,
        'replaces':             (-1, 28)
      },

     25: {
        'name':                 "Gravity Generator",
        'tech':                 131,
        'cost':     		120,
        'maint':    		-2,
      },

     26: {
        'name':                 "Missile Base",
        'tech':                 132,
        'cost':     		120,
        'maint':    		-2,
      },

     27: {
        'name':                 "Ground Batteries",
        'tech':                 133,
        'cost':     		200,
        'maint':    		-2,
      },

     28: {
        'name':                 "Radiation Shield",
        'tech':                 134,
        'cost':     		80,
        'maint':    		-1,
      },

     29: {
        'name':                 "Stock Exchange",
        'tech':                 135,
        'cost':     		150,
        'maint':    		-2,
      },

     30: {
        'name':     		"Supercomputer",
        'tech':     		136,
        'cost':     		150,
        'maint':    		-2,
        'scientist_bonus':	+2,
        'research':		+10,
      },

     31: {
        'name':                 "Pleasure Dome",
        'tech':                 141,
        'cost':     		250,
        'maint':    		-3,
        'morale_bonus':         30, # percent
      },

     32: {
        'name':                 "Pollution Processor",
        'tech':                 142,
        'cost':     		80,
        'maint':    		-1,
      },

     33: {
        'name':                 "Recyclotron",
        'tech':                 152,
        'cost':     		200,
        'maint':    		-3,
        'industry_per_pop':  +1
      },

     34: {
        'name':                 "Robotic Factory",
        'tech':                 154,
        'cost':     		200,
        'maint':    		-3,
        'industry_by_minerals': [5, 8, 10, 15, 20],
      },

     35: {
        'name':     		"Research Lab",
        'tech':     		155,
        'cost':     		60,
        'maint':    		-1,
        'scientist_bonus':	+1,
        'research':		+5,
      },

     36: {
        'name':     		"Robo Miner Plant",
        'tech':     		156,
        'cost':     		150,
        'maint':    		-2,
        'worker_bonus':		+2,
        'industry':		+10,
      },

     37: {
        'name':     		"Soil Enrichment",
        'tech':     		162,
        'cost':     		120,
        'maint':    		0,
      },

     38: {
        'name':     		"Space Academy",
        'tech':     		163,
        'cost':     		100,
        'maint':    		-2,
      },

     39: {
        'name':     		"Spaceport",
        'tech':     		164,
        'cost':     		80,
        'maint':    		-1,
      },

     40: {
        'name':     		"Star Base",
        'tech':     		168,
        'cost':     		400,
        'maint':    		-2,
      },

     41: {
        'name':     		"Star Fortress",
        'tech':     		169,
        'cost':     		1500,
        'maint':    		-4,
        'replaces':             (40, 8),
      },

     42: {
        'name':     		"Stellar Converter",
        'tech':     		174,
        'cost':     		1000,
        'maint':    		-6,
      },

     43: {
        'name':     		"Subterranean Farms",
        'tech':     		178,
        'cost':     		150,
        'maint':    		-4,
        'food_production':      +4,
      },

     44: {
        'name':     		"Terraforming",
        'tech':     		183,
        'cost':     		250,
        'maint':    		0,
      },

     45: {
        'name':     		"Warp Interdictor",
        'tech':     		197,
        'cost':     		300,
        'maint':    		-3,
      },

     46: {
        'name':     		"Weather Controller",
        'tech':     		198,
        'cost':     		200,
        'maint':    		-3,
        'farmer_bonus':		+2,
      },

     47: {
        'name':     		"Fighter Garrison",
        'tech':     		67,
        'cost':     		150,
        'maint':    		-2,
      },

     48: {
        'name':     		"Artificial Planet",
        'tech':     		16,
        'cost':     		1111,
        'maint':    		0,
      },

    90: {
        'name':     		"? BUILDING 90 ?",
        'tech':     		0,
        'cost':     		0,
        'maint':    		0,
      },

    96: {
        'name':     		"? BUILDING 96 ?",
        'tech':     		0,
        'cost':     		0,
        'maint':    		0,
      },

    105: {
        'name':     		"? BUILDING 105 ?",
        'tech':     		0,
        'cost':     		0,
        'maint':    		0,
      },

    106: {
        'name':     		"? BUILDING 106 ?",
        'tech':     		0,
        'cost':     		0,
        'maint':    		0,
      },

    107: {
        'name':     		"? BUILDING 107 ?",
        'tech':     		0,
        'cost':     		0,
        'maint':    		0,
      },

    108: {
        'name':     		"? BUILDING 108 ?",
        'tech':     		0,
        'cost':     		0,
        'maint':    		0,
      },

    112: {
        'name':     		"? BUILDING 112 ?",
        'tech':     		0,
        'cost':     		0,
        'maint':    		0,
      },

    116: {
        'name':     		"? BUILDING 116 ?",
        'tech':     		0,
        'cost':     		0,
        'maint':    		0,
      },

    117: {
        'name':     		"? BUILDING 117 ?",
        'tech':     		0,
        'cost':     		0,
        'maint':    		0,
      },

    123: {
        'name':     		"? BUILDING 123 ?",
        'tech':     		0,
        'cost':     		0,
        'maint':    		0,
      },

    124: {
        'name':     		"? BUILDING 124 ?",
        'tech':     		0,
        'cost':     		0,
        'maint':    		0,
      },

    128: {
        'name':     		"? BUILDING 128 ?",
        'tech':     		0,
        'cost':     		0,
        'maint':    		0,
      },

    141: {
        'name':     		"Transport Ship",
        'tech':     		189,
        'cost':     		100,
        'maint':    		-1,
        'type':                 "xship"
      },

    142: {
        'name':     		"Outpost Ship",
        'tech':     		109,
        'cost':     		100,
        'maint':    		0,
        'type':                 "xship"
      },

    143: {
        'name':     		"Colony Ship",
        'tech':     		41,
        'cost':     		500,
        'maint':    		0,
        'type':                 "xship"
      },

    144: {
        'name':     		"ship design # 4",
        'tech':     		0,
        'cost':     		0,
        'maint':    		0,
      },

    145: {
        'name':     		"ship design # 3",
        'tech':     		0,
        'cost':     		0,
        'maint':    		0,
      },

    146: {
        'name':     		"? production_id 146 ?",
        'tech':     		0,
        'cost':     		0,
        'maint':    		0,
      },

    147: {
        'name':     		"ship design # 2",
        'tech':     		0,
        'cost':     		0,
        'maint':    		0,
      },

    148: {
        'name':     		"ship design # 1",
        'tech':     		0,
        'cost':     		0,
        'maint':    		0,
      },

    149: {
        'name':     		"? production_id 149 ?",
        'tech':     		0,
        'cost':     		0,
        'maint':    		0,
      },

    150: {
        'name':     		"ship design # 0",
        'tech':     		0,
        'cost':     		0,
        'maint':    		0,
      },

    151: {
        'name':     		"? production_id 151 ?",
        'tech':     		0,
        'cost':     		0,
        'maint':    		0,
      },

    152: {
        'name':     		"? production_id 152 ?",
        'tech':     		0,
        'cost':     		0,
        'maint':    		0,
      },

    153: {
        'name':     		"ship design # X",
        'tech':     		0,
        'cost':     		0,
        'maint':    		0,
      },

    214: {
        'name':     		"Freighter Fleet",
        'tech':     		69,
        'cost':     		50,
        'maint':    		-1,
        'type':                 "xship"
      },

    241: {
        'name':     		"? BUILDING 241 ?",
        'tech':     		0,
        'cost':     		0,
        'maint':    		0,
      },

    246: {
        'name':     		"Spy",
        'tech':     		166,
        'cost':     		100,
        'maint':    		-1,
        'type':                 "special"
      },

    249: {
        'name':     		"^ Repeat ^",
        'tech':     		0,
        'cost':     		0,
        'maint':    		0,
        'type':    		"repeat"
      },

    253: {
        'name':     		"Housing",
        'tech':     		0,
        'cost':     		0,
        'maint':    		0,
        'type':                 "housing"
      },

    254: {
        'name':     		"Trade Goods",
        'tech':     		0,
        'cost':     		0,
        'maint':    		0,
        'type':                 "trade"
      },
}
