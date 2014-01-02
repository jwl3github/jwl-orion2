TECH_NONE    = 0
TECH_UNKNOWN = 1
TECH_KNOWN   = 3

TECH_TABLE = {
    0:  {
        'name':  "",
        'area':  0,
    },
    1: {
        'name':  "Achilles Targeting Unit",
        'area':  49,
    },
    2: {
        'name':  "Adamantium Armor",
        'area':  48,
    },
    3: {
        'name':  "Advanced City Planning",
        'area':  42,
        'pop_bonus':  +5,
    },
    4: {
        'name':  "Advanced Damage Control",
        'area':  63,
    },
    5: {
        'name':  "Alien Management Center",
        'area':  73,
    },
    6: {
        'name':  "Android Farmers",
        'area':  24,
    },
    7: {
        'name':  "Android Scientists",
        'area':  24,
    },
    8: {
        'name':  "Android Workers",
        'area':  24,
    },
    9: {
        'name':  "Anti-Gravity Harness",
        'area':  36,
    },
    10: {
        'name':  "Anti-Matter Bomb",
        'area':  13,
    },
    11: {
        'name':  "Anti-Matter Drive",
        'area':  13,
    },
    12: {
        'name':  "Anti-Matter Torpedoes",
        'area':  13,
    },
    13: {
        'name':  "Anti-Missile Rockets",
        'area':  4,
    },
    14: {
        'name':  "Armor Barracks",
        'area':  20,
        'description':  "Creates tank battalions. It has 2 units when built, and adds 1 unit every 10 turns, up to half the planet's  population. Eliminates the morale penalty for dictatorship and feudal governments."
    },
    15: {
        'name':  "Artemis System Net",
        'area':  58,
    },
    16: {
        'name':  "Planet Construction",
        'area':  8,
    },
    17: {
        'name':  "Assault Shuttles",
        'area':  63,
    },
    18: {
        'name':  "Astro University",
        'area':  12,
    },
    19: {
        'name':  "Atmospheric Renewer",
        'area':  47,
    },
    20: {
        'name':  "Augmented Engines",
        'area':  5,
    },
    21: {
        'name':  "Autolab",
        'area':  25,
    },
    22: {
        'name':  "Automated Factories",
        'area':  3,
    },
    23: {
        'name':  "Automated Repair Unit",
        'area':  8,
    },
    24: {
        'name':  "Battleoids",
        'area':  19,
    },
    25: {
        'name':  "Battle Pods",
        'area':  21,
    },
    26: {
        'name':  "Battle Scanner",
        'area':  66,
    },
    27: {
        'name':  "Battlestation",
        'area':  62,
    },
    28: {
        'name':  "Bio-Terminator",
        'area':  17,
    },
    29: {
        'name':  "Biomorphic Fungi",
        'area':  70,
    },
    30: {
        'name':  "Black Hole Generator",
        'area':  0,
    },
    31: {
        'name':  "Bomber Bays",
        'area':  11,
    },
    32: {
        'name':  "Capitol",
        'area':  0,
    },
    33: {
        'name':  "Class I Shield",
        'area':  7,
    },
    34: {
        'name':  "Class III Shield",
        'area':  45,
    },
    35: {
        'name':  "Class V Shield",
        'area':  64,
    },
    36: {
        'name':  "Class VII Shield",
        'area':  61,
    },
    37: {
        'name':  "Class X Shield",
        'area':  68,
    },
    38: {
        'name':  "Cloaking Device",
        'area':  26,
    },
    39: {
        'name':  "Cloning Center",
        'area':  1,
        'description':  "Allows doctors to replace failing or damaged organs, increasing the population grow by +100K each turn as long as the current population is below the planetary maximum."
    },
    40: {
        'name':  "Colony Base",
        'area':  0,
        'description':  "Creates a colony on another planet inside the same star system as the building colony."
    },
    41: {
        'name':  "Colony Ship",
        'area':  23,
        'description':  "Capable of creating a colony in a distant star system. Will not engage in combat and will be destroyed when attacked if not escorted by a military ship."
    },
    42: {
        'name':  "Confederation",
        'area':  0,
    },
    43: {
        'name':  "Cyber-Security Link",
        'area':  14,
    },
    44: {
        'name':  "Cybertronic Computer",
        'area':  25,
    },
    45: {
        'name':  "Damper Field",
        'area':  0,
    },
    46: {
        'name':  "Dauntless Guidance System",
        'area':  56,
    },
    47: {
        'name':  "Death Ray",
        'area':  0,
    },
    48: {
        'name':  "Death Spores",
        'area':  1,
    },
    49: {
        'name':  "Deep Core Mining",
        'area':  67,
    },
    50: {
        'name':  "Core Waste Dumps",
        'area':  67,
    },
    51: {
        'name':  "Deuterium Fuel Cells",
        'area':  9,
    },
    52: {
        'name':  "Dimensional Portal",
        'area':  51,
    },
    53: {
        'name':  "Displacement Device",
        'area':  71,
    },
    54: {
        'name':  "Disrupter Cannon",
        'area':  51,
    },
    55: {
        'name':  "Doom Star Construction",
        'area':  58,
    },
    56: {
        'name':  "Reinforced Hull",
        'area':  4,
    },
    57: {
        'name':  "ECM Jammer",
        'area':  7,
    },
    58: {
        'name':  "Electronic Computer",
        'area':  28,
    },
    59: {
        'name':  "Emissions Guidance System",
        'area':  14,
    },
    60: {
        'name':  "Energy Absorber",
        'area':  37,
    },
    61: {
        'name':  "Biospheres",
        'area':  18,
    },
    62: {
        'name':  "Evolutionary Mutation",
        'area':  70,
    },
    63: {
        'name':  "Extended Fuel Tanks",
        'area':  22,
    },
    64: {
        'name':  "Fast Missile Racks",
        'area':  63,
    },
    65: {
        'name':  "Federation",
        'area':  0,
    },
    66: {
        'name':  "Fighter Bays",
        'area':  4,
    },
    67: {
        'name':  "Fighter Garrison",
        'area':  20,
    },
    68: {
        'name':  "Food Replicators",
        'area':  46,
    },
    69: {
        'name':  "Freighters",
        'area':  55,
    },
    70: {
        'name':  "Fusion Beam",
        'area':  31,
    },
    71: {
        'name':  "Fusion Bomb",
        'area':  5,
    },
    72: {
        'name':  "Fusion Drive",
        'area':  5,
    },
    73: {
        'name':  "Fusion Rifle",
        'area':  31,
    },
    74: {
        'name':  "Gaia Transformation",
        'area':  70,
    },
    75: {
        'name':  "Galactic Currency Exchange",
        'area':  32,
    },
    76: {
        'name':  "Galactic Cybernet",
        'area':  33,
    },
    77: {
        'name':  "Galactic Unification",
        'area':  0,
    },
    78: {
        'name':  "Gauss Cannon",
        'area':  64,
    },
    79: {
        'name':  "Graviton Beam",
        'area':  16,
    },
    80: {
        'name':  "Gyro Destabilizer",
        'area':  36,
    },
    81: {
        'name':  "Hard Shields",
        'area':  26,
    },
    82: {
        'name':  "Heavy Armor",
        'area':  3,
    },
    83: {
        'name':  "Heavy Fighter Bays",
        'area':  42,
    },
    84: {
        'name':  "Heightened Intelligence",
        'area':  30,
    },
    85: {
        'name':  "High Energy Focus",
        'area':  37,
    },
    86: {
        'name':  "Holo Simulator",
        'area':  60,
    },
    87: {
        'name':  "Hydroponic Farms",
        'area':  18,
    },
    88: {
        'name':  "Hyper Drive",
        'area':  38,
    },
    89: {
        'name':  "MegaFluxers",
        'area':  37,
    },
    90: {
        'name':  "Hyper-X Capacitors",
        'area':  38,
    },
    91: {
        'name':  "Hyperspace Communications",
        'area':  39,
    },
    92: {
        'name':  "Imperium",
        'area':  6,
    },
    93: {
        'name':  "Inertial Nullifier",
        'area':  71,
    },
    94: {
        'name':  "Inertial Stabilizer",
        'area':  36,
    },
    95: {
        'name':  "Interphased Drive",
        'area':  40,
    },
    96: {
        'name':  "Ion Drive",
        'area':  41,
    },
    97: {
        'name':  "Ion Pulse Cannon",
        'area':  41,
    },
    98: {
        'name':  "Iridium Fuel Cells",
        'area':  47,
    },
    99: {
        'name':  "Jump Gate",
        'area':  65,
    },
    100: {
        'name':  "Laser Cannon",
        'area':  57,
    },
    101: {
        'name':  "Laser Rifle",
        'area':  57,
    },
    102: {
        'name':  "Lightning Field",
        'area':  72,
    },
    103: {
        'name':  "Marine Barracks",
        'area':  0,
    },
    104: {
        'name':  "Mass Driver",
        'area':  7,
    },
    105: {
        'name':  "Mauler Device",
        'area':  39,
    },
    106: {
        'name':  "Merculite Missile",
        'area':  2,
    },
    107: {
        'name':  "Microbiotics",
        'area':  34,
        'pop_growth':  25.0,
    },
    108: {
        'name':  "Microlite Construction",
        'area':  53,
        'industry_per_worker': +1,
    },
    109: {
        'name':  "Outpost Ship",
        'area':  23,
        'description':  "Capable of creating an outpost on any uninhabited planet. Outposts function like a colony, except no population units may be moved there. Outpost ships are unarmed and will be destroyed if not escorted by military ships."
    },
    110: {
        'name':  "Moleculartronic Computer",
        'area':  49,
    },
    111: {
        'name':  "Multi-Wave Ecm Jammer",
        'area':  64,
    },
    112: {
        'name':  "Multi-Phased Shields",
        'area':  52,
    },
    113: {
        'name':  "Nano Disassemblers",
        'area':  53,
        'industry_pollution_base_ratio':  2.0,
    },
    114: {
        'name':  "Neural Scanner",
        'area':  15,
    },
    115: {
        'name':  "Neutron Blaster",
        'area':  54,
    },
    116: {
        'name':  "Neutron Scanner",
        'area':  54,
    },
    117: {
        'name':  "Neutronium Armor",
        'area':  50,
    },
    118: {
        'name':  "Neutronium Bomb",
        'area':  40,
    },
    119: {
        'name':  "Nuclear Bomb",
        'area':  55,
    },
    120: {
        'name':  "Nuclear Drive",
        'area':  55,
    },
    121: {
        'name':  "Nuclear Missile",
        'area':  22,
    },
    122: {
        'name':  "Optronic Computer",
        'area':  56,
    },
    123: {
        'name':  "Particle Beam",
        'area':  0,
    },
    124: {
        'name':  "Personal Shield",
        'area':  27,
    },
    125: {
        'name':  "Phase Shifter",
        'area':  0,
    },
    126: {
        'name':  "Phasing Cloak",
        'area':  68,
    },
    127: {
        'name':  "Phasor",
        'area':  52,
    },
    128: {
        'name':  "Phasor Rifle",
        'area':  52,
    },
    129: {
        'name':  "Planetary Barrier Shield",
        'area':  68,
    },
    130: {
        'name':  "Planetary Flux Shield",
        'area':  61,
    },
    131: {
        'name':  "Planetary Gravity Generator",
        'area':  16,
    },
    132: {
        'name':  "Planetary Missile Base",
        'area':  3,
    },
    133: {
        'name':  "Ground Batteries",
        'area':  19,
    },
    134: {
        'name':  "Planetary Radiation Shield",
        'area':  45,
    },
    135: {
        'name':  "Planetary Stock Exchange",
        'area':  43,
    },
    136: {
        'name':  "Planetary Supercomputer",
        'area':  60,
    },
    137: {
        'name':  "Plasma Cannon",
        'area':  59,
    },
    138: {
        'name':  "Plasma Rifle",
        'area':  59,
    },
    139: {
        'name':  "Plasma Torpedoes",
        'area':  40,
    },
    140: {
        'name':  "Plasma Web",
        'area':  59,
    },
    141: {
        'name':  "Pleasure Dome",
        'area':  49,
    },
    142: {
        'name':  "Pollution Processor",
        'area':  2,
    },
    143: {
        'name':  "Positronic Computer",
        'area':  60,
    },
    144: {
        'name':  "Powered Armor",
        'area':  62,
    },
    145: {
        'name':  "Pulse Rifle",
        'area':  0,
    },
    146: {
        'name':  "Proton Torpedoes",
        'area':  38,
    },
    147: {
        'name':                             "Psionics",
        'area':                             30,
        'morale_bonus_gov':                 [0, 0, 10, 10, 0, 0, 0], # percent
    },
    148: {
        'name':  "Pulsar",
        'area':  72,
    },
    149: {
        'name':  "Pulson Missile",
        'area':  47,
    },
    150: {
        'name':  "Quantum Detonator",
        'area':  0,
    },
    151: {
        'name':  "Rangemaster Unit",
        'area':  14,
    },
    152: {
        'name':  "Recyclotron",
        'area':  8,
    },
    153: {
        'name':  "Reflection Field",
        'area':  0,
    },
    154: {
        'name':  "Robotic Factory",
        'area':  11,
    },
    155: {
        'name':  "Research Laboratory",
        'area':  56,
    },
    156: {
        'name':  "Robo-Miners",
        'area':  62,
    },
    157: {
        'name':  "Space Scanner",
        'area':  57,
    },
    158: {
        'name':  "Scout Lab",
        'area':  15,
    },
    159: {
        'name':  "Security Stations",
        'area':  15,
    },
    160: {
        'name':  "Sensors",
        'area':  39,
    },
    161: {
        'name':  "Shield Capacitors",
        'area':  41,
    },
    162: {
        'name':  "Soil Enrichment",
        'area':  1,
    },
    163: {
        'name':  "Space Academy",
        'area':  10,
    },
    164: {
        'name':  "Spaceport",
        'area':  20,
    },
    165: {
        'name':  "Spatial Compressor",
        'area':  0,
    },
    166: {
        'name':  "Spy Network",
        'area':  0,
    },
    167: {
        'name':  "Standard Fuel Cells",
        'area':  22,
    },
    168: {
        'name':  "Star Base",
        'area':  0,
    },
    169: {
        'name':  "Star Fortress",
        'area':  42,
    },
    170: {
        'name':  "Star Gate",
        'area':  69,
    },
    171: {
        'name':  "Stasis Field",
        'area':  26,
    },
    172: {
        'name':  "Stealth Field",
        'area':  27,
    },
    173: {
        'name':  "Stealth Suit",
        'area':  27,
    },
    174: {
        'name':  "Stellar Converter",
        'area':  69,
    },
    175: {
        'name':  "Structural Analyzer",
        'area':  25,
    },
    176: {
        'name':  "Sub-Space Communications",
        'area':  65,
    },
    177: {
        'name':  "Sub-Space Teleporter",
        'area':  71,
    },
    178: {
        'name':  "Subterranean Farms",
        'area':  44,
    },
    179: {
        'name':  "Survival Pods",
        'area':  21,
    },
    180: {
        'name':  "Tachyon Communications",
        'area':  66,
    },
    181: {
        'name':  "Tachyon Scanner",
        'area':  66,
    },
    182: {
        'name':  "Telepathic Training",
        'area':  34,
    },
    183: {
        'name':  "Terraforming",
        'area':  35,
    },
    184: {
        'name':  "Thorium Fuel Cells",
        'area':  48,
    },
    185: {
        'name':  "Time Warp Facilitator",
        'area':  69,
    },
    186: {
        'name':  "Titan Construction",
        'area':  19,
    },
    187: {
        'name':  "Titanium Armor",
        'area':  22,
    },
    188: {
        'name':  "Tractor Beam",
        'area':  16,
    },
    189: {
        'name':  "Transport",
        'area':  23,
    },
    190: {
        'name':  "Transporters",
        'area':  46,
    },
    191: {
        'name':  "Tritanium Armor",
        'area':  9,
    },
    192: {
        'name':  "Troop Pods",
        'area':  21,
    },
    193: {
        'name':  "Universal Antidote",
        'area':  17,
        'pop_growth':  50.0,
    },
    194: {
        'name':  "Urridium Fuel Cells",
        'area':  50,
    },
    195: {
        'name':             "Virtual Reality Network",
        'area':             33,
        'morale_bonus':     20, # percent
    },
    196: {
        'name':  "Warp Dissipater",
        'area':  45,
    },
    197: {
        'name':  "Warp Interdictor",
        'area':  72,
    },
    198: {
        'name':  "Weather Control System",
        'area':  44,
    },
    199: {
        'name':  "Wide Area Jammer",
        'area':  61,
    },
    200: {
        'name':  "Xeno Psychology",
        'area':  73,
    },
    201: {
        'name':  "Xentronium Armor",
        'area':  0,
    },
    202: {
        'name':  "Zeon Missile",
        'area':  50,
    },
    203: {
        'name':  "Zortrium Armor",
        'area':  53,
    },
    204: {
        'name':  "Biology I",
        'area':  75,
    },
    205: {
        'name':  "Power I",
        'area':  76,
    },
    206: {
        'name':  "Physics I",
        'area':  77,
    },
    207: {
        'name':  "Construction I",
        'area':  78,
    },
    208: {
        'name':  "Fields I",
        'area':  79,
    },
    209: {
        'name':  "Chemistry I",
        'area':  80,
    },
    210: {
        'name':  "Computers I",
        'area':  81,
    },
    211: {
        'name':  "Sociology I",
        'area':  82,
    },
}

# ------------------------------------------------------------------------------
def apply_tech_key_default(tech_id, key, value):
    if not TECH_TABLE[tech_id].has_key(key):
        TECH_TABLE[tech_id][key] = value
# ------------------------------------------------------------------------------
def regularize_tech_keys():
    ''' Makes sure that the base key set is present to avoid a lot of extraneous has_key() calls. '''
    for tech_id in TECH_TABLE.keys():
        apply_tech_key_default(tech_id, 'description',            'TBD')
        apply_tech_key_default(tech_id, 'morale_bonus',           0)
        apply_tech_key_default(tech_id, 'morale_bonus_gov',       [0, 0, 0, 0, 0, 0, 0])
        apply_tech_key_default(tech_id, 'pop_bonus',              0)
        apply_tech_key_default(tech_id, 'pop_growth',             0.0)
        apply_tech_key_default(tech_id, 'food_per_farmer',        0)
        apply_tech_key_default(tech_id, 'industry_per_worker',    0)
        apply_tech_key_default(tech_id, 'research_per_scientist', 0)
        apply_tech_key_default(tech_id, 'industry_pollution_base_ratio',  1.0)
# ------------------------------------------------------------------------------
def get_technames():
    return [
        "Achilles Targeting Unit",
        "Adamantium Armor",
        "Advanced City Planning",
        "Advanced Damage Control",
        "Alien Management Center",
        "Android Farmers",
        "Android Scientists",
        "Android Workers",
        "Anti-Gravity Harness",
        "Anti-Matter Bomb",
        "Anti-Matter Drive",
        "Anti-Matter Torpedoes",
        "Anti-Missile Rockets",
        "Armor Barracks",
        "Artemis System Net",
        "Artificial Planet",
        "Assault Shuttles",
        "Astro University",
        "Atmospheric Renewer",
        "Augmented Engines",
        "Autolab",
        "Automated Factories",
        "Automated Repair Unit",
        "Battleoids",
        "Battle Pods",
        "Battle Scanner",
        "Battlestation",
        "Bio-Terminator",
        "Biomorphic Fungi",
        "Black Hole Generator",
        "Bomber Bays",
        "Capitol",
        "Class I Shield",
        "Class III Shield",
        "Class V Shield",
        "Class VII Shield",
        "Class X Shield",
        "Cloaking Device",
        "Cloning Center",
        "Colony Base",
        "Colony Ship",
        "Confederation",
        "Cyber-Security Link",
        "Cybertronic Computer",
        "Damper Field",
        "Dauntless Guidance System",
        "Death Ray",
        "Death Spores",
        "Deep Core Mining",
        "Core Waste Dumps",
        "Deuterium Fuel Cells",
        "Dimensional Portal",
        "Displacement Device",
        "Disrupter Cannon",
        "Doom Star Construction",
        "Reinforced Hull",
        "ECM Jammer",
        "Electronic Computer",
        "Emissions Guidance System",
        "Energy Absorber",
        "Biospheres",
        "Evolutionary Mutation",
        "Extended Fuel Tanks",
        "Fast Missile Racks",
        "Federation",
        "Fighter Bays",
        "Fighter Garrison",
        "Food Replicators",
        "Freighters",
        "Fusion Beam",
        "Fusion Bomb",
        "Fusion Drive",
        "Fusion Rifle",
        "Gaia Transformation",
        "Galactic Currency Exchange",
        "Galactic Cybernet",
        "Galactic Unification",
        "Gauss Auto-Cannon",
        "Graviton Beam",
        "Gyro Destabilizer",
        "Hard Shields",
        "Heavy Armor",
        "Heavy Fighter Bays",
        "Heightened Intelligence",
        "High Energy Focus",
        "Holo Simulator",
        "Hydroponic Farms",
        "Hyper Drive",
        "MegaFluxers",
        "Hyper-X Capacitors",
        "Hyperspace Communications",
        "Imperium",
        "Inertial Nullifier",
        "Inertial Stabilizer",
        "Interphased Drive",
        "Ion Drive",
        "Ion Pulse Cannon",
        "Iridium Fuel Cells",
        "Jump Gate",
        "Laser Cannon",
        "Laser Rifle",
        "Lightning Field",
        "Marine Barracks",
        "Mass Driver",
        "Mauler Device",
        "Merculite Missile",
        "Microbiotics",
        "Microlite Construction",
        "Outpost Ship",
        "Moleculartronic Computer",
        "Multi-Wave Ecm Jammer",
        "Multi-Phased Shields",
        "Nano Disassemblers",
        "Neural Scanner",
        "Neutron Blaster",
        "Neutron Scanner",
        "Neutronium Armor",
        "Neutronium Bomb",
        "Nuclear Bomb",
        "Nuclear Drive",
        "Nuclear Missile",
        "Optronic Computer",
        "Particle Beam",
        "Personal Shield",
        "Phase Shifter",
        "Phasing Cloak",
        "Phasor",
        "Phasor Rifle",
        "Planetary Barrier Shield",
        "Planetary Flux Shield",
        "Planetary Gravity Generator",
        "Planetary Missile Base",
        "Ground Batteries",
        "Planetary Radiation Shield",
        "Planetary Stock Exchange",
        "Planetary Supercomputer",
        "Plasma Cannon",
        "Plasma Rifle",
        "Plasma Torpedoes",
        "Plasma Web",
        "Pleasure Dome",
        "Pollution Processor",
        "Positronic Computer",
        "Powered Armor",
        "Pulse Rifle",
        "Proton Torpedoes",
        "Psionics",
        "Pulsar",
        "Pulson Missile",
        "Quantum Detonator",
        "Rangemaster Unit",
        "Recyclotron",
        "Reflection Field",
        "Robotic Factory",
        "Research Laboratory",
        "Robo-Miners",
        "Space Scanner",
        "Scout Lab",
        "Security Stations",
        "Sensors",
        "Shield Capacitors",
        "Soil Enrichment",
        "Space Academy",
        "Spaceport",
        "Spatial Compressor",
        "Spy Network",
        "Standard Fuel Cells",
        "Star Base",
        "Star Fortress",
        "Star Gate",
        "Stasis Field",
        "Stealth Field",
        "Stealth Suit",
        "Stellar Converter",
        "Structural Analyzer",
        "Sub-Space Communications",
        "Sub-Space Teleporter",
        "Subterranean Farms",
        "Survival Pods",
        "Tachyon Communications",
        "Tachyon Scanner",
        "Telepathic Training",
        "Terraforming",
        "Thorium Fuel Cells",
        "Time Warp Facilitator",
        "Titan Construction",
        "Titanium Armor",
        "Tractor Beam",
        "Transport",
        "Transporters",
        "Tritanium Armor",
        "Troop Pods",
        "Universal Antidote",
        "Uridium Fuel Cells",
        "Virtual Reality Network",
        "Warp Dissipater",
        "Warp Interdictor",
        "Weather Control System",
        "Wide Area Jammer",
        "Xeno Psychology",
        "Xentronium Armor",
        "Zeon Missile",
        "Zortrium Armor"
    ]

# end func get_technames
RESEARCH = {
    'construction':     { 'index': 0, 'start_area':  4, },
    'power':            { 'index': 1, 'start_area': 55, },
    'chemistry':        { 'index': 2, 'start_area': 22, },
    'sociology':        { 'index': 3, 'start_area': 10, },
    'computers':        { 'index': 4, 'start_area': 28, },
    'biology':          { 'index': 5, 'start_area': 18, },
    'physics':          { 'index': 6, 'start_area': 57, },
    'force_fields':     { 'index': 7, 'start_area':  7, },
}

RESEARCH_AREAS = {
    1:  { 'name':    "Advanced Biology",              'cost':    400,     'next':    34, },
    2:  { 'name':    "Advanced Chemistry",            'cost':    650,     'next':    47, },
    3:  { 'name':    "Advanced Construction",         'cost':    150,     'next':    21, },
    4:  { 'name':    "Advanced Engineering",          'cost':    80,      'next':    3, },
    5:  { 'name':    "Advanced Fusion",               'cost':    250,     'next':    41, },
    6:  { 'name':    "Advanced Governments",          'cost':    4500,    'next':    32, },
    7:  { 'name':    "Advanced Magnetism",            'cost':    250,     'next':    36, },
    8:  { 'name':    "Advanced Manufacturing",        'cost':    1500,    'next':    11, },
    9:  { 'name':    "Advanced Metallurgy",           'cost':    250,     'next':    2, },
    10: { 'name':    "Military Tactics",              'cost':    150,     'next':    73, },
    11: { 'name':    "Advanced Robotics",             'cost':    2000,    'next':    67, },
    12: { 'name':    "Teaching Methods",              'cost':    2000,    'next':    6, },
    13: { 'name':    "Anti-Matter Fission",           'cost':    2000,    'next':    46, },
    14: { 'name':    "Artificial Consciousness",      'cost':    1500,    'next':    25, },
    15: { 'name':    "Artificial Intelligence",       'cost':    400,     'next':    60, },
    16: { 'name':    "Artificial Gravity",            'cost':    1150,    'next':    65, },
    17: { 'name':    "Artificial Life",               'cost':    4500,    'next':    70, },
    18: { 'name':    "Astro Biology",                 'cost':    80,      'next':    1, },
    19: { 'name':    "Astro Construction",            'cost':    1150,    'next':    8, },
    20: { 'name':    "Astro Engineering",             'cost':    400,     'next':    62, },
    21: { 'name':    "Capsule Construction",          'cost':    250,     'next':    20, },
    22: { 'name':    "Chemistry",                     'cost':    50,      'next':    9, },
    23: { 'name':    "Cold Fusion",                   'cost':    80,      'next':    5, },
    24: { 'name':    "Cybertechnics",                 'cost':    3500,    'next':    33, },
    25: { 'name':    "Cybertronics",                  'cost':    2750,    'next':    24, },
    26: { 'name':    "Distortion Fields",             'cost':    3500,    'next':    61, },
    27: { 'name':    "Electromagnetic Refraction",    'cost':    1500,    'next':    72, },
    28: { 'name':    "Electronics",                   'cost':    50,      'next':    56, },
    30: { 'name':    "Evolutionary Genetics",         'cost':    2750,    'next':    17, },
    31: { 'name':    "Fusion Physics",                'cost':    150,     'next':    66, },
    32: { 'name':    "Galactic Economics",            'cost':    6000,    'next':    82, },
    33: { 'name':    "Galactic Networking",           'cost':    4500,    'next':    49, },
    34: { 'name':    "Genetic Engineering",           'cost':    900,     'next':    35, },
    35: { 'name':    "Genetic Mutations",             'cost':    1150,    'next':    44, },
    36: { 'name':    "Gravitic Fields",               'cost':    650,     'next':    45, },
    37: { 'name':    "High Energy Distribution",      'cost':    3500,    'next':    38, },
    38: { 'name':    "Hyper Dimensioanl Fission",     'cost':    4500,    'next':    40, },
    39: { 'name':    "Hyper Dimensional Physics",     'cost':    6000,    'next':    69, },
    40: { 'name':    "Interphased Fission",           'cost':    10000,   'next':    76, },
    41: { 'name':    "Ion Fission",                   'cost':    900,     'next':    13, },
    42: { 'name':    "Superscalar Construction",      'cost':    6000,    'next':    58, },
    43: { 'name':    "Macro Economics",               'cost':    1150,    'next':    12, },
    44: { 'name':    "Macro Genetics",                'cost':    1500,    'next':    30, },
    45: { 'name':    "Magneto Gravitics",             'cost':    900,     'next':    27, },
    46: { 'name':    "Matter Energy Conversion",      'cost':    2750,    'next':    37, },
    47: { 'name':    "Molecular Compression",         'cost':    1150,    'next':    53, },
    48: { 'name':    "Molecular Control",             'cost':    10000,   'next':    80, },
    49: { 'name':    "Moleculartronics",              'cost':    6000,    'next':    81, },
    50: { 'name':    "Molecular Manipulation",        'cost':    4500,    'next':    48, },
    51: { 'name':    "Multi-Dimensional Physics",     'cost':    4500,    'next':    39, },
    52: { 'name':    "Multi-Phased Physics",          'cost':    2000,    'next':    59, },
    53: { 'name':    "Nano Technology",               'cost':    2000,    'next':    50, },
    54: { 'name':    "Neutrino Physics",              'cost':    900,     'next':    16, },
    55: { 'name':    "Nuclear Fission",               'cost':    50,      'next':    23, },
    56: { 'name':    "Optronic",                      'cost':    150,     'next':    15, },
    57: { 'name':    "Physics",                       'cost':    50,      'next':    31, },
    58: { 'name':    "Planetoid Construction",        'cost':    7500,    'next':    78, },
    59: { 'name':    "Plasma Physics",                'cost':    3500,    'next':    51, },
    60: { 'name':    "Positronics",                   'cost':    900,     'next':    14, },
    61: { 'name':    "Quantum Fileds",                'cost':    4500,    'next':    71, },
    62: { 'name':    "Robotics",                      'cost':    650,     'next':    63, },
    63: { 'name':    "Servo Mechanics",               'cost':    900,     'next':    19, },
    64: { 'name':    "Subspace Fields",               'cost':    2750,    'next':    26, },
    65: { 'name':    "Subspace Physics",              'cost':    1500,    'next':    52, },
    66: { 'name':    "Tachyon Physics",               'cost':    250,     'next':    54, },
    67: { 'name':    "Tectonic Engineering",          'cost':    3500,    'next':    42, },
    68: { 'name':    "Temporal Fields",               'cost':    15000,   'next':    79, },
    69: { 'name':    "Temporal Physics",              'cost':    15000,   'next':    77, },
    70: { 'name':    "Trans Genetics",                'cost':    7500,    'next':    75, },
    71: { 'name':    "Transwarp Fields",              'cost':    7500,    'next':    68, },
    72: { 'name':    "Warp Fields",                   'cost':    2000,    'next':    64, },
    73: { 'name':    "Xeno Relations",                'cost':    650,     'next':    43, },
    75: { 'name':    "Hyper-advanced",                'cost':    25000,   'next':    0, },
    76: { 'name':    "Hyper-advanced",                'cost':    25000,   'next':    0, },
    77: { 'name':    "Hyper-advanced",                'cost':    25000,   'next':    0, },
    78: { 'name':    "Hyper-advanced",                'cost':    25000,   'next':    0, },
    79: { 'name':    "Hyper-advanced",                'cost':    25000,   'next':    0, },
    80: { 'name':    "Hyper-advanced",                'cost':    25000,   'next':    0, },
    81: { 'name':    "Hyper-advanced",                'cost':    25000,   'next':    0, },
    82: { 'name':    "Hyper-advanced",                'cost':    25000,   'next':    0, },
}

