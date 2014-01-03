import math
import logging
import Data_BUILDINGS
import Data_CONST
import Data_TECH
from Data_CONST import *

WORKER_BASE_BY_PLANET_MINERALS = { 0:1, 1:2, 2:3, 3:5, 4:8, }

PLANETS_SPECIALS = {
    K_SPECIAL_ARTIFACTS: {'research_bonus': +2},
    K_SPECIAL_GOLD:      {'bc_bonus':       +50.0},
}

DEFAULT_RULES = {
    'hero_levels':         (0, 60, 150, 300, 1000, 2000),
    'worker_base':         WORKER_BASE_BY_PLANET_MINERALS,
    'planets_specials':    PLANETS_SPECIALS,
    'research':            Data_TECH.RESEARCH,
    'research_areas':      Data_TECH.RESEARCH_AREAS,
    'tech_table':          Data_TECH.TECH_TABLE,
    'buildings':           Data_BUILDINGS.BUILDINGS,
    'governments':         Data_CONST.K_GOVERNMENTS,
}

# ------------------------------------------------------------------------------
def count_colony_pollution(RULES, colony, colony_leader, industry_total, PLAYERS):

    if colony.is_outpost():
        return 0

    # Basic pollution ratio due to industry vs. buildings.
    # May fall to 0 (i.e. for Core Waste Dump)
    industry = float(industry_total)

    for b_id in colony.v_building_ids:
        industry *= RULES['buildings'][b_id]['industry_pollution_ratio']
        if industry < 1.0:
            return 0

    base_tolerance = K_PLANET_TOL_BY_SIZE[colony.o_planet.i_size]

    for tech_id in PLAYERS[colony.i_owner_id].v_known_techs:
        base_tolerance *= RULES['tech_table'][tech_id]['industry_pollution_base_ratio']

    pollution = (industry - base_tolerance) / 2
    if pollution < 1.0:
        return 0

    # Per-colonist tolerance calcuation.
    total_pop    = colony.total_population()
    tolerant_pop = 0

    for t in (K_FARMER, K_SCIENTIST, K_WORKER):
        for colonist in colony.d_colonists[t]:
            if colonist.android or PLAYERS[colonist.race].get_racepick_item('tolerant'):
                tolerant_pop += 1

    pollution *= float(total_pop - tolerant_pop) / float(total_pop)

    return round(pollution)
# ------------------------------------------------------------------------------
def get_hero_bonus(hero, skill_name):
    # Note: all hero bonuses accessed here are expected to be percentages
    # expressed as a value of (0.0 -> 100.0)
    if hero and hero.has_key(skill_name):
        bonus = hero['skills'][skill_name] * (hero['level'] + 1)
        return bonus
    return 0.0
# ------------------------------------------------------------------------------
def colonist_food_base(colonist, colonist_player, planet, food_per_farmer):
    ### JWL: TODO I forget, do Natives and Androids have a fixed base?
    # if colonist.android: return K_ANDROID_FOOD_BASE  # 2.0?
    # if colonist.native:  return K_NATIVES_FOOD_BASE  # 2.0?
    # if colonist.rioting: return min(K_RIOTERS_FOOD_BASE, planet.i_foodbase)  # 1.0?
    b_is_aquatic_planet = (planet.i_terrain in [K_TERRAIN_OCEAN, K_TERRAIN_TERRAN])
    colonist_food = planet.i_foodbase
    if b_is_aquatic_planet and colonist_player.get_racepick_item('aquatic'):
        colonist_food += 1
    return colonist_food * (colonist_player.get_racepick_item('food') + 100.0) / 100.0
# ------------------------------------------------------------------------------
def colonist_industry_base(RULES, colonist, colonist_player, planet, industry_per_worker):
    # Note: natives and rioters can only be farmers, so no check done here.
    ### JWL: TODO I forget, do Androids have a fixed base?
    # if colonist.android: return K_ANDROID_RESEARCH_BASE
    colonist_industry = RULES['worker_base'][planet.i_minerals]
    return colonist_industry * (colonist_player.get_racepick_item('industry') + 100.0) / 100.0
# ------------------------------------------------------------------------------
def colonist_research_base(RULES, colonist, colonist_player, planet, research_per_scientist):
    # Note: natives and rioters can only be farmers, so no check done here.
    ### JWL: TODO I forget, do Androids have a fixed base?
    # if colonist['android']: return K_ANDROID_RESEARCH_BASE
    colonist_research = research_per_scientist
    if planet.has_artifacts():
        colonist_research += RULES['planets_specials'][K_SPECIAL_ARTIFACTS]['research_bonus']
    return colonist_research * (colonist_player.get_racepick_item('research') + 100.0) / 100.0
# ------------------------------------------------------------------------------
def colonist_morale_mult(colonist, morale_total):
    if colonist.android: return 1.0
    if colonist.rioting: return 1.0
    return morale_total / 100.0
# ------------------------------------------------------------------------------
def compose_prod_summary(RULES, colony, colony_leader, PLAYERS):
    ''' Determine the production summaries and totals for all areas. '''
    morale_base              = 0
    morale_bonus_gov         = 0
    morale_bonus_hero        = 0
    morale_bonus_building    = 0
    morale_bonus_tech        = 0
    morale_total             = 0
    food_gravity             = 0
    food_base                = 0
    food_per_farmer          = 0
    food_per_colony          = 0
    food_bonus_gov           = 0
    food_bonus_hero          = 0
    food_total               = 0
    industry_pollution       = 0
    industry_gravity         = 0
    industry_base            = 0
    industry_per_worker      = 0
    industry_per_colony      = 0
    industry_bonus_gov       = 0
    industry_bonus_hero      = 0
    industry_total           = 0
    research_gravity         = 0
    research_base            = 0
    research_per_scientist   = 0
    research_per_colony      = 0
    research_bonus_gov       = 0
    research_bonus_hero      = 0
    research_bonus_planet    = 0
    research_total           = 0

    print("=== Game_Rules.compose_prod_summary === " + colony.s_name)

    o_owner               = PLAYERS[colony.i_owner_id]
    i_owner_goverment     = o_owner.get_racepick_item('goverment')
    i_num_colonists       = colony.total_population()
    b_has_gravity_gen     = colony.has_building(Data_BUILDINGS.B_GRAVITY_GENERATOR)

    for b_id in colony.v_building_ids:
        d_building = RULES['buildings'][b_id]
        morale_bonus_gov          += d_building['morale_bonus_gov'][i_owner_goverment]
        morale_bonus_building     += d_building['morale_bonus']
        food_per_farmer           += d_building['food_per_farmer']
        food_per_colony           += d_building['food_per_colony']
        industry_per_worker       += d_building['industry_per_worker']
        industry_per_colony       += d_building['industry_per_colony']
        industry_per_colony       += d_building['industry_by_minerals'][colony.o_planet.i_minerals]
        industry_per_colony       += d_building['industry_per_colonist'] * i_num_colonists
        research_per_scientist    += d_building['research_per_scientist']
        research_per_colony       += d_building['research_per_colony']

    for tech_id in o_owner.v_known_techs:
        d_tech = RULES['tech_table'][tech_id]
        morale_bonus_gov           = max(morale_bonus_gov, d_tech['morale_bonus_gov'][i_owner_goverment])
        morale_bonus_tech         += d_tech['morale_bonus']
        food_per_farmer           += d_tech['food_per_farmer']
        industry_per_worker       += d_tech['industry_per_worker']
        research_per_scientist    += d_tech['research_per_scientist']

    # ---------------------------------------------------------------------------
    # Finish MORALE computation first --
    #     it is used as a multiplier for the others.
    # ---------------------------------------------------------------------------

    morale_base = RULES['governments'][i_owner_goverment]['morale']

    # The gov_morale_bonus is elimination of the government morale penalty,
    # so it cannot ever go above the original penalty amount.
    morale_bonus_gov  = min(20, morale_bonus_gov)

    morale_bonus_hero = get_hero_bonus(colony_leader, 'morale_bonus')

    morale_total = 100.0 + morale_base + morale_bonus_gov + morale_bonus_building + \
                   morale_bonus_tech + morale_bonus_hero

    #print("morale_base              = %s" % morale_base)
    #print("morale_bonus_gov         = %s" % morale_bonus_gov)
    #print("morale_bonus_hero        = %s" % morale_bonus_hero)
    #print("morale_bonus_building    = %s" % morale_bonus_building)
    #print("morale_bonus_tech        = %s" % morale_bonus_tech)
    #print("morale_total             = %s" % morale_total)

    # ---------------------------------------------------------------------------
    # Finish FOOD computation
    # ---------------------------------------------------------------------------

    for colonist in colony.d_colonists[K_FARMER]:
        colonist_player = PLAYERS[colonist.race]
        colonist_food   = colonist_food_base(colonist, colonist_player, colony.o_planet, food_per_farmer)
        colonist_food  *= colonist_morale_mult(colonist, morale_total)
        food_base      += colonist_food

    food_bonus_gov  = RULES['governments'][i_owner_goverment]['food_bonus']
    food_bonus_hero = get_hero_bonus(colony_leader, 'food_bonus')

    food_total      = (food_base + food_per_colony + food_gravity) * \
                      (100.0 + food_bonus_gov + food_bonus_hero) / 100.0
    food_total      = int(food_total + 0.5)

    #print("food_gravity             = %s" % food_gravity)
    #print("food_base                = %s" % food_base)
    #print("food_per_farmer          = %s" % food_per_farmer)
    #print("food_per_colony          = %s" % food_per_colony)
    #print("food_bonus_gov           = %s" % food_bonus_gov)
    #print("food_bonus_hero          = %s" % food_bonus_hero)
    #print("food_total               = %s" % food_total)

    # ---------------------------------------------------------------------------
    # Finish INDUSTRY computation
    # ---------------------------------------------------------------------------

    for colonist in colony.d_colonists[K_WORKER]:
        colonist_player    = PLAYERS[colonist.race]
        colonist_industry  = colonist_industry_base(RULES, colonist, colonist_player, colony.o_planet, industry_per_worker)
        colonist_industry *= colonist_morale_mult(colonist, morale_total)
        industry_base     += colonist_industry
        industry_gravity  += colonist_industry * colonist.get_gravity_penalty(colony.o_planet, b_has_gravity_gen)

    industry_bonus_gov  = RULES['governments'][i_owner_goverment]['industry_bonus']
    industry_bonus_hero = get_hero_bonus(colony_leader, 'industry_bonus')

    industry_total = (industry_base + industry_per_colony + industry_gravity) * \
                      (100.0 + industry_bonus_gov + industry_bonus_hero) / 100.0

    industry_pollution = count_colony_pollution(RULES, colony, colony_leader, industry_total, PLAYERS)
    industry_total    -= industry_pollution
    industry_total     = int(industry_total + 0.5)

    print("industry_pollution           = %s" % industry_pollution)
    print("industry_gravity             = %s" % industry_gravity)
    print("industry_base                = %s" % industry_base)
    print("industry_per_worker          = %s" % industry_per_worker)
    print("industry_per_colony          = %s" % industry_per_colony)
    print("industry_bonus_gov           = %s" % industry_bonus_gov)
    print("industry_bonus_hero          = %s" % industry_bonus_hero)
    print("industry_total               = %s" % industry_total)

    # ---------------------------------------------------------------------------
    # Finish RESEARCH computation
    # ---------------------------------------------------------------------------

    for colonist in colony.d_colonists[K_SCIENTIST]:
        colonist_player    = PLAYERS[colonist.race]
        colonist_research  = colonist_research_base(RULES, colonist, colonist_player, colony.o_planet, research_per_scientist)
        colonist_research *= colonist_morale_mult(colonist, morale_total)
        research_base     += colonist_research
        research_gravity  += colonist_research * colonist.get_gravity_penalty(colony.o_planet, b_has_gravity_gen)

    research_bonus_gov    = RULES['governments'][i_owner_goverment]['research_bonus']
    research_bonus_hero   = get_hero_bonus(colony_leader, 'research_bonus')
    research_bonus_planet = 25.0 if colony.o_planet.has_artifacts() else 0.0

    research_total = (research_base + research_per_colony + research_gravity) * \
                      (100.0 + research_bonus_gov + research_bonus_hero + research_bonus_planet) / 100.0
    research_total = int(research_total + 0.5)

    #print("research_gravity             = %s" % research_gravity)
    #print("research_base                = %s" % research_base)
    #print("research_per_scientist       = %s" % research_per_scientist)
    #print("research_per_colony          = %s" % research_per_colony)
    #print("research_bonus_gov           = %s" % research_bonus_gov)
    #print("research_bonus_hero          = %s" % research_bonus_hero)
    #print("research_bonus_planet        = %s" % research_bonus_planet)
    #print("research_total               = %s" % research_total)

    # ---------------------------------------------------------------------------
    # Finish BC computation
    # ---------------------------------------------------------------------------

    # TODO


    # ---------------------------------------------------------------------------
    # Compose summary
    # ---------------------------------------------------------------------------

    summary = {
        'morale_base':              morale_base,
        'morale_bonus_gov':         morale_bonus_gov,
        'morale_bonus_hero':        morale_bonus_hero,
        'morale_bonus_building':    morale_bonus_building,
        'morale_bonus_tech':        morale_bonus_tech,
        'morale_total':             morale_total,
        'food_gravity':             food_gravity,
        'food_base':                food_base,
        'food_per_farmer':          food_per_farmer,
        'food_per_colony':          food_per_colony,
        'food_bonus_gov':           food_bonus_gov,
        'food_bonus_hero':          food_bonus_hero,
        'food_total':               food_total,
        'industry_pollution':       industry_pollution,
        'industry_gravity':         industry_gravity,
        'industry_base':            industry_base,
        'industry_per_worker':      industry_per_worker,
        'industry_per_colony':      industry_per_colony,
        'industry_bonus_gov':       industry_bonus_gov,
        'industry_bonus_hero':      industry_bonus_hero,
        'industry_total':           industry_total,
        'research_gravity':         research_gravity,
        'research_base':            research_base,
        'research_per_scientist':   research_per_scientist,
        'research_per_colony':      research_per_colony,
        'research_bonus_gov':       research_bonus_gov,
        'research_bonus_hero':      research_bonus_hero,
        'research_bonus_planet':    research_bonus_planet,
        'research_total':           research_total,
    }
    print '+++++++++++++++ compose_prod_summary:'
    print summary

    return summary
# ------------------------------------------------------------------------------
def compose_bc_summaryxxx(RULES, colony, PLAYERS):
    """
    Returns BC Summary
    """
    planet = colony.planet()

    summary = {
        'taxes_collected':        0,
        'special_income':        0,
        'morale_bonus':        0,
        'government_bonus':        0,
        'stock_exchange':        0,
        'spaceport':        0,
        'trade_goods':        0
    }

    # Taxes Collected
    # TODO: do natives and androids produce taxes too?
    summary['taxes_collected'] = colony.total_population()

    # Special Income - Gold Deposits
    if planet.has_gold():
        summary['special_income'] = 5

    # Morale Bonus
    morale = float(colony.i_morale)
    summary['morale_bonus'] = round(morale * (float(sum(summary.values()))) / 100)

    # Government Bonus
    player_goverment = PLAYERS[colony.i_owner_id].get_racepick_item('goverment')
    if player_goverment == K_GOVERMENT_DEMOCRACY:
        summary['government_bonus'] = int(sum(summary.values()) / 2)

    # Planetary Stock Exchange
    if colony.has_building(Data_BUILDINGS.B_STOCK_EXCHANGE):
        summary['stock_exchange'] = summary['taxes_collected']

    # Spaceport
    if colony.has_building(Data_BUILDINGS.B_SPACEPORT):
        summary['spaceport'] = int(summary['taxes_collected'] / 2)

    # TODO: Trade Goods ... round the 50% of industry
    build_queue = colony.get_build_queue()
    if (len(build_queue) > 0) and (build_queue[0]['production_id'] == BUILD_TRADE_GOODS):
        summary['trade_goods'] = int(colony.i_industry / 2)

    return summary
# ------------------------------------------------------------------------------
def get_empty_max_populations():
    return [0, 0, 0, 0, 0, 0, 0, 0]
# ------------------------------------------------------------------------------
def compose_max_populations(RULES, colony, PLAYERS):
    v_max_populations = get_empty_max_populations()

    if colony.is_outpost():
        return v_max_populations

    # Determine basic population bonus (actual count of extra colonists).
    pop_bonus = 0
    for b_id in colony.v_building_ids:
        pop_bonus += RULES['buildings'][b_id]['pop_bonus']

    for tech_id in PLAYERS[colony.i_owner_id].v_known_techs:
        pop_bonus += RULES['tech_table'][tech_id]['pop_bonus']

    # Determine the race types actually present in this colony.
    v_present = [0, 0, 0, 0, 0, 0, 0, 0]
    for t in [K_FARMER, K_WORKER, K_SCIENTIST]:
        for colonist in colony.d_colonists[t]:
            v_present[colonist.race] = True

    # Determine the max pop based on race, planet size, and planet terrain.
    # Then add in the flat population bonus.

    i_size    = colony.o_planet.i_size
    i_terrain = colony.o_planet.i_terrain

    for i in range(K_MAX_PLAYERS):
        if v_present[i]:
            if PLAYERS[i].get_racepick_item('subterranean'):
                s_racial = 'sub'
            elif PLAYERS[i].get_racepick_item('aquatic'):
                s_racial = 'aqua'
            else:
                s_racial = ''
            if PLAYERS[i].get_racepick_item('tolerant'):
                s_racial += '-tol'
            v_max_populations[i] = pop_bonus + K_PLANET_POP[s_racial][i_size][i_terrain]

    return v_max_populations
# ------------------------------------------------------------------------------
def compose_pop_growth(RULES, colony, colony_leader, PLAYERS):
    """
    http://masteroforion2.blogspot.com/2005/09/growth-formula.html
    """
    v_pop_growth = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    if colony.is_outpost():
        return v_pop_growth

    v_pop_by_race = colony.get_aggregated_populations()
    i_total_pop   = colony.total_population()

    f_tech_bonus = 0.0
    for i_tech_id in PLAYERS[colony.i_owner_id].v_known_techs:
        f_tech_bonus += RULES['tech_table'][i_tech_id]['pop_growth'] / 100.0

    for i_race in range(K_MAX_PLAYERS):
        i_race_pop = v_pop_by_race[i_race]
        if i_race_pop > 0:
            i_max_pop = colony.v_max_populations[i_race]

            b = math.floor((2000 * i_race_pop * max(0, i_max_pop - i_total_pop) / i_max_pop) ** 0.5)

            g = PLAYERS[i_race].get_racepick_item('population') / 100.0  # g == GrowthPick
            t = f_tech_bonus    # t == Tech Bonus
            r = 0               # r == Random Bonus; TODO 1.0 when Population Boom occurring
            l = get_hero_bonus(colony_leader, 'pop_growth')  # l == Leader Bonus
            h = 0               # h == Housing; TODO Compute Housing bonus
            s = 0               # s == Starvation; TODO Compute Starvation bonus (50k pop per missing food)

            if colony.has_building(Data_BUILDINGS.B_CLONING_CENTER):
                c = 100 * i_race_pop / i_total_pop
            else:
                c = 0

            a = 1 + g + t + r + l + h

            v_pop_growth[i_race] = int(((a * b) / 100) + math.floor(c) + s)

    return v_pop_growth
# ------------------------------------------------------------------------------
def count_summary_result(summary):
    sum = 0.0
    for k in summary:
        sum += float(summary[k])
    return round(sum)
# ------------------------------------------------------------------------------
def research_costs(research_areas, area, rp):
    if not area:
        return -1
    else:
        return research_areas[area]['cost']
# ------------------------------------------------------------------------------
def research_turns(cost, progress, rp):
    if rp > 0:
        turns = int(math.ceil((float(cost) - float(progress)) / float(rp)))
        turns = turns if turns > 0 else 0
    else:
        turns = -1
    print("rules::research_turns() ... cost <%d>  progress <%d>  rp <%d>  turns <%d>" % (cost,progress,rp,turns))
    return turns
# ------------------------------------------------------------------------------
