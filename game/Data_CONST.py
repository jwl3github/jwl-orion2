import Data_TECH

K_MAX_PLAYERS             = 8
K_MAX_WEAPONS_PER_SHIP    = 8
K_MAX_STAR_OBJECTS        = 5
K_MAX_BUILD_QUEUE         = 8

K_RACE_0                  = 0
K_RACE_1                  = 1
K_RACE_2                  = 2
K_RACE_3                  = 3
K_RACE_4                  = 4
K_RACE_5                  = 5
K_RACE_6                  = 6
K_RACE_7                  = 7
K_RACE_ANTARAN            = 8
K_RACE_ORION              = 9
K_RACE_AMOEBA             = 10
K_RACE_CRYSTAL            = 11
K_RACE_DRAGON             = 12
K_RACE_EEL                = 13
K_RACE_HYDRA              = 14
K_RACE_ANDROID_FARMER     = 15   # Only used for colonist type (cannot index into d_players[])
K_RACE_ANDROID_WORKER     = 16   # Only used for colonist type (cannot index into d_players[])
K_RACE_ANDROID_SCIENTIST  = 17   # Only used for colonist type (cannot index into d_players[])
K_RACE_NATIVE             = 18   # Only used for colonist type (cannot index into d_players[])

K_SHIP_SIZE_SMALL         = 0
K_SHIP_SIZE_MEDIUM        = 1
K_SHIP_SIZE_LARGE         = 2
K_SHIP_SIZE_HUGE          = 3
K_SHIP_SIZE_TITAN         = 4
K_SHIP_SIZE_DOOMSTAR      = 5

K_SHIP_TYPE_COMBAT        = 0
K_SHIP_TYPE_COLONY        = 1
K_SHIP_TYPE_TRANSPORT     = 2
K_SHIP_TYPE_UNUSED        = 3
K_SHIP_TYPE_OUTPOST       = 4

K_SHIP_STATUS_ORBIT       = 0
K_SHIP_STATUS_TRAVEL      = 1
K_SHIP_STATUS_LAUNCH      = 2
K_SHIP_STATUS_UNKNOWN     = 3
K_SHIP_STATUS_REFIT       = 4
K_SHIP_STATUS_DELETED     = 5
K_SHIP_STATUS_BUILD       = 6

K_FONT1                   = 1
K_FONT2                   = 2
K_FONT3                   = 3
K_FONT4                   = 4
K_FONT5                   = 5
K_FONT6                   = 6

K_PALETTE_BUILD_ITEM      = [0x0, 0x141420, 0x6c688c]
K_PALETTE_PRODUCTION      = [0x0, 0x440c00, 0xac542c]
K_PALETTE_XSHIP           = [0x0, 0x802810, 0xe48820, 0xe46824]
K_PALETTE_BUILD_QUEUE     = [0x0, 0x802810, 0xe48820]
K_PALETTE_LIGHT_TEXT      = [0x0, 0x802810, 0xe48820, 0xe46824]
K_PALETTE_DARK_TEXT       = [0x0, 0x440c00, 0xac542c]
K_PALETTE_POPULATION      = [0x0, 0x141420, 0x6c688c]
K_PALETTE_TITLE           = [0x0, 0x141420, 0x6c688c, 0x605c80]
K_PALETTE_SCHEMES_FONT    = [0x0, 0x141420, 0x6c688c]
K_PALETTE_SHIP_INFO       = [0x0, 0x181818, 0x047800]
K_PALETTE_TECH            = [0x0, 0x082808, 0x0c840c]
K_PALETTE_TECH_NORMAL     = [0x0, 0x181818, 0x047800, 0x047800]
K_PALETTE_TECH_HOVER      = [0x0, 0x181818, 0x28c800, 0x28c800]
K_PALETTE_TECH_ACTIVE     = [0x0, 0x181818, 0x64d000, 0x64d000]
K_PALETTE_COMMON          = [0x0, 0x20284c, 0x789cc0]
K_PALETTE_STARNAME        = [0x0, 0x101018, 0x6c6c74]
K_PALETTE_STARDATE        = [0x0, 0x7c7c84, 0xbcbcc4]
K_PALETTE_WARN            = [0x0, 0x802810, 0xe48820]
K_PALETTE_RESEARCH        = [0x0, 0x7c7c84, 0xbcbcc4]
K_PALETTE_VIEWPORT_FONT   = [0x0, 0x181c40, 0x688cb0]
K_PALETTE_INFO            = [0x0, 0x181c40, 0x688cb0]
K_PALETTE_TITLE_SHADOW    = [0x0, 0x181c40, 0x20284c, 0x20284c]
K_PALETTE_TITLE           = [0x0, 0x181c40, 0x506c90, 0x445c80]
K_PALETTE_LIGHT_TEXT      = [0x0, 0x802810, 0xe48820, 0xe46824]
K_PALETTE_DARK_TEXT       = [0x0, 0x440c00, 0xac542c]

K_FARMER                  = 0x02
K_SCIENTIST               = 0x03
K_WORKER                  = 0x82

K_HERO_OFFICER            = 0    # Fleet-only hero
K_HERO_GOVERNOR           = 1    # Colony-only hero

# ------------------------------------------------------------------------------
K_GOVERMENT_FEUDAL        = 0
K_GOVERMENT_FEUDAL2       = 1
K_GOVERMENT_DICTATORSHIP  = 2
K_GOVERMENT_IMPERIUM      = 3
K_GOVERMENT_DEMOCRACY     = 4
K_GOVERMENT_UNIFICATION   = 6
K_GOVERMENT_UNIFICATION2  = 7
# ------------------------------------------------------------------------------
K_GOVERNMENTS = {
        0:    { 'name':              'Feudal',
                'morale':            -20,
                'ship_build_bonus':  +33.3,
                'science_bonus':     -50.0,
                'assimilate_turns':  8 },

        1:    { 'name':              'Feudal 2',
                'morale':            -20,
                'ship_build_bonus':  +33.3,
                'science_bonus':     -50.0,
                'assimilate_turns':  8 },

        2:    { 'name':              'Dictatorship',
                'morale':            -20.0,
                'spy_bonus':         +10.0,
                'assimilate_turns':  8 },

        3:    { 'name':              'Imperium',
                'morale':            -20.0,
                'spy_bonus':         +10.0,
                'assimilate_turns':  8 },

        4:    { 'name':              'Democracy',
                'spy_bonus':         -10.0,
                'research_bonus':    +50.0,
                'bc_bonus':          +50.0,
                'assimilate_turns':  4 },

        5:    { 'name':              'Democracy 2',
                'spy_bonus':         -10.0,
                'research_bonus':    +50.0,
                'bc_bonus':          +50.0,
                'assimilate_turns':  4 },

        6:    { 'name':              'Unification',
                'spy_bonus':         +15.0,
                'food_bonus':        +50.0,
                'industry_bonus':    +50.0,
                'assimilate_turns':  20 },

        7:    { 'name':              'Galactic Unification',
                'spy_bonus':         +15.0,
                'food_bonus':        +50.0,
                'industry_bonus':    +50.0,
                'assimilate_turns':  20 },
}
# ------------------------------------------------------------------------------
def apply_government_key_default(gov_id, key, value):
    if not K_GOVERNMENTS[gov_id].has_key(key):
        K_GOVERNMENTS[gov_id][key] = value
# ------------------------------------------------------------------------------
def regularize_government_keys():
    ''' Makes sure that the base key set is present to avoid a lot of extraneous has_key() calls. '''
    for gov_id in K_GOVERNMENTS.keys():
        apply_government_key_default(gov_id, 'morale',           0)
        apply_government_key_default(gov_id, 'food_bonus',       0)
        apply_government_key_default(gov_id, 'industry_bonus',   0)
        apply_government_key_default(gov_id, 'research_bonus',   0)
        apply_government_key_default(gov_id, 'spy_bonus',        0)
        apply_government_key_default(gov_id, 'bc_bonus',         0)
        apply_government_key_default(gov_id, 'ship_build_bonus', 0)
# ------------------------------------------------------------------------------

K_PLANET_LOW_G            = 0
K_PLANET_NORMAL_G         = 1
K_PLANET_HEAVY_G          = 2

K_PLANET_ASTEROID         = 1
K_PLANET_GAS_GIANT        = 2
K_PLANET_HABITABLE        = 3

K_PLANET_TOL_BY_SIZE      = [2,  4,  6,  8, 10]   # Base amount of ignored pollution; Indexed by size

'''
http://masteroforion2.blogspot.com/2005/10/maximum-population.html
'''
K_PLANET_POP = {
    #                To, Ra, Ba, De, Tu, Oc, Sw, Ar, Te, Ga
    '':           [ [ 1,  1,  1,  1,  1,  1,  2,  3,  4,  5],
                    [ 3,  3,  3,  3,  3,  3,  4,  6,  8, 10],
                    [ 4,  4,  4,  4,  4,  4,  6,  9, 12, 15],
                    [ 5,  5,  5,  5,  5,  5,  8, 12, 16, 20],
                    [ 6,  6,  6,  6,  6,  6, 10, 15, 20, 25], ],
    'aqua':       [ [ 1,  1,  1,  1,  2,  5,  2,  3,  5,  5],
                    [ 3,  3,  3,  3,  4, 10,  4,  6, 10, 10],
                    [ 4,  4,  4,  4,  6, 15,  6,  9, 15, 15],
                    [ 5,  5,  5,  5,  8, 20,  8, 12, 20, 20],
                    [ 6,  6,  6,  6, 10, 25, 10, 15, 25, 25], ],
    '-tol':       [ [ 3,  3,  3,  3,  3,  3,  3,  4,  5,  5],
                    [ 5,  5,  5,  5,  5,  5,  7,  9, 10, 10],
                    [ 8,  8,  8,  8,  8,  8, 10, 13, 15, 15],
                    [10, 10, 10, 10, 10, 10, 13, 17, 20, 20],
                    [13, 13, 13, 13, 13, 13, 16, 21, 25, 25], ],
    'sub':        [ [ 3,  3,  3,  3,  3,  3,  4,  5,  6,  7],
                    [ 7,  7,  7,  7,  7,  7,  8, 10, 12, 14],
                    [10, 10, 10, 10, 10, 10, 12, 15, 18, 21],
                    [13, 13, 13, 13, 13, 13, 16, 20, 24, 28],
                    [16, 16, 16, 16, 16, 16, 20, 25, 30, 35], ],
    'aqua-tol':   [ [ 3,  3,  3,  3,  3,  5,  3,  4,  5,  5],
                    [ 5,  5,  5,  5,  5, 10,  7,  9, 10, 10],
                    [ 8,  8,  8,  8,  8, 15, 10, 13, 15, 15],
                    [10, 10, 10, 10, 10, 20, 13, 17, 20, 20],
                    [13, 13, 13, 13, 13, 25, 16, 21, 25, 25], ],
    'sub-tol':    [ [ 5,  5,  5,  5,  5,  5,  5,  6,  7,  7],
                    [ 9,  9,  9,  9,  9,  9, 11, 13, 14, 14],
                    [14, 14, 14, 14, 14, 14, 16, 19, 21, 21],
                    [18, 18, 18, 18, 18, 18, 21, 25, 28, 28],
                    [23, 23, 23, 23, 23, 23, 26, 31, 35, 35], ],
    }

K_TERRAIN_TOXIC           = 0
K_TERRAIN_RADIATED        = 1
K_TERRAIN_BARREN          = 2
K_TERRAIN_DESERT          = 3
K_TERRAIN_TUNDRA          = 4
K_TERRAIN_OCEAN           = 5
K_TERRAIN_SWAMP           = 6
K_TERRAIN_ARID            = 7
K_TERRAIN_TERRAN          = 8
K_TERRAIN_GAIA            = 9

K_MINERAL_ULTRAPOOR       = 0
K_MINERAL_POOR            = 1
K_MINERAL_ABUNDANT        = 2
K_MINERAL_RICH            = 3
K_MINERAL_ULTRARICH       = 4
K_SPECIAL_ARTIFACTS       = 10
K_SPECIAL_GOLD            = 4

K_BUILD_TRADE_GOODS       = 0xFE

K_TECH_ANTI_MISSILE_ROCKETS       =  13
K_TECH_PLANET_CONSTRUCTION        =  16
K_TECH_COLONY_BASE                =  40
K_TECH_COLONY_SHIP                =  41
K_TECH_REINFORCED_HULL            =  56
K_TECH_BIOSPHERES                 =  61
K_TECH_FIGHTER_BAYS               =  66
K_TECH_FREIGHTERS                 =  69
K_TECH_HEIGHTENED_INTELLIGENCE    =  83
K_TECH_HYDROPONIC_FARM            =  87
K_TECH_TRANSPORT                  = 189
K_TECH_MICROLITE_CONSTRUCTION     = 107
K_TECH_OUTPOST_SHIP               = 109
K_TECH_NANO_DISASSEMBLERS         = 112
K_TECH_NEURAL_SCANNER             = 113
K_TECH_NUCLEAR_BOMB               = 119
K_TECH_PSIONICS                   = 146
K_TECH_SPACE_ACADEMY              = 163
K_TECH_SPY_NETWORK                = 165   # 166 ?
K_TECH_TELEPATHIC_TRAINING        = 181
K_TECH_TITAN_CONTRUCTION          = 186
K_TECH_VIRTUAL_REALITY_NETWORK    = 194

K_TECH_GROUP_CONSTRUCTIONS        =  1
K_TECH_GROUP_SPIES                =  2
K_TECH_GROUP_COLONY               =  3
K_TECH_GROUP_SHIP_EQUIPMENT       =  4
K_TECH_GROUP_GROUND_COMBAT        =  5
K_TECH_GROUP_MISCELANEOUS         =  6

K_TECH_REVIEW = {
    0: [],
    K_TECH_GROUP_CONSTRUCTIONS: [K_TECH_TRANSPORT, K_TECH_OUTPOST_SHIP, K_TECH_FREIGHTERS, K_TECH_COLONY_SHIP, K_TECH_COLONY_BASE]
}

K_TEXT_LIST_DICT = {
    'COLONY_TYPES':             ["Colony", "Outpost"],
    'COLONY_ASSIGNMENT':        {0x00: "???", 0x01:"Agricultural Colony", 0x02: "Industrial Colony", 0x03: "Research Colony", 0xff: "Colony"},

    'RACE_PICTURES ':           ["Alkari", "Bulrathi", "Darlok", "Elerian", "Gnolam", "Human", "Klackon", "Meklar", "Mrrshan", "Psilon", "Sakkra", "Silicoid", "Trilarian", "Android"],

    'PLANET_TYPES':             ['?', 'Asteroids', 'Gas Giant', 'Planet', '??', '???', '????', '?????'],
    'PLANET_SIZES':             ['Tiny', 'Small', 'Medium', 'Large', 'Huge'],
    'PLANET_GRAVITIES':         ['Low G', 'Normal G', 'Heavy G'],
    'PLANET_TERRAINS':          ['Toxic', 'Radiated', 'Baren', 'Desert', 'Tundra', 'Ocean', 'Swamp', 'Arid', 'Terran', 'Gaia', 'k', 'l'],
    'PLANET_MINERALS':          ['Ultra Poor', 'Poor', 'Abundant', 'Rich', 'Ultra Rich'],
    'PLANET_SPECIALS':          ['-', 'Wormhole', 'Space Debris', 'Pirate Cache', 'Gold Deposits', 'Gem Deposits', 'Natives', 'Splinter', 'Hero', 'Monster', 'Artifacts', 'Orion'],

    'PLAYER_COLORS':            ["red", "yellow", "green", "white", "blue", "brown", "purple", "orange"],
    'PLAYER_PERSONALITIES':     ["Xenophobic", "Ruthless", "Aggressive", "Erratic", "Honorable", "Pacifist", "Dishonored"],
    'PLAYER_OBJECTIVES':        ["Diplomat", "Militarist", "Expansionist", "Technologist", "Industrialist", "Ecologist"],
    'PLAYER_GOVERMENTS':        ["Feudal", "Confederation", "Dictatorship", "Imperium", "Democracy", "Federation", "Unification", "Galactic Unification"],

    'SHIP_SIZES':               ["Frigate", "Destroyer", "Cruiser", "Battleship", "Titan", "Doomstar"],
    'SHIP_TYPES':               ["Combat Ship", "Colony Ship", "Transport Ship", "???", "Outpost Ship"],
    'DRIVES':                   ["-", "Nuclear", "Fusion", "Ion", "Antimatter", "Hyperdrive", "Interphased", "no unit"],
    'ARMORS':                   ["-", "Titanium", "Tritanium", "Zortrium", "Neutronium", "Adamantium", "Xentronium"],
    'SHIELDS':                  ["-", "Class I", "Class III", "Class V", "Class VII", "Class X"],
    'COLONIST_TYPE':            {0x02: "farmer", 0x03: "scientist", 0x82: "worker"},
    'COMPUTERS':                ["-", "Electronic", "Optronic", "Positronic", "Cybertronic", "Moleculartronic"],
    'WEAPONS':                  ["None", "Mass Driver", "Gauss Cannon", "Laser Cannon", "Particle Beam", "Fusion Beam", "Ion Pulse Cannon", "Graviton Beam", "Neutron Blaster", "Phasor", "Disrupter", "Death Ray", "Plasma Cannon", "Spatial Compressor", "Nuclear Missile", "Merculite Missile", "Pulson Missile", "Zeon Missile", "Anti-Matter Torpedo", "Proton Torpedo", "Plasma Torpedo", "Nuclear Bomb", "Fusion Bomb", "Anti-Matter Bomb", "Neutronium Bomb", "Death Spore", "Bio Terminator", "Mauler Device", "Assault Shuttle", "Heavy Fighter", "Bomber", "Interceptor", "Stasis Field", "Anti-Missile Rocket", "Gyro Destabilizer", "Plasma Web", "Pulsar", "Black Hole Generator", "Stellar Converter", "Tractor Beam", "Dragon Breath", "Phasor Eye", "Crystal Ray", "Plasma Breath", "Plasma Flux", "Caustic Slime"],
    'WEAPON_ARCS':              ["-", "Forward", "Forward ext.", "", "Back ext.", "", "", "", "Back", "", "", "", "", "", "", "360", "x"],
    'WEAPON_MODS_BEAM':         ["-", "Heavy Mount", "Point Defense", "Armor piercing", "Continous", "No Range Dissipation", "Shield Piercing", "AutoFire"],
    'WEAPON_MODS_MISSILE':      ["-", "Enveloping", "Mirv", "ECCM", "Heavily Armored", "Fast", "Emimisions Guidance", "Overloaded"],

    'SHIP_EXP_LEVEL':           ["Green", "Regular", "Veteran", "Elite", "Ultra Elite"],
    'SHIP_STATUS':              ["Orbit", "Travel", "Launch", "???", "Refit", "Deleted", "Build"],
    'SHIP_SPECIALS':            [
                                    "-no-special-", "Achilles Targeting Unit", "Augmented Engines", "Automated Repair Unit", "Battle Pods", "Battle Scanner", "Cloaking Device", "Damper Field",
                                    "Displacement Device", "ECM Jammer", "Energy Absorber", "Extended Fuel Tanks", "Fast Missile Racks", "Hard Shields", "Heavy Armor", "High Energy Focus",
                                    "Hyper X Capacitors", "Inertial Nullifier", "Inertial Stabilizer", "Lightning Field", "Multi-Phased Shields", "Multi-Wave ECM Jammer", "Phase Shifter", "Phasing Cloak",
                                    "Quantum Dentonator", "Range Master Unit", "Reflection Field", "Reinforced Hull", "Scout Lab", "Security Stations", "Shield Capacitor", "Stealth Field",
                                    "Structual Analyzer", "Sub Space Teleporter", "Time Warp Facilitator", "Transporters", "Troop Pods", "Warp Dissipator", "Wide Area Jammer", "unknown special 2",
                                    "unknown special 3","unknown special 4"
                                ],

    'STAR_SIZES':               ['Small', 'Medium', 'Large'],
    'STAR_CLASSES':             ['Blue', 'White', 'Yellow', 'Orange', 'Red', 'Gray', 'Black Hole'],

    'SYSTEM_SPECIALS':          ["-", "stable wormhole", "space debris", "pirate cache", "gold deposits", "gem deposits", "natives", "splinter colony", "lost hero", "space monster", "ancient artifacts", "orion", "MAX_SYSTEM_AND_PLANET_SPECIALS"],
    'GREEK_NUM':                ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"],
    'TECH_LIST':                Data_TECH.TECH_TABLE
}

def get_dictionary():
    return K_TEXT_LIST_DICT

def get_text_list(s_type):
    return K_TEXT_LIST_DICT[s_type]

def get_planet_size_text(i_index):
    return get_text_list('PLANET_SIZES')[i_index]

def get_planet_terrain_text(i_index):
    return get_text_list('PLANET_TERRAINS')[i_index]

def get_planet_minerals_text(i_index):
    return get_text_list('PLANET_MINERALS')[i_index]

def get_planet_gravity_text(i_index):
    return get_text_list('PLANET_GRAVITIES')[i_index]

def get_greek_num_text(i_index):
    return get_text_list('GREEK_NUM')[i_index]


