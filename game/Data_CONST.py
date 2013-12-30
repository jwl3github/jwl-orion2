import Data_TECH

K_MAX_PLAYERS             = 8
K_MAX_WEAPONS_PER_SHIP    = 8
K_MAX_STAR_OBJECTS        = 5

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
K_PALETTE_COMMON          = [0x0, 0x20284c, 0x789cc0]
K_PALETTE_STARNAME        = [0x0, 0x101018, 0x6c6c74]
K_PALETTE_STARDATE        = [0x0, 0x7c7c84, 0xbcbcc4]
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

K_GOVERMENT_FEUDAL        = 0
K_GOVERMENT_FEUDAL2       = 1
K_GOVERMENT_DICTATORSHIP  = 2
K_GOVERMENT_IMPERIUM      = 3
K_GOVERMENT_DEMOCRACY     = 4
K_GOVERMENT_UNIFICATION   = 6

K_GOVERNMENTS = { 0:    { 'name': "Feudal",               'morale': 0, },
                  1:    { 'name': "Feudal 2",             'morale': 0, },
                  2:    { 'name': "Dictatorship",         'morale': -20, },
                  3:    { 'name': "Imperium",             'morale': 0, },
                  4:    { 'name': "Democracy",            'morale': 0, },
                  5:    { 'name': "Democracy 2",          'morale': 0, },
                  6:    { 'name': "Unification",          'morale': 0, },
                  7:    { 'name': "Galactic Unification", 'morale': 0, },
}

K_PLANET_LOW_G            = 0
K_PLANET_NORMAL_G         = 1
K_PLANET_HEAVY_G          = 2

K_PLANET_ASTEROID         = 1
K_PLANET_GAS_GIANT        = 2
K_PLANET_HABITABLE        = 3

K_TERRAIN_TOXIC           = 0
K_TERRAIN_RADIATED        = 1
K_TERRAIN_BARED           = 2
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

    'RACE_PICTURES ':           ["Alkari", "Bulrathi", "Darlok", "Elerian", "Gnolam", "Human", "Klackon", "Meklar", "Mrrshan", "Psilon", "Sakkra", "Silicoid", "Trilarian"],

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


